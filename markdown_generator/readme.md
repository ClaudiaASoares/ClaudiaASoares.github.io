# Jupyter notebook markdown generator

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process. The .py files are pure python that do the same things if they are executed in a terminal, they just don't have pretty documentation.

## Updating publications from open metadata

The site uses `pubs.bib` as the source for generated publication pages. To fetch candidate publications from ORCID, OpenAlex, OpenReview, and DOI metadata providers, run this from the repository root:

```bash
python scripts/update_publications_bib.py
```

By default, the updater reads the ORCID iD from `_config.yml`, scans the OpenReview profile `~Claudia_Soares1` for accepted public venue records, writes a generated metadata snapshot to `generated_pubs.bib`, and appends only missing records to `pubs.bib`. Existing hand-curated BibTeX entries are preserved to avoid large formatting-only diffs.

Then regenerate the publication pages:

```bash
cd markdown_generator
python pubsFromBib.py
```

The GitHub Actions workflow in `.github/workflows/update-publications.yml` runs the same process weekly and opens a pull request when generated files change.


