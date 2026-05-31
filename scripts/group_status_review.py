#!/usr/bin/env python3
"""Generate a manual review checklist for group member professional status.

The script intentionally does not scrape LinkedIn. It classifies LinkedIn
profiles for manual review and optionally fetches lightweight metadata from
public non-LinkedIn profile pages.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")
HEADING_UNDERLINE_RE = re.compile(r"^-{3,}\s*$")
META_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
META_DESCRIPTION_RE = re.compile(
    r'<meta\s+[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\'][^>]*>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")


@dataclass
class Person:
    section: str
    name: str
    url: str
    details: str
    source_line: int

    @property
    def profile_type(self) -> str:
        if not self.url:
            return "missing"
        hostname = urllib.parse.urlparse(self.url).hostname or ""
        if "linkedin.com" in hostname:
            return "linkedin"
        return "public"


def strip_markdown_links(text: str) -> str:
    return LINK_RE.sub(lambda match: match.group(1), text)


def clean_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_html_text(text: str) -> str:
    return html.unescape(clean_spaces(TAG_RE.sub("", text)))


def parse_group_page(path: Path) -> list[Person]:
    lines = path.read_text(encoding="utf-8").splitlines()
    people: list[Person] = []
    section = "Unsectioned"

    for index, line in enumerate(lines):
        if index + 1 < len(lines) and HEADING_UNDERLINE_RE.match(lines[index + 1]):
            section = clean_spaces(strip_markdown_links(line))

        if not line.startswith("* "):
            continue

        bullet = line[2:].strip()
        first_link = LINK_RE.match(bullet)
        if first_link:
            name = clean_spaces(first_link.group(1))
            url = first_link.group(2).strip()
            details = bullet[first_link.end() :].strip()
        else:
            name = clean_spaces(re.split(r"\s+\(", bullet, maxsplit=1)[0])
            url = ""
            details = bullet[len(name) :].strip()

        if name:
            people.append(
                Person(
                    section=section,
                    name=name,
                    url=url,
                    details=clean_spaces(strip_markdown_links(details)),
                    source_line=index + 1,
                )
            )

    return people


def fetch_public_metadata(url: str, timeout: float) -> tuple[str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 group-status-review; "
                "+https://github.com/ClaudiaASoares/ClaudiaASoares.github.io"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("content-type", "")
        charset = response.headers.get_content_charset() or "utf-8"
        if "text/html" not in content_type:
            return "", f"Non-HTML response: {content_type or 'unknown content type'}"
        body = response.read(250_000).decode(charset, errors="replace")

    title_match = META_TITLE_RE.search(body)
    description_match = META_DESCRIPTION_RE.search(body)
    title = clean_html_text(title_match.group(1)) if title_match else ""
    description = (
        clean_html_text(description_match.group(1))
        if description_match
        else ""
    )
    return title, description


def format_person(person: Person, metadata: dict[str, tuple[str, str]]) -> str:
    profile = person.url or "no profile link"
    details = person.details or "no current details recorded"
    extra = ""
    if person.url in metadata:
        title, description = metadata[person.url]
        parts = []
        if title:
            parts.append(f"title: {title}")
        if description:
            parts.append(f"description: {description}")
        if parts:
            extra = "\n  - public page hints: " + "; ".join(parts)

    return (
        f"- [ ] {person.name} ({person.section}, line {person.source_line})\n"
        f"  - profile: {profile}\n"
        f"  - current page text: {details}\n"
        f"  - status update: TODO{extra}"
    )


def build_report(
    people: list[Person],
    metadata: dict[str, tuple[str, str]],
    source_path: Path,
) -> str:
    generated_at = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    public_profiles = [person for person in people if person.profile_type == "public"]
    linkedin_profiles = [person for person in people if person.profile_type == "linkedin"]
    missing_profiles = [person for person in people if person.profile_type == "missing"]

    sections = [
        "# Group Professional Status Review",
        "",
        f"Generated: {generated_at}",
        f"Source: `{source_path}`",
        "",
        "Use this checklist to update professional status in `_pages/group.md`.",
        "Public profile pages are listed first because they are safer to review than LinkedIn.",
        "LinkedIn entries are marked for manual review; this workflow does not scrape LinkedIn.",
        "",
        "## Public Profile Pages",
        "",
        *(format_person(person, metadata) for person in public_profiles),
        "",
        "## LinkedIn Manual Review",
        "",
        *(format_person(person, metadata) for person in linkedin_profiles),
        "",
        "## Missing Profile Link",
        "",
        *(format_person(person, metadata) for person in missing_profiles),
        "",
    ]
    return "\n".join(sections)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a review checklist for group member professional status."
    )
    parser.add_argument(
        "--source",
        default="_pages/group.md",
        type=Path,
        help="Markdown group page to parse.",
    )
    parser.add_argument(
        "--output",
        default="reports/group_status_review.md",
        type=Path,
        help="Markdown checklist to write.",
    )
    parser.add_argument(
        "--fetch-public",
        action="store_true",
        help="Fetch title and description from non-LinkedIn public profile pages.",
    )
    parser.add_argument(
        "--timeout",
        default=8.0,
        type=float,
        help="Timeout in seconds for each public page fetch.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    people = parse_group_page(args.source)
    metadata: dict[str, tuple[str, str]] = {}

    if args.fetch_public:
        public_urls = sorted({person.url for person in people if person.profile_type == "public"})
        for url in public_urls:
            try:
                metadata[url] = fetch_public_metadata(url, args.timeout)
            except (urllib.error.URLError, TimeoutError, ValueError) as error:
                metadata[url] = ("", f"Could not fetch page metadata: {error}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_report(people, metadata, args.source), encoding="utf-8")

    print(f"Wrote {args.output} with {len(people)} people.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
