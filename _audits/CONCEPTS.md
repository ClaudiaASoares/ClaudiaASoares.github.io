# Concepts used in the SEO audit

These terms were checked against the live website and the documentation linked below on 13 October 2026. Use these names in the audit and any implementation notes. A crawl result establishes the response observed during the audit. It does not establish a search engine's indexing decision.

| Concept | Definition and usage |
| --- | --- |
| SEO | Search engine optimisation. Changes intended to help search engines discover and understand pages and help readers choose relevant search results. |
| Crawling | A crawler requesting a URL and reading its response. |
| Indexing | A search engine processing content for inclusion in its search index. A successful HTTP response does not prove indexing. |
| Canonical URL | The preferred URL for a page or a set of duplicate pages. A canonical link communicates a preference to a search engine. |
| XML sitemap | A machine-readable list of URLs supplied for discovery. Inclusion does not guarantee indexing. |
| Internal link | An HTML link to another URL on the same website. |
| HTTP 404 | The HTTP response status indicating that the requested resource was not found. |
| Meta description | The HTML head element `<meta name="description" content="…">`. An Open Graph description and a Schema.org `itemprop="description"` are separate elements. |
| Page title | The text in the HTML `<title>` element. |
| Title link | The title displayed for a search result. A search engine may generate it from several sources. |
| H1 | An HTML heading at level one. This audit recommends one page heading, followed by section headings at lower levels, for clarity. |
| Structured data | Machine-readable statements about the entities and content represented on a page, using a defined vocabulary. |
| JSON-LD | The JSON representation used to express linked structured data. Valid JSON syntax does not establish eligibility for a search feature. |
| Person | The Schema.org type representing an individual. |
| ProfilePage | The Schema.org type representing a page whose primary subject is a person or organisation affiliated with the website. |
| Citation metadata | Bibliographic HTML meta tags, including `citation_title`, one `citation_author` tag per author, and `citation_publication_date`. |
| Google Scholar indexing | Inclusion of scholarly content in Google Scholar. Its content and bibliographic requirements differ from ordinary web search. |
| Open Graph metadata | HTML properties used to describe a page when it is shared, including `og:title`, `og:type`, `og:image`, and `og:url`. |
| Lab measurement | A measurement from a controlled test, such as an emulated device running Lighthouse. |
| Field measurement | A measurement collected from visits by users. |
| Core Web Vitals | The field metrics Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift. |
| Largest Contentful Paint (LCP) | The elapsed time until the largest visible image or text block is rendered. |
| First Contentful Paint (FCP) | The elapsed time until the first text or image content is rendered. |
| Total Blocking Time (TBT) | A lab measurement of main-thread blocking after FCP. It is not a field measurement of Interaction to Next Paint. |
| Cumulative Layout Shift (CLS) | A measurement of unexpected movement of visible page content. |
| TrustworthyML@NOVA | The group name used in the live website's navigation. Use this spelling when proposing page titles. |
| Trustworthy machine learning | The research topic named in the website's introduction. Use the full term in proposed search metadata. Preserve the mechanisms and claims stated in the source content. |

Definitions are bounded by [Google's search documentation](https://developers.google.com/search/docs/fundamentals/how-search-works), [title link guidance](https://developers.google.com/search/docs/appearance/title-link), [meta description guidance](https://developers.google.com/search/docs/appearance/snippet), [ProfilePage guidance](https://developers.google.com/search/docs/appearance/structured-data/profile-page), [Google Scholar inclusion guidelines](https://scholar.google.com/intl/en/scholar/inclusion.html), the [Open Graph protocol](https://ogp.me/), and [Web Vitals documentation](https://web.dev/articles/vitals). Group and research names come from the [live website](https://claudiaasoares.github.io/).
