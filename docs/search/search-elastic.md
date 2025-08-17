---
title: Elastic Search
---

The beauty of **[Elastic Search](https://www.elastic.co/)** is it's ability to search data with great flexibility and fuzziness. It is also supports perform semantic search very well.

## Hubspot Example
Let's say you have a lot of data in Hubspot and you want to be able to search with more flexibility than Hubspot itself offers.

You can create Ziggy Flows that load data into an Elastic Index that manages very flexible searching, presents a list of records using [Slack](TODO), [ChatterBox](TODO) or your own UI. From there you can directly jump into Hubspot records using a simple link

Data can be bulk loaded initially and then updated in real-time using WebHooks and another simple Flow whenever related Hubspot data is edited.

## Database/Data Warehouse Example
Similarly, you may have your data in a Database or Data Warehouse and want to have flexible searching. Although databases can be tuned with special indexes to perform such tasks (good fuzzy matching can be challenging to configure well) it is very easy to simply load the data you want to search on into an Elastic search.

## Ziggy Blocks
To support Elastic, Ziggy has three Blocks for quickly and easily working with Elastic.

### AI Prompt Block
The [AI Prompt Block](TODO) turns any natural language query into a platform specific query.

### Elastic Ingest Block
The [Elastic Ingest Black](TODO) handles both Elastic Index configuration and data ingestion. It is used as a part of an [ingest Flow](TODO).

### Elastic Search Block
This is used in a Flow, in conjunction with the [AI Prompt Bock](TODO), to perform the actual Elastic search. 