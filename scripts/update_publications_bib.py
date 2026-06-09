#!/usr/bin/env python3
"""Update publication BibTeX from ORCID, OpenAlex, OpenReview, and DOI metadata.

The default mode is intentionally conservative:

* fetch candidate works from ORCID and OpenAlex using the ORCID iD in
  `_config.yml`;
* fetch accepted public OpenReview notes for the configured OpenReview profile;
* prefer DOI content negotiation for canonical BibTeX records;
* keep preprints only as `preprinturl` links on matching publications;
* copy abstracts from BibTeX, OpenAlex, or OpenReview when available;
* write a generated snapshot to `markdown_generator/generated_pubs.bib`;
* append only records that are missing from `markdown_generator/pubs.bib`.

That keeps the existing hand-curated BibTeX formatting stable while still
letting scheduled automation propose newly discovered publications.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional

try:
    from pybtex.database import BibliographyData, Entry, Person
    from pybtex.database.input import bibtex
    from pybtex.database.output import bibtex as bibtex_output
except ImportError as exc:  # pragma: no cover - exercised by users without deps.
    raise SystemExit(
        "Missing or incompatible dependency: pybtex. "
        "Install it with `pip install -r requirements-publications.txt`. "
        f"Original import error: {exc}"
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "_config.yml"
DEFAULT_OUTPUT_BIB = REPO_ROOT / "markdown_generator" / "pubs.bib"
DEFAULT_GENERATED_BIB = REPO_ROOT / "markdown_generator" / "generated_pubs.bib"
DEFAULT_MANUAL_BIB = REPO_ROOT / "markdown_generator" / "manual_pubs.bib"
DEFAULT_OPENREVIEW_PROFILE = "~Claudia_Soares1"

USER_AGENT = "ClaudiaASoares.github.io publication updater (GitHub Actions)"

OPENREVIEW_REJECTED_TERMS = (
    "submitted",
    "withdrawn",
    "rejected",
    "desk reject",
    "under review",
    "not accepted",
)

OPENREVIEW_IMPORTED_VENUE_PREFIXES = (
    "dblp.org/",
)

PREPRINT_TERMS = (
    "arxiv",
    "corr",
    "biorxiv",
    "medrxiv",
    "ssrn",
    "preprint",
)

MONTH_WORDS = (
    "jan",
    "january",
    "feb",
    "february",
    "mar",
    "march",
    "apr",
    "april",
    "may",
    "jun",
    "june",
    "jul",
    "july",
    "aug",
    "august",
    "sep",
    "sept",
    "september",
    "oct",
    "october",
    "nov",
    "november",
    "dec",
    "december",
)


@dataclass(frozen=True)
class WorkCandidate:
    source: str
    doi: Optional[str]
    title: Optional[str]
    year: Optional[str]
    openalex_work: Optional[dict[str, Any]] = None
    openreview_note: Optional[dict[str, Any]] = None


@dataclass
class RunStats:
    orcid_candidates: int = 0
    openalex_candidates: int = 0
    openreview_candidates: int = 0
    doi_fetches: int = 0
    doi_failures: int = 0
    synthesized: int = 0
    generated_entries: int = 0
    existing_entries: int = 0
    new_entries: int = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update markdown_generator/pubs.bib from open publication metadata."
    )
    parser.add_argument(
        "--orcid",
        help="ORCID iD or ORCID URL. Defaults to author.orcid in _config.yml.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Jekyll config file used to discover ORCID and email.",
    )
    parser.add_argument(
        "--output-bib",
        type=Path,
        default=DEFAULT_OUTPUT_BIB,
        help="Final BibTeX file consumed by the site generator.",
    )
    parser.add_argument(
        "--generated-bib",
        type=Path,
        default=DEFAULT_GENERATED_BIB,
        help="Generated BibTeX snapshot written on each run.",
    )
    parser.add_argument(
        "--manual-bib",
        type=Path,
        default=DEFAULT_MANUAL_BIB,
        help="Optional curated BibTeX file. Matching records override generated metadata.",
    )
    parser.add_argument(
        "--no-openalex",
        action="store_true",
        help="Do not use OpenAlex as a fallback/complementary source.",
    )
    parser.add_argument(
        "--include-openalex-only",
        action="store_true",
        help="Also import OpenAlex records that are not matched to an ORCID work.",
    )
    parser.add_argument(
        "--openreview-profile",
        default=os.environ.get("OPENREVIEW_PROFILE", DEFAULT_OPENREVIEW_PROFILE),
        help=(
            "OpenReview profile tilde ID to scan for accepted public papers. "
            "Use an empty value to disable. Defaults to ~Claudia_Soares1."
        ),
    )
    parser.add_argument(
        "--no-openreview",
        action="store_true",
        help="Do not use OpenReview as a publication source.",
    )
    parser.add_argument(
        "--include-openreview-imports",
        action="store_true",
        help="Also import DBLP/CoRR-style records shown on the OpenReview profile.",
    )
    parser.add_argument(
        "--no-generated-bib",
        action="store_true",
        help="Do not write the generated BibTeX snapshot.",
    )
    parser.add_argument(
        "--rewrite-output",
        action="store_true",
        help="Rewrite output-bib as a normalized merge instead of appending only new records.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and compare records without writing files.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.2,
        help="Delay between DOI metadata requests.",
    )
    parser.add_argument(
        "--max-openalex-pages",
        type=int,
        default=10,
        help="Maximum OpenAlex cursor pages to read.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print more detail about skipped records and fetch failures.",
    )
    return parser.parse_args()


def text_value(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, dict):
        if "value" in value:
            return text_value(value["value"])
        return None
    text = str(value).strip()
    return text or None


def read_config_scalar(path: Path, key: str) -> Optional[str]:
    if not path.exists():
        return None
    pattern = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*(?:#.*)?$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        value = match.group(1).strip()
        if value[:1] in {"'", '"'} and value[-1:] == value[:1]:
            value = value[1:-1]
        return value.strip() or None
    return None


def normalize_orcid(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    match = re.search(r"\d{4}-\d{4}-\d{4}-\d{3}[\dXx]", value)
    if not match:
        return None
    return match.group(0).upper()


def normalize_openreview_profile(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    value = value.strip()
    if not value:
        return None
    value = re.sub(r"^https?://openreview\.net/profile\?id=", "", value)
    value = urllib.parse.unquote(value)
    if not value.startswith("~"):
        value = f"~{value}"
    return value


def normalize_doi(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    doi = urllib.parse.unquote(value).strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    doi = doi.strip().strip("<>")
    doi = re.sub(r"[\s.,;)\]]+$", "", doi)
    if not doi.lower().startswith("10."):
        return None
    return doi.lower()


def normalize_title(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    title = value.lower()
    title = title.replace("{", "").replace("}", "").replace("\\", "")
    title = re.sub(r"[^a-z0-9]+", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title or None


def openalex_abstract(work: dict[str, Any]) -> Optional[str]:
    inverted_index = work.get("abstract_inverted_index")
    if not isinstance(inverted_index, dict):
        return None
    positions: list[tuple[int, str]] = []
    for word, indexes in inverted_index.items():
        if not isinstance(indexes, list):
            continue
        positions.extend((index, word) for index in indexes if isinstance(index, int))
    if not positions:
        return None
    return " ".join(word for _index, word in sorted(positions))


def entry_is_preprint(entry: Entry) -> bool:
    doi = normalize_doi(entry.fields.get("doi"))
    if doi and doi.startswith("10.48550/arxiv"):
        return True
    for field in (
        "journal",
        "journaltitle",
        "booktitle",
        "publisher",
        "howpublished",
        "archiveprefix",
        "eprinttype",
        "url",
    ):
        value = text_value(entry.fields.get(field))
        if value and any(term in value.lower() for term in PREPRINT_TERMS):
            return True
    return False


def arxiv_pdf_url(value: Optional[str]) -> Optional[str]:
    value = text_value(value)
    if not value:
        return None
    doi_match = re.search(r"10\.48550/arxiv\.([^\s/]+)", value, flags=re.IGNORECASE)
    if doi_match:
        return f"https://arxiv.org/pdf/{doi_match.group(1)}.pdf"
    arxiv_match = re.search(
        r"arxiv\.org/(?:abs|pdf)/([^?#\s]+)",
        value,
        flags=re.IGNORECASE,
    )
    if arxiv_match:
        arxiv_id = arxiv_match.group(1).removesuffix(".pdf")
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    return None


def preprint_url_for_entry(entry: Entry) -> Optional[str]:
    for field in ("preprintpdfurl", "preprinturl", "url", "doi", "eprint"):
        value = text_value(entry.fields.get(field))
        if not value:
            continue
        if pdf_url := arxiv_pdf_url(value):
            return pdf_url
        if field in {"preprintpdfurl", "preprinturl", "url"}:
            return value
    return None


def enrich_entry_from_candidate(entry: Entry, candidate: WorkCandidate) -> None:
    if not entry.fields.get("abstract"):
        abstract = None
        if candidate.openalex_work:
            abstract = openalex_abstract(candidate.openalex_work)
        elif candidate.openreview_note:
            abstract = openreview_text(candidate.openreview_note, "abstract")
        if abstract:
            entry.fields["abstract"] = abstract


def entry_identity(entry: Entry) -> Optional[tuple[str, str]]:
    identities = entry_identities(entry)
    if not identities:
        return None
    for identity in identities:
        if identity[0] == "doi":
            return identity
    return sorted(identities)[0]


def entry_identities(entry: Entry) -> set[tuple[str, str]]:
    identities: set[tuple[str, str]] = set()
    doi = normalize_doi(entry.fields.get("doi"))
    if doi:
        identities.add(("doi", doi))
    title = normalize_title(entry.fields.get("title"))
    if title:
        identities.add(("title", title))
    return identities


def candidate_identity(candidate: WorkCandidate) -> Optional[tuple[str, str]]:
    identities = candidate_identities(candidate)
    if not identities:
        return None
    for identity in identities:
        if identity[0] == "doi":
            return identity
    return sorted(identities)[0]


def candidate_identities(candidate: WorkCandidate) -> set[tuple[str, str]]:
    identities: set[tuple[str, str]] = set()
    if candidate.doi:
        identities.add(("doi", candidate.doi))
    title = normalize_title(candidate.title)
    if title:
        identities.add(("title", title))
    return identities


def http_get_text(url: str, headers: dict[str, str], timeout: float) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            **headers,
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def http_get_json(url: str, timeout: float) -> dict[str, Any]:
    body = http_get_text(url, {"Accept": "application/json"}, timeout)
    return json.loads(body)


def extract_external_ids(container: dict[str, Any], external_id_type: str) -> list[str]:
    ids = (
        container.get("external-ids", {}).get("external-id", [])
        if isinstance(container, dict)
        else []
    )
    values: list[str] = []
    for item in ids:
        item_type = text_value(item.get("external-id-type"))
        if (item_type or "").lower() != external_id_type.lower():
            continue
        value = text_value(item.get("external-id-value"))
        if value:
            values.append(value)
        external_url = item.get("external-id-url") or {}
        url = text_value(
            external_url.get("value")
            if isinstance(external_url, dict)
            else external_url
        )
        if url:
            values.append(url)
    return values


def publication_year(summary: dict[str, Any]) -> Optional[str]:
    date = summary.get("publication-date") or {}
    year = text_value(date.get("year"))
    return year if year and re.fullmatch(r"\d{4}", year) else None


def publication_title(summary: dict[str, Any]) -> Optional[str]:
    title = summary.get("title") or {}
    return text_value(title.get("title"))


def openreview_content_value(note: dict[str, Any], key: str) -> Any:
    content = note.get("content") or {}
    value = content.get(key)
    if isinstance(value, dict) and "value" in value:
        return value["value"]
    return value


def openreview_text(note: dict[str, Any], key: str) -> Optional[str]:
    return text_value(openreview_content_value(note, key))


def openreview_list(note: dict[str, Any], key: str) -> list[str]:
    value = openreview_content_value(note, key)
    if value is None:
        return []
    if isinstance(value, list):
        return [text for item in value if (text := text_value(item))]
    text = text_value(value)
    return [text] if text else []


def best_orcid_summary(group: dict[str, Any]) -> Optional[dict[str, Any]]:
    summaries = group.get("work-summary") or []
    if not summaries:
        return None

    def display_index(summary: dict[str, Any]) -> int:
        try:
            return int(summary.get("display-index") or 0)
        except (TypeError, ValueError):
            return 0

    return max(summaries, key=display_index)


def fetch_orcid_candidates(orcid: str, timeout: float) -> list[WorkCandidate]:
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    data = http_get_json(url, timeout)
    candidates: list[WorkCandidate] = []
    for group in data.get("group") or []:
        summary = best_orcid_summary(group)
        if not summary:
            continue
        title = publication_title(summary)
        year = publication_year(summary)
        doi_values = extract_external_ids(group, "doi")
        doi_values.extend(extract_external_ids(summary, "doi"))
        dois = sorted({doi for value in doi_values if (doi := normalize_doi(value))})
        if not dois:
            candidates.append(WorkCandidate("orcid", None, title, year))
            continue
        for doi in dois:
            candidates.append(WorkCandidate("orcid", doi, title, year))
    return candidates


def fetch_openalex_candidates(
    orcid: str,
    mailto: Optional[str],
    timeout: float,
    max_pages: int,
) -> list[WorkCandidate]:
    candidates: list[WorkCandidate] = []
    cursor = "*"
    filter_value = f"authorships.author.orcid:https://orcid.org/{orcid}"
    for _page in range(max_pages):
        params = {
            "filter": filter_value,
            "per_page": "200",
            "sort": "publication_date:desc",
            "cursor": cursor,
        }
        if mailto:
            params["mailto"] = mailto
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        data = http_get_json(url, timeout)
        for work in data.get("results") or []:
            year = work.get("publication_year")
            candidates.append(
                WorkCandidate(
                    "openalex",
                    normalize_doi(work.get("doi")),
                    text_value(work.get("display_name")),
                    str(year) if year else None,
                    openalex_work=work,
                )
            )
        next_cursor = (data.get("meta") or {}).get("next_cursor")
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
    return candidates


def year_from_millis(value: Any) -> Optional[str]:
    try:
        timestamp = int(value) / 1000
    except (TypeError, ValueError):
        return None
    return time.strftime("%Y", time.gmtime(timestamp))


def openreview_year(note: dict[str, Any]) -> Optional[str]:
    for key in ("year", "publication_year"):
        year = openreview_text(note, key)
        if year and re.fullmatch(r"\d{4}", year):
            return year
    venue = openreview_text(note, "venue")
    venueid = openreview_text(note, "venueid")
    for value in (venue, venueid):
        if not value:
            continue
        match = re.search(r"\b(19|20)\d{2}\b", value)
        if match:
            return match.group(0)
    return year_from_millis(note.get("pdate")) or year_from_millis(note.get("cdate"))


def openreview_forum_url(note: dict[str, Any]) -> str:
    forum_id = note.get("forum") or note.get("id")
    return f"https://openreview.net/forum?id={forum_id}"


def openreview_pdf_url(note: dict[str, Any]) -> Optional[str]:
    paperhash = openreview_text(note, "paperhash")
    if paperhash:
        return f"https://openreview.net/pdf?id={paperhash}"
    note_id = text_value(note.get("id"))
    return f"https://openreview.net/pdf?id={note_id}" if note_id else None


def openreview_is_top_level(note: dict[str, Any]) -> bool:
    note_id = note.get("id")
    forum_id = note.get("forum")
    return bool(note_id) and (not forum_id or note_id == forum_id)


def openreview_is_accepted_publication(
    note: dict[str, Any],
    include_imports: bool,
) -> bool:
    if not openreview_is_top_level(note):
        return False

    venue = openreview_text(note, "venue") or ""
    venueid = openreview_text(note, "venueid") or ""
    combined = " ".join(
        text
        for text in (
            venue,
            venueid,
            text_value(note.get("invitation")),
            text_value(note.get("domain")),
        )
        if text
    ).lower()

    if not include_imports and venueid.lower().startswith(
        OPENREVIEW_IMPORTED_VENUE_PREFIXES
    ):
        return False
    if any(term in combined for term in OPENREVIEW_REJECTED_TERMS):
        return False
    return bool(openreview_text(note, "title") and venue)


def fetch_openreview_candidates(
    profile: str,
    timeout: float,
    include_imports: bool,
    limit: int = 100,
) -> list[WorkCandidate]:
    candidates: list[WorkCandidate] = []
    offset = 0
    encoded_profile = urllib.parse.quote(profile, safe="~")
    while True:
        params = {
            "content.authorids": encoded_profile,
            "limit": str(limit),
            "offset": str(offset),
        }
        url = "https://api2.openreview.net/notes?" + urllib.parse.urlencode(
            params,
            safe="~",
        )
        data = http_get_json(url, timeout)
        notes = data.get("notes") or []
        for note in notes:
            if not openreview_is_accepted_publication(note, include_imports):
                continue
            doi = None
            for key in ("doi", "DOI"):
                if doi := normalize_doi(openreview_text(note, key)):
                    break
            candidates.append(
                WorkCandidate(
                    "openreview",
                    doi,
                    openreview_text(note, "title"),
                    openreview_year(note),
                    openreview_note=note,
                )
            )
        if len(notes) < limit:
            break
        offset += limit
    return candidates


def fetch_bibtex_for_doi(doi: str, timeout: float) -> str:
    quoted_doi = urllib.parse.quote(doi, safe="/")
    url = f"https://doi.org/{quoted_doi}"
    text = http_get_text(url, {"Accept": "application/x-bibtex"}, timeout)
    if "@" not in text[:100]:
        raise ValueError(f"DOI did not return BibTeX: {doi}")
    return text.strip() + "\n"


def parse_bibtex_string(source: str, label: str) -> dict[str, Entry]:
    if not source.strip():
        return {}
    source = sanitize_bibtex(source)
    try:
        return dict(bibtex.Parser().parse_string(source).entries)
    except Exception as exc:
        raise ValueError(f"Could not parse BibTeX from {label}: {exc}") from exc


def sanitize_bibtex(source: str) -> str:
    """Normalize small BibTeX variants commonly returned by DOI services."""
    month_pattern = "|".join(MONTH_WORDS)
    return re.sub(
        rf"(?i)(month\s*=\s*)({month_pattern})(\s*[,}}])",
        lambda match: f"{match.group(1)}{{{match.group(2)}}}{match.group(3)}",
        source,
    )


def load_bib_file(path: Path) -> dict[str, Entry]:
    if not path.exists():
        return {}
    return parse_bibtex_string(path.read_text(encoding="utf-8"), str(path))


def bibtex_for_entries(entries: dict[str, Entry]) -> str:
    writer = bibtex_output.Writer()
    return writer.to_string(BibliographyData(entries=entries)).strip() + "\n"


def entry_to_bibtex(key: str, entry: Entry) -> str:
    return bibtex_for_entries({key: entry})


def slug_words(title: Optional[str], max_words: int = 4) -> str:
    normalized = normalize_title(title)
    if not normalized:
        return "work"
    return "-".join(normalized.split()[:max_words]) or "work"


def family_name_from_display_name(name: Optional[str]) -> Optional[str]:
    if not name:
        return None
    parts = re.split(r"\s+", name.strip())
    return parts[-1] if parts else None


def safe_key(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_:-]+", "-", text)
    text = text.strip("-:")
    return text or "work"


def unique_key(base: str, used: set[str]) -> str:
    key = safe_key(base)
    if key not in used:
        used.add(key)
        return key
    counter = 2
    while f"{key}-{counter}" in used:
        counter += 1
    key = f"{key}-{counter}"
    used.add(key)
    return key


def openalex_source_display_name(work: dict[str, Any]) -> Optional[str]:
    for location_key in ("primary_location", "best_oa_location"):
        location = work.get(location_key) or {}
        source = location.get("source") or {}
        name = text_value(source.get("display_name"))
        if name:
            return name
    return None


def synthesize_openalex_entry(work: dict[str, Any], used_keys: set[str]) -> tuple[str, Entry]:
    title = text_value(work.get("display_name")) or "Untitled work"
    year = str(work.get("publication_year") or "")
    work_type = (work.get("type") or "").lower()
    source_name = openalex_source_display_name(work)
    biblio = work.get("biblio") or {}

    authors: list[Person] = []
    for authorship in work.get("authorships") or []:
        author = authorship.get("author") or {}
        name = text_value(author.get("display_name"))
        if name:
            authors.append(Person(name))

    fields = {"title": title}
    if year:
        fields["year"] = year
    doi = normalize_doi(work.get("doi"))
    if doi:
        fields["doi"] = doi
        fields["url"] = f"https://doi.org/{doi}"
    elif work.get("id"):
        fields["url"] = str(work["id"])
    if abstract := openalex_abstract(work):
        fields["abstract"] = abstract

    for field_name, source_field in (
        ("volume", "volume"),
        ("number", "issue"),
        ("pages", "first_page"),
    ):
        value = text_value(biblio.get(source_field))
        if value:
            fields[field_name] = value
    first_page = text_value(biblio.get("first_page"))
    last_page = text_value(biblio.get("last_page"))
    if first_page and last_page and first_page != last_page:
        fields["pages"] = f"{first_page}--{last_page}"

    if "proceedings" in work_type or "conference" in work_type:
        entry_type = "inproceedings"
        if source_name:
            fields["booktitle"] = source_name
    elif "chapter" in work_type:
        entry_type = "incollection"
        if source_name:
            fields["booktitle"] = source_name
    elif "article" in work_type:
        entry_type = "article"
        if source_name:
            fields["journal"] = source_name
    else:
        entry_type = "misc"
        if source_name:
            fields["howpublished"] = source_name

    first_author = None
    if authors:
        if authors[0].last_names:
            first_author = str(authors[0].last_names[-1])
        if not first_author:
            first_author = family_name_from_display_name(str(authors[0]))
    key_base = f"{first_author or 'work'}{year}{slug_words(title, 3)}"
    key = unique_key(key_base, used_keys)
    return key, Entry(entry_type, fields=fields, persons={"author": authors})


def synthesize_openreview_entry(note: dict[str, Any], used_keys: set[str]) -> tuple[str, Entry]:
    title = openreview_text(note, "title") or "Untitled work"
    venue = openreview_text(note, "venue") or "OpenReview"
    year = openreview_year(note) or ""
    authors = [Person(name) for name in openreview_list(note, "authors")]

    fields = {
        "title": title,
        "booktitle": venue,
        "url": openreview_forum_url(note),
    }
    if year:
        fields["year"] = year
    if pdf_url := openreview_pdf_url(note):
        fields["eprint"] = pdf_url
    if venueid := openreview_text(note, "venueid"):
        fields["organization"] = venueid
    if abstract := openreview_text(note, "abstract"):
        fields["abstract"] = abstract
    for key in ("doi", "DOI"):
        if doi := normalize_doi(openreview_text(note, key)):
            fields["doi"] = doi
            break

    first_author = None
    if authors:
        if authors[0].last_names:
            first_author = str(authors[0].last_names[-1])
        if not first_author:
            first_author = family_name_from_display_name(str(authors[0]))
    key_base = f"{first_author or 'openreview'}{year}{slug_words(title, 3)}"
    key = unique_key(key_base, used_keys)
    return key, Entry("inproceedings", fields=fields, persons={"author": authors})


def sort_entries(entries: dict[str, Entry]) -> dict[str, Entry]:
    def sort_key(item: tuple[str, Entry]) -> tuple[int, str, str]:
        key, entry = item
        year_text = entry.fields.get("year") or "0"
        match = re.search(r"\d{4}", year_text)
        year = int(match.group(0)) if match else 0
        return (-year, normalize_title(entry.fields.get("title")) or "", key.lower())

    return dict(sorted(entries.items(), key=sort_key))


def attach_preprints_to_publications(entries: dict[str, Entry]) -> dict[str, Entry]:
    publications: dict[str, Entry] = {}
    publications_by_title: dict[str, Entry] = {}
    preprints: list[Entry] = []

    for key, entry in entries.items():
        if entry_is_preprint(entry):
            preprints.append(entry)
            continue
        publications[key] = entry
        if title := normalize_title(entry.fields.get("title")):
            publications_by_title[title] = entry

    for preprint in preprints:
        title = normalize_title(preprint.fields.get("title"))
        if not title:
            continue
        publication = publications_by_title.get(title)
        if not publication:
            continue
        if preprint_url := preprint_url_for_entry(preprint):
            publication.fields.setdefault("preprinturl", preprint_url)
        if preprint_abstract := preprint.fields.get("abstract"):
            publication.fields.setdefault("abstract", preprint_abstract)

    return publications


def generated_identity_updates(
    entry: Entry,
    candidate_id_values: set[tuple[str, str]],
) -> set[tuple[str, str]]:
    identities = set(entry_identities(entry))
    identities.update(candidate_id_values)
    if entry_is_preprint(entry):
        return {identity for identity in identities if identity[0] == "doi"}
    return identities


def identity_index(entries: Iterable[Entry]) -> set[tuple[str, str]]:
    identities: set[tuple[str, str]] = set()
    for entry in entries:
        identities.update(entry_identities(entry))
    return identities


def dedupe_candidates(candidates: Iterable[WorkCandidate]) -> list[WorkCandidate]:
    by_identity: dict[tuple[str, str], WorkCandidate] = {}
    for candidate in candidates:
        identity = candidate_identity(candidate)
        if not identity:
            continue
        existing = by_identity.get(identity)
        if not existing:
            by_identity[identity] = candidate
            continue
        if (
            (candidate.openalex_work and not existing.openalex_work)
            or (candidate.openreview_note and not existing.openreview_note)
        ):
            by_identity[identity] = WorkCandidate(
                source=f"{existing.source}+{candidate.source}",
                doi=existing.doi or candidate.doi,
                title=existing.title or candidate.title,
                year=existing.year or candidate.year,
                openalex_work=existing.openalex_work or candidate.openalex_work,
                openreview_note=existing.openreview_note or candidate.openreview_note,
            )
    return list(by_identity.values())


def filter_openalex_candidates(
    openalex_candidates: Iterable[WorkCandidate],
    orcid_candidates: Iterable[WorkCandidate],
    include_openalex_only: bool,
) -> list[WorkCandidate]:
    if include_openalex_only:
        return list(openalex_candidates)

    orcid_dois = {
        candidate.doi for candidate in orcid_candidates if candidate.doi is not None
    }
    orcid_titles = {
        normalized
        for candidate in orcid_candidates
        if (normalized := normalize_title(candidate.title))
    }

    filtered = []
    for candidate in openalex_candidates:
        title = normalize_title(candidate.title)
        if candidate.doi in orcid_dois or (title and title in orcid_titles):
            filtered.append(candidate)
    return filtered


def build_generated_entries(
    candidates: Iterable[WorkCandidate],
    timeout: float,
    sleep_seconds: float,
    verbose: bool,
    stats: RunStats,
) -> dict[str, Entry]:
    generated: dict[str, Entry] = {}
    generated_identities: set[tuple[str, str]] = set()
    used_keys: set[str] = set()

    for candidate in candidates:
        identities = candidate_identities(candidate)
        if not identities or not identities.isdisjoint(generated_identities):
            continue

        if candidate.doi:
            try:
                bib_text = fetch_bibtex_for_doi(candidate.doi, timeout)
                fetched = parse_bibtex_string(bib_text, candidate.doi)
                if not fetched:
                    raise ValueError("empty BibTeX response")
                raw_key, entry = next(iter(fetched.items()))
                entry.fields.setdefault("doi", candidate.doi)
                entry.fields.setdefault("url", f"https://doi.org/{candidate.doi}")
                enrich_entry_from_candidate(entry, candidate)
                key = unique_key(raw_key, used_keys)
                generated[key] = entry
                generated_identities.update(generated_identity_updates(entry, identities))
                stats.doi_fetches += 1
                time.sleep(sleep_seconds)
                continue
            except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as exc:
                stats.doi_failures += 1
                if verbose:
                    print(f"warning: DOI BibTeX fetch failed for {candidate.doi}: {exc}")

        if candidate.openalex_work:
            key, entry = synthesize_openalex_entry(candidate.openalex_work, used_keys)
            generated[key] = entry
            generated_identities.update(generated_identity_updates(entry, identities))
            stats.synthesized += 1
        elif candidate.openreview_note:
            key, entry = synthesize_openreview_entry(candidate.openreview_note, used_keys)
            generated[key] = entry
            generated_identities.update(generated_identity_updates(entry, identities))
            stats.synthesized += 1
        elif verbose:
            label = candidate.title or candidate.doi or "untitled work"
            print(f"warning: skipping work without DOI or source metadata: {label}")

    generated = attach_preprints_to_publications(generated)
    stats.generated_entries = len(generated)
    return generated


def append_entries(output_path: Path, entries: dict[str, Entry], dry_run: bool) -> None:
    if dry_run or not entries:
        return
    existing = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    separator = "\n" if existing.endswith("\n") or not existing else "\n\n"
    block = "% Automatically appended by scripts/update_publications_bib.py\n\n"
    block += "\n".join(entry_to_bibtex(key, entry).strip() for key, entry in entries.items())
    output_path.write_text(existing + separator + block + "\n", encoding="utf-8")


def rewrite_output(
    output_path: Path,
    existing: dict[str, Entry],
    manual: dict[str, Entry],
    generated: dict[str, Entry],
    dry_run: bool,
) -> None:
    if dry_run:
        return
    merged: dict[str, Entry] = {}
    used_keys: set[str] = set()
    for source in (generated, existing, manual):
        for key, entry in source.items():
            identities = entry_identities(entry)
            if identities:
                for current_key, current_entry in list(merged.items()):
                    if not identities.isdisjoint(entry_identities(current_entry)):
                        del merged[current_key]
                        used_keys.discard(current_key)
                        break
            merged[unique_key(key, used_keys)] = entry
    output_path.write_text(bibtex_for_entries(sort_entries(merged)), encoding="utf-8")


def write_generated_snapshot(
    path: Path,
    generated: dict[str, Entry],
    dry_run: bool,
) -> None:
    if dry_run:
        return
    header = (
        "% Generated by scripts/update_publications_bib.py; "
        "edit pubs.bib or manual_pubs.bib instead.\n\n"
    )
    path.write_text(header + bibtex_for_entries(sort_entries(generated)), encoding="utf-8")


def main() -> int:
    args = parse_args()
    stats = RunStats()

    orcid = normalize_orcid(args.orcid) or normalize_orcid(
        read_config_scalar(args.config, "orcid")
    )
    if not orcid:
        print("error: no ORCID iD found. Pass --orcid or set author.orcid in _config.yml.")
        return 2

    mailto = os.environ.get("OPENALEX_EMAIL") or read_config_scalar(args.config, "email")

    print(f"Fetching publication metadata for ORCID {orcid}")
    orcid_candidates = fetch_orcid_candidates(orcid, args.timeout)
    candidates = list(orcid_candidates)
    stats.orcid_candidates = len(orcid_candidates)
    if not args.no_openalex:
        all_openalex_candidates = fetch_openalex_candidates(
            orcid,
            mailto,
            args.timeout,
            args.max_openalex_pages,
        )
        openalex_candidates = filter_openalex_candidates(
            all_openalex_candidates,
            orcid_candidates,
            args.include_openalex_only,
        )
        stats.openalex_candidates = len(openalex_candidates)
        candidates.extend(openalex_candidates)
    openreview_profile = normalize_openreview_profile(args.openreview_profile)
    if openreview_profile and not args.no_openreview:
        openreview_candidates = fetch_openreview_candidates(
            openreview_profile,
            args.timeout,
            args.include_openreview_imports,
        )
        stats.openreview_candidates = len(openreview_candidates)
        candidates.extend(openreview_candidates)

    candidates = dedupe_candidates(candidates)
    if not candidates:
        print("error: no publication candidates found from ORCID/OpenAlex.")
        return 1

    generated = build_generated_entries(
        candidates,
        timeout=args.timeout,
        sleep_seconds=args.sleep,
        verbose=args.verbose,
        stats=stats,
    )
    if not generated:
        print("error: no BibTeX entries could be generated.")
        return 1

    existing_entries = load_bib_file(args.output_bib)
    manual_entries = load_bib_file(args.manual_bib) if args.manual_bib.exists() else {}
    stats.existing_entries = len(existing_entries)
    existing_publications = [
        entry for entry in existing_entries.values() if not entry_is_preprint(entry)
    ]
    manual_publications = [
        entry for entry in manual_entries.values() if not entry_is_preprint(entry)
    ]
    existing_identities = identity_index(existing_publications)
    existing_identities.update(identity_index(manual_publications))

    new_entries = {
        key: entry
        for key, entry in sort_entries(generated).items()
        if not entry_is_preprint(entry)
        and (identities := entry_identities(entry))
        and identities.isdisjoint(existing_identities)
    }
    stats.new_entries = len(new_entries)

    if not args.no_generated_bib:
        write_generated_snapshot(args.generated_bib, generated, args.dry_run)

    if args.rewrite_output:
        rewrite_output(
            args.output_bib,
            existing_entries,
            manual_entries,
            generated,
            args.dry_run,
        )
    else:
        append_entries(args.output_bib, new_entries, args.dry_run)

    print(
        "Summary: "
        f"{stats.orcid_candidates} ORCID candidates, "
        f"{stats.openalex_candidates} OpenAlex candidates, "
        f"{stats.openreview_candidates} OpenReview candidates, "
        f"{stats.doi_fetches} DOI BibTeX records, "
        f"{stats.synthesized} synthesized records, "
        f"{stats.doi_failures} DOI failures, "
        f"{stats.generated_entries} generated entries, "
        f"{stats.existing_entries} existing entries, "
        f"{stats.new_entries} new entries."
    )
    if args.dry_run:
        print("Dry run only; no files were written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
