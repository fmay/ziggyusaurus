---
title: AI Search Overview
description: Discover Ziggy's AI-powered search capabilities. Make any data searchable using natural language queries across all your systems and databases.
keywords: [ziggy ai search, natural language search, data search, ai powered search, search platform]
image: /img/ziggy-logo-light-bg.webp
---

Ziggy helps you make your data searchable using natural language queries, no matter where it is stored.

## Front Ends
You have various options for querying.

### ChatterBox
[ChatterBox](/search/search-chatterbox.md) is Ziggy's own, fully customizable front end.

<iframe 
  src="https://nxucrsk2vrk61vtm.public.blob.vercel-storage.com/website-videos/chatterbox-overview-bL8l1IooBSo2zJYEgOD6hC7zSYUnpJ.mp4" 
  width="100%" 
  height="400" 
  allow="fullscreen; picture-in-picture" 
  allowfullscreen>
</iframe>


### Slack 
You can also enter natural language queries in [Slack](search-slack.md) and get data back in any format you need.  

<iframe 
  src="https://nxucrsk2vrk61vtm.public.blob.vercel-storage.com/website-videos/slack-overview-UAw2NUTAo8NJHOiblOdEvfh8sSPyBT.mp4" 
  width="100%" 
  height="400" 
  allow="fullscreen; picture-in-picture" 
  allowfullscreen>
</iframe>

### Your own front end
All Ziggy Flows can be invoked using simple API calls, so you can perform searches using any application. All data is returned in standardised formats for listings, tables and crosstabs.

## Search Flows
If your data is already in a database, data warehouse, Elastic ERP/CRM platform etc., then you use a Ziggy Flow to directly query the data.

Please refer to [Search Flows](search-prompt-flows.md).

## Transformed Data
In some cases, while you have direct access to the data, the data is not searchable in the way you want it for very flexible search. Typical examples of this are

- **Fuzzy search** : some databases and platforms do not allow flexible fuzzy searching or require unnecessarily complex index configurations.
- **Semantic search** : if you want to perform semantic search (general meaning, intent, contextually aware) then you will need to handle this using LLM *embeddings*.

In both cases, Ziggy can handle this for you very efficiently by creating a streamlined data store with everything you need for these types of searches.

Initially, you can bulk load this data. Thereafter, you can incrementally load data when systems performs record level changes. This is all managed by [ingestion flows](search-loading-flows).

## Parameter object
A search

