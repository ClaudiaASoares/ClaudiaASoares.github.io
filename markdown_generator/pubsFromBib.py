#!/usr/bin/env python
# coding: utf-8

"""Convert BibTeX publications into AcademicPages Markdown files.

Run this script from the `markdown_generator` directory:

    python pubsFromBib.py

It reads `pubs.bib` and writes one Markdown file per usable entry into
`../_publications`.
"""

from __future__ import annotations

import html
import os
import re
from time import strptime
from typing import Optional

from pybtex.database import Entry, Person
from pybtex.database.input import bibtex


PUBS_FILE = "pubs.bib"
OUTPUT_DIR = "../_publications"
COLLECTION_NAME = "publications"
PERMALINK_PREFIX = "/publication/"

VENUE_FIELDS = (
    "journal",
    "journaltitle",
    "booktitle",
    "series",
    "publisher",
    "school",
    "institution",
    "organization",
    "howpublished",
)

HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
}


def html_escape(text: str) -> str:
    """Escape characters that make YAML front matter fragile."""
    return "".join(HTML_ESCAPE_TABLE.get(character, character) for character in text)


def clean_bibtex_text(text: Optional[str]) -> str:
    if not text:
        return ""
    cleaned = (
        str(text)
        .replace("{", "")
        .replace("}", "")
        .replace("\\", "")
        .replace("\n", " ")
    )
    return re.sub(r"\s+", " ", cleaned).strip()


def month_number(month: Optional[str]) -> str:
    if not month:
        return "01"
    month = clean_bibtex_text(month)
    if month.isdigit():
        return f"{int(month):02d}" if 1 <= int(month) <= 12 else "01"
    try:
        return f"{strptime(month[:3], '%b').tm_mon:02d}"
    except ValueError:
        return "01"


def day_number(day: Optional[str]) -> str:
    if not day:
        return "01"
    match = re.search(r"\d{1,2}", str(day))
    if not match:
        return "01"
    day_int = int(match.group(0))
    return f"{day_int:02d}" if 1 <= day_int <= 31 else "01"


def publication_date(fields: dict[str, str]) -> Optional[str]:
    year = clean_bibtex_text(fields.get("year"))
    match = re.search(r"\d{4}", year)
    if not match:
        return None
    return (
        f"{match.group(0)}-"
        f"{month_number(fields.get('month'))}-"
        f"{day_number(fields.get('day'))}"
    )


def publication_venue(fields: dict[str, str]) -> str:
    for field in VENUE_FIELDS:
        venue = clean_bibtex_text(fields.get(field))
        if venue:
            return venue
    return "Publication"


def person_name(person: Person) -> str:
    parts = []
    for names in (
        person.first_names,
        person.middle_names,
        person.prelast_names,
        person.last_names,
        person.lineage_names,
    ):
        parts.extend(clean_bibtex_text(str(name)) for name in names)
    return " ".join(part for part in parts if part).strip()


def authors_text(entry: Entry) -> str:
    authors = [person_name(person) for person in entry.persons.get("author", [])]
    authors = [author for author in authors if author]
    if authors:
        return ", ".join(authors)
    return "Unknown author"


def url_for_entry(fields: dict[str, str]) -> Optional[str]:
    url = clean_bibtex_text(fields.get("url"))
    if url:
        return url
    doi = clean_bibtex_text(fields.get("doi"))
    if doi:
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
        doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
        return f"https://doi.org/{doi}"
    return None


def slug_for_title(title: str) -> str:
    clean_title = title.replace(" ", "-")
    url_slug = re.sub(r"\[.*\]|[^a-zA-Z0-9_-]", "", clean_title)
    return re.sub(r"-+", "-", url_slug).strip("-") or "publication"


def markdown_for_entry(entry: Entry) -> Optional[tuple[str, str]]:
    fields = entry.fields
    title = clean_bibtex_text(fields.get("title"))
    if not title:
        return None

    pub_date = publication_date(fields)
    if not pub_date:
        return None

    pub_year = pub_date[:4]
    venue = publication_venue(fields)
    url_slug = slug_for_title(title)
    html_filename = f"{pub_date}-{url_slug}"
    md_filename = os.path.basename(f"{html_filename}.md")
    paper_url = url_for_entry(fields)
    note = clean_bibtex_text(fields.get("note"))

    citation = (
        f'{authors_text(entry)}, "{html_escape(title)}." '
        f"{html_escape(venue)}, {pub_year}."
    )

    md = f'---\ntitle: "{html_escape(title)}"\n'
    md += f"collection: {COLLECTION_NAME}"
    md += f"\npermalink: {PERMALINK_PREFIX}{html_filename}"
    if note:
        md += f"\nexcerpt: '{html_escape(note)}'"
    md += f"\ndate: {pub_date}"
    md += f"\nvenue: '{html_escape(venue)}'"
    if paper_url:
        md += f"\npaperurl: '{paper_url}'"
    md += f"\ncitation: '{citation}'"
    md += "\n---"

    if note:
        md += f"\n{html_escape(note)}\n"

    if paper_url:
        md += f'\n[Access paper here]({paper_url}){{:target="_blank"}}\n'
    else:
        scholar_query = html.escape(title.replace(" ", "+"))
        md += (
            "\nUse [Google Scholar]"
            f"(https://scholar.google.com/scholar?q={scholar_query})"
            '{:target="_blank"} for full citation'
        )

    return md_filename, md


def main() -> int:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(PUBS_FILE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    written = 0
    skipped = 0
    for bib_id, entry in bibdata.entries.items():
        rendered = markdown_for_entry(entry)
        if not rendered:
            title = clean_bibtex_text(entry.fields.get("title")) or bib_id
            print(f'WARNING Skipping entry with missing title or year: "{title}"')
            skipped += 1
            continue

        md_filename, md = rendered
        with open(os.path.join(OUTPUT_DIR, md_filename), "w", encoding="utf-8") as file:
            file.write(md)
        short_title = clean_bibtex_text(entry.fields.get("title"))[:60]
        print(f'SUCCESSFULLY PARSED {bib_id}: "{short_title}"')
        written += 1

    print(f"Finished publication generation: {written} written, {skipped} skipped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
