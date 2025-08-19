---
title: Elastic Search
---

This Block is used to perform a search on an Elastic Search index. 

It expects to receive an object on the input edge that contains the Elastic query object in the first array element and other parameters in the second, both of which are provided by the the [AI Search Prompt](../ai/ai-search-prompt.md) Block.

## Typical Flow
Below is an example of a typical Flow. 

![Elastic search flow](/img/flows/blocks/elastic/elastic-search-flow.png)

## Configuration and testing
We recommend using Ziggy's [Debugging](/user-guide/editor/Debugging.md) to configure the Flow. This lets you set up without calling the Flow externally until you are ready.

## Flow Input
Search Flows should pass in an input object containing the query, pagination details etc. 

This is explained in [Search Flows](/search/search-prompt-flows#receiver-data-object).

### Test Data
You can put the Flow Input it the data section of the [Receiver](/user-guide/block-types/core/Receiver). You can see this in the above screenshot.

## Configuration

### Connection
You should select an Elastic Connection in [Connections](/user-guide/Connections#elastic-search).

## Index
Select the Elastic Search index from the dropdown.

## Paste Ingest Config
If you have created and configured the index using the [Elastic Ingest](elastic-ingest) Block, then you should press the **Copy Field Config** button in that Block. Then press the **Paste Ingest Config** button in this Block to bring over the configuration. 

## Fields configuration
Once the fields are visible at the bottom of the Block, you can check the **Fuzz** box where you require fuzzy matching. 

You will notice that this is only possible for **Text** type fields. Keyword fields require exact matching.