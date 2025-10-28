# README

## Algolia Indexing

### Editor
The editor configuration should look like this (specifically the `recordExtractor`) to extract the headers etc for indexing.

```javascript
new Crawler({
  appId: "XPMSD22TBN",
  indexPrefix: "",
  rateLimit: 8,
  startUrls: ["https://docs.ziggyservices.com"],
  renderJavaScript: false,
  maxDepth: 10,
  maxUrls: 300,
  sitemaps: ["https://docs.ziggyservices.com/sitemap.xml"],
  schedule: "on the 30 day of the month",
  ignoreCanonicalTo: false,
  discoveryPatterns: ["https://docs.ziggyservices.com/**"],
  actions: [
    {
      indexName: "Ziggy Docs",
      pathsToMatch: ["https://docs.ziggyservices.com/**"],
      recordExtractor: ({ $, helpers }) => {
        // Extract the section from breadcrumbs or sidebar
        const breadcrumbs = $(".breadcrumbs__item .breadcrumbs__link");
        let lvl0 = "Documentation"; // default fallback

        // Try to get the section from breadcrumbs (second item is usually the section)
        if (breadcrumbs.length > 1) {
          lvl0 = $(breadcrumbs[1]).text().trim();
        }

        return helpers.docsearch({
          recordProps: {
            lvl0: {
              selectors: ".breadcrumbs__item:nth-child(2) .breadcrumbs__link",
              defaultValue: "Documentation",
            },
            lvl1: ".theme-doc-markdown h1, .theme-doc-markdown header h1",
            lvl2: ".theme-doc-markdown h2",
            lvl3: ".theme-doc-markdown h3",
            lvl4: ".theme-doc-markdown h4",
            lvl5: ".theme-doc-markdown h5",
            lvl6: ".theme-doc-markdown h6",
            content:
              ".theme-doc-markdown p, .theme-doc-markdown li, .theme-doc-markdown td",
          },
          indexHeadings: true,
          aggregateContent: true,
        });
      },
    },
  ],
  safetyChecks: { beforeIndexPublishing: { maxLostRecordsPercentage: 30 } },
  initialIndexSettings: {
    "Ziggy Docs": {
      attributesForFaceting: ["type", "lang"],
      attributesToRetrieve: [
        "hierarchy",
        "content",
        "anchor",
        "url",
        "url_without_anchor",
        "type",
      ],
      attributesToHighlight: ["hierarchy", "content"],
      attributesToSnippet: ["content:10"],
      camelCaseAttributes: ["hierarchy", "content"],
      searchableAttributes: [
        "unordered(hierarchy.lvl0)",
        "unordered(hierarchy.lvl1)",
        "unordered(hierarchy.lvl2)",
        "unordered(hierarchy.lvl3)",
        "unordered(hierarchy.lvl4)",
        "unordered(hierarchy.lvl5)",
        "unordered(hierarchy.lvl6)",
        "content",
      ],
      distinct: true,
      attributeForDistinct: "url",
      customRanking: [
        "desc(weight.pageRank)",
        "desc(weight.level)",
        "asc(weight.position)",
      ],
      ranking: [
        "words",
        "filters",
        "typo",
        "attribute",
        "proximity",
        "exact",
        "custom",
      ],
      highlightPreTag: '<span class="algolia-docsearch-suggestion--highlight">',
      highlightPostTag: "</span>",
      minWordSizefor1Typo: 3,
      minWordSizefor2Typos: 7,
      allowTyposOnNumericTokens: false,
      minProximity: 1,
      ignorePlurals: true,
      advancedSyntax: true,
      attributeCriteriaComputedByMinProximity: true,
      removeWordsIfNoResults: "allOptional",
    },
  },
  apiKey: "d306c3a1645bb47380811310974fed3b",
});
```