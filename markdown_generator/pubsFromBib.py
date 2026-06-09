#!/usr/bin/env python
# coding: utf-8

"""Convert BibTeX publications into AcademicPages Markdown files.

Run this script from the `markdown_generator` directory:

    python pubsFromBib.py

It reads `pubs.bib` and writes one Markdown file per usable publication into
`../_publications`. Duplicate BibTeX records are collapsed by DOI and title,
with missing metadata merged into the selected record. Preprint entries are not
rendered as standalone pages; when their title matches a published entry, their
URL is linked from the published page instead.
"""

from __future__ import annotations

import html
import os
import re
import unicodedata
from time import strptime
from typing import Optional

from pybtex.database import BibliographyData, Entry, Person
from pybtex.database.input import bibtex
from pybtex.database.output import bibtex as bibtex_output


_HERE = os.path.dirname(os.path.abspath(__file__))

PUBS_FILE = os.path.join(_HERE, "pubs.bib")
OUTPUT_DIR = os.path.join(_HERE, "../_publications")
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

ABSTRACT_FIELDS = (
    "abstract",
    "description",
    "summary",
)

PREPRINT_TERMS = (
    "arxiv",
    "corr",
    "biorxiv",
    "medrxiv",
    "ssrn",
    "preprint",
)

# Map LaTeX accent commands (single-char) to Unicode combining diacritical marks.
_LATEX_COMBINING: dict[str, str] = {
    "'": "\u0301",  # acute
    "`": "\u0300",  # grave
    '"': "\u0308",  # diaeresis / umlaut
    "^": "\u0302",  # circumflex
    "~": "\u0303",  # tilde
    "=": "\u0304",  # macron
    ".": "\u0307",  # dot above
    "u": "\u0306",  # breve
    "v": "\u030C",  # caron
    "H": "\u030B",  # double acute
    "r": "\u030A",  # ring above
    "c": "\u0327",  # cedilla
    "k": "\u0328",  # ogonek
    "d": "\u0323",  # dot below
    "b": "\u0332",  # macron below
}

# Special LaTeX letter commands that map to a single Unicode character.
_LATEX_SPECIALS: dict[str, str] = {
    "ss": "\u00DF",  # ß
    "ae": "\u00E6",  # æ
    "oe": "\u0153",  # œ
    "aa": "\u00E5",  # å
    "AE": "\u00C6",  # Æ
    "OE": "\u0152",  # Œ
    "AA": "\u00C5",  # Å
    "o": "\u00F8",   # ø
    "O": "\u00D8",   # Ø
    "l": "\u0142",   # ł
    "L": "\u0141",   # Ł
}


def _decode_latex_accents(text: str) -> str:
    """Convert LaTeX accent/special-letter commands to their Unicode equivalents.

    Handles both braced forms (e.g. ``\\'{a}`` → á) and unbraced forms
    (e.g. ``\\'a`` → á), as well as special symbols like ``\\ss`` → ß.
    """

    def _replace(m: re.Match) -> str:  # type: ignore[type-arg]
        cmd, char = m.group(1), m.group(2)
        combining = _LATEX_COMBINING.get(cmd)
        if combining:
            return unicodedata.normalize("NFC", char + combining)
        return char

    _cls = "[" + "".join(_LATEX_COMBINING) + "]"
    # \cmd{letter} — e.g. \'{a}, \"{o}, \c{c}
    text = re.sub(r"\\(" + _cls + r")\{([a-zA-Z])\}", _replace, text)
    # \cmd letter  — e.g. \'a, \"o (without braces)
    text = re.sub(r"\\(" + _cls + r")([a-zA-Z])", _replace, text)
    # \special — e.g. \ss, \ae, \o
    specials_pattern = "|".join(re.escape(k) for k in _LATEX_SPECIALS)
    text = re.sub(
        rf"\\({specials_pattern})(?=[^a-zA-Z]|$)",
        lambda m: _LATEX_SPECIALS.get(m.group(1), m.group(1)),
        text,
    )
    return text


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
    cleaned = _decode_latex_accents(str(text))
    cleaned = cleaned.replace("{", "").replace("}", "")
    cleaned = cleaned.replace("\\", "").replace("\n", " ").replace("\r", " ")
    return re.sub(r"\s+", " ", cleaned).strip()


def normalize_title(text: Optional[str]) -> Optional[str]:
    title = clean_bibtex_text(text).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title or None


def normalize_doi(text: Optional[str]) -> Optional[str]:
    doi = clean_bibtex_text(text).lower()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    doi = doi.strip().strip("<>")
    doi = re.sub(r"[\s.,;)\]]+$", "", doi)
    if not doi.startswith("10."):
        return None
    return doi


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


def abstract_for_entry(fields: dict[str, str]) -> str:
    for field in ABSTRACT_FIELDS:
        abstract = clean_bibtex_text(fields.get(field))
        if abstract:
            return abstract
    return ""


def excerpt_for_abstract(abstract: str, max_words: int = 65) -> str:
    words = abstract.split()
    if len(words) <= max_words:
        return abstract
    return " ".join(words[:max_words]).rstrip(".,;:") + "."


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


def arxiv_pdf_url(value: str) -> Optional[str]:
    value = clean_bibtex_text(value)
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
    fields = entry.fields
    for field in ("preprintpdfurl", "preprinturl", "url", "doi", "eprint"):
        value = clean_bibtex_text(fields.get(field))
        if not value:
            continue
        if pdf_url := arxiv_pdf_url(value):
            return pdf_url
        if field in {"preprintpdfurl", "preprinturl", "url"}:
            return value
    return None


def is_preprint_entry(entry: Entry) -> bool:
    fields = entry.fields
    doi = clean_bibtex_text(fields.get("doi")).lower()
    if doi.startswith("10.48550/arxiv"):
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
        value = clean_bibtex_text(fields.get(field)).lower()
        if any(term in value for term in PREPRINT_TERMS):
            return True
    return False


def entry_identities(entry: Entry) -> set[tuple[str, str]]:
    identities: set[tuple[str, str]] = set()
    if doi := normalize_doi(entry.fields.get("doi")):
        identities.add(("doi", doi))
    if title := normalize_title(entry.fields.get("title")):
        identities.add(("title", title))
    return identities


def entry_quality_score(entry: Entry) -> int:
    fields = entry.fields
    score = 0
    if normalize_doi(fields.get("doi")):
        score += 30
    if url_for_entry(fields):
        score += 8
    if abstract_for_entry(fields):
        score += 8
    if clean_bibtex_text(fields.get("month")):
        score += 10
    if clean_bibtex_text(fields.get("day")):
        score += 3
    for field in ("pages", "volume", "number"):
        if clean_bibtex_text(fields.get(field)):
            score += 3
    for field in ("publisher", "issn", "isbn", "keywords"):
        if clean_bibtex_text(fields.get(field)):
            score += 1
    return score


def clone_entry(entry: Entry) -> Entry:
    return Entry(
        entry.type,
        fields=dict(entry.fields),
        persons={role: list(people) for role, people in entry.persons.items()},
    )


def merge_missing_metadata(target: Entry, source: Entry) -> None:
    for field, value in source.fields.items():
        if field not in target.fields or not clean_bibtex_text(target.fields.get(field)):
            target.fields[field] = value
    for role, people in source.persons.items():
        if role not in target.persons or not target.persons[role]:
            target.persons[role] = list(people)


def duplicate_groups(
    entries: list[tuple[str, Entry]],
) -> list[list[tuple[str, Entry]]]:
    parent = {key: key for key, _entry in entries}
    by_identity: dict[tuple[str, str], str] = {}

    def find(key: str) -> str:
        while parent[key] != key:
            parent[key] = parent[parent[key]]
            key = parent[key]
        return key

    def union(left: str, right: str) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for key, entry in entries:
        for identity in entry_identities(entry):
            if identity in by_identity:
                union(by_identity[identity], key)
            else:
                by_identity[identity] = key

    grouped: dict[str, list[tuple[str, Entry]]] = {}
    for key, entry in entries:
        grouped.setdefault(find(key), []).append((key, entry))
    return list(grouped.values())


def dedupe_publication_entries(
    entries: list[tuple[str, Entry]],
) -> list[tuple[str, Entry, list[str]]]:
    deduped: list[tuple[str, Entry, list[str]]] = []
    for group in duplicate_groups(entries):
        best_key, best_entry = group[0]
        best_score = entry_quality_score(best_entry)
        for key, entry in group[1:]:
            score = entry_quality_score(entry)
            if score > best_score:
                best_key, best_entry, best_score = key, entry, score

        merged = clone_entry(best_entry)
        for key, entry in group:
            if key != best_key:
                merge_missing_metadata(merged, entry)

        duplicate_keys = [key for key, _entry in group if key != best_key]
        deduped.append((best_key, merged, duplicate_keys))
    return deduped


def bibtex_for_entry(key: str, entry: Entry) -> str:
    writer = bibtex_output.Writer()
    data = BibliographyData(entries={key: entry})
    return writer.to_string(data).strip()


def slug_for_title(title: str) -> str:
    clean_title = title.replace(" ", "-")
    url_slug = re.sub(r"\[.*\]|[^a-zA-Z0-9_-]", "", clean_title)
    return re.sub(r"-+", "-", url_slug).strip("-") or "publication"


def preferred_existing_filename(
    normalized_title: Optional[str],
    default_filename: str,
    existing_files: Optional[dict[str, list[str]]],
) -> str:
    if not normalized_title or not existing_files:
        return default_filename
    candidates = existing_files.get(normalized_title, [])
    if default_filename in candidates:
        return default_filename
    for candidate in candidates:
        if candidate.casefold() == default_filename.casefold():
            return candidate
    default_date = default_filename[:10]
    for candidate in candidates:
        if candidate.startswith(default_date):
            return candidate
    return default_filename


def markdown_for_entry(
    bib_id: str,
    entry: Entry,
    preprint_entry: Optional[Entry] = None,
    existing_files: Optional[dict[str, list[str]]] = None,
) -> Optional[tuple[str, str]]:
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
    md_filename = preferred_existing_filename(
        normalize_title(title),
        md_filename,
        existing_files,
    )
    html_filename = os.path.splitext(md_filename)[0]
    paper_url = url_for_entry(fields)
    abstract = abstract_for_entry(fields)
    if preprint_entry and not abstract:
        abstract = abstract_for_entry(preprint_entry.fields)
    excerpt = excerpt_for_abstract(abstract) if abstract else ""
    preprint_url = preprint_url_for_entry(preprint_entry) if preprint_entry else None

    citation = (
        f'{authors_text(entry)}, "{html_escape(title)}." '
        f"{html_escape(venue)}, {pub_year}."
    )

    md = f'---\ntitle: "{html_escape(title)}"\n'
    md += f"collection: {COLLECTION_NAME}"
    md += f"\npermalink: {PERMALINK_PREFIX}{html_filename}"
    if excerpt:
        md += f"\nexcerpt: '{html_escape(excerpt)}'"
    md += f"\ndate: {pub_date}"
    md += f"\nvenue: '{html_escape(venue)}'"
    if paper_url:
        md += f"\npaperurl: '{paper_url}'"
    if preprint_url:
        md += f"\npreprinturl: '{preprint_url}'"
    md += f"\ncitation: '{citation}'"
    md += "\n---"

    if abstract:
        md += f"\n\n{html_escape(abstract)}\n"

    if preprint_url:
        md += f'\n[Download paper here]({preprint_url}){{:target="_blank"}}\n'
    elif paper_url:
        md += f'\n[Access paper here]({paper_url}){{:target="_blank"}}\n'

    md += "\nBibtex:\n\n"
    md += "<pre><code>"
    md += html.escape(bibtex_for_entry(bib_id, entry))
    md += "</code></pre>\n"

    return md_filename, md


def markdown_title(path: str) -> Optional[str]:
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read()
    except OSError:
        return None
    match = re.search(r'^\s*title:\s*["\']?(.*?)["\']?\s*$', text, re.MULTILINE)
    if not match:
        return None
    return clean_bibtex_text(match.group(1))


def existing_markdown_files_by_title() -> dict[str, list[str]]:
    existing: dict[str, list[str]] = {}
    for filename in os.listdir(OUTPUT_DIR):
        if not filename.endswith(".md"):
            continue
        path = os.path.join(OUTPUT_DIR, filename)
        title = normalize_title(markdown_title(path))
        if title:
            existing.setdefault(title, []).append(filename)
    return existing


def remove_stale_duplicate_pages(
    desired_files: set[str],
    rendered_titles: set[str],
) -> int:
    removed = 0
    for filename in os.listdir(OUTPUT_DIR):
        if not filename.endswith(".md") or filename in desired_files:
            continue
        path = os.path.join(OUTPUT_DIR, filename)
        title = normalize_title(markdown_title(path))
        if not title or title not in rendered_titles:
            continue
        os.remove(path)
        removed += 1
        print(f"REMOVED STALE DUPLICATE {filename}")
    return removed


def main() -> int:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(PUBS_FILE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    preprints_by_title: dict[str, Entry] = {}
    publication_entries: list[tuple[str, Entry]] = []
    for bib_id, entry in bibdata.entries.items():
        normalized_title = normalize_title(entry.fields.get("title"))
        if not normalized_title:
            continue
        if is_preprint_entry(entry):
            preprints_by_title.setdefault(normalized_title, entry)
        else:
            publication_entries.append((bib_id, entry))

    deduped_entries = dedupe_publication_entries(publication_entries)
    published_titles = {
        normalized_title
        for _bib_id, entry, _duplicate_keys in deduped_entries
        if (normalized_title := normalize_title(entry.fields.get("title")))
    }
    existing_files = existing_markdown_files_by_title()

    written = 0
    skipped = 0
    skipped_preprints = 0
    deduped = 0
    desired_files: set[str] = set()
    rendered_titles: set[str] = set()
    for bib_id, entry in bibdata.entries.items():
        normalized_title = normalize_title(entry.fields.get("title"))
        if is_preprint_entry(entry):
            title = clean_bibtex_text(entry.fields.get("title")) or bib_id
            if normalized_title in published_titles:
                print(f'INFO Linking preprint through published entry: "{title}"')
            else:
                print(f'INFO Skipping standalone preprint: "{title}"')
            skipped_preprints += 1
            continue

    for bib_id, entry, duplicate_keys in deduped_entries:
        normalized_title = normalize_title(entry.fields.get("title"))
        preprint_entry = preprints_by_title.get(normalized_title) if normalized_title else None
        rendered = markdown_for_entry(bib_id, entry, preprint_entry, existing_files)
        if not rendered:
            title = clean_bibtex_text(entry.fields.get("title")) or bib_id
            print(f'WARNING Skipping entry with missing title or year: "{title}"')
            skipped += 1
            continue

        md_filename, md = rendered
        with open(os.path.join(OUTPUT_DIR, md_filename), "w", encoding="utf-8") as file:
            file.write(md)
        desired_files.add(md_filename)
        if normalized_title:
            rendered_titles.add(normalized_title)
        short_title = clean_bibtex_text(entry.fields.get("title"))[:60]
        if duplicate_keys:
            print(
                f"INFO Deduplicated {bib_id}: skipped duplicate BibTeX keys "
                f"{', '.join(duplicate_keys)}"
            )
            deduped += len(duplicate_keys)
        print(f'SUCCESSFULLY PARSED {bib_id}: "{short_title}"')
        written += 1

    removed_stale = remove_stale_duplicate_pages(desired_files, rendered_titles)

    print(
        "Finished publication generation: "
        f"{written} written, {skipped} skipped, "
        f"{skipped_preprints} preprints skipped or linked, "
        f"{deduped} duplicate BibTeX records collapsed, "
        f"{removed_stale} stale duplicate pages removed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
