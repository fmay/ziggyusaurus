---
title: Overview
---

Ziggy helps you make your data searchable using natural language queires, no matter where it is stored. 

## Search Flows
If your data is already in a database, data warehouse, Elastic ERP/CRM platform etc., then you use a Ziggy Flow to directly query the data.

Please refer to [Search Flows](search-prompt-flows.md).

## Transformed Data
In some cases, while you have direct access to the data, the data is not searchable in the way you want it for very flexible search. Typical examples of this are

- **Fuzzy search** : some databases and platforms do not allow flexible fuzzy searching or require unnecessarily complex index configurations.
- **Semantic search** : if you want to perform semantic search (general meaning, intent, contextually aware) then you will need to handle this using LLM *embeddings*.

In both cases, Ziggy can handle this for you very efficiently by creating a streamlined data store with everything you need for these types of searches.

Initially, you can bulk load this data. Thereafter, you can incrementally load data when systems performs record level changes. This is all managed by simple Ziggy Flows.

[Transformation Flow details](search-loading-flows).



