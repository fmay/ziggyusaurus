---
title: Batching - large data sets
---

# Batching - large data sets

When performing tasks like data migrations or other operations that deal with large amounts of data it is not possible to have the data in its entirety in memory.

When working with APIs there are often limits placed on the amount of data that an API endpoint will accept in a single call.

From a speed perspective, it is much faster to call an endpoint once with 100 records of data that to call an endpoint 100 times with one unit of data.

These situations require batching in order to optimise for memory, speed and API methods.

## Blocks that support batching
All blocks can be used within a batch loop. The following blocks initiate a batch loop.
The following blocks offer batching.

- [HubSpot Read](/user-guide/block-types/hubspot/hs-read)
- [SQL (select)](SQL.md)
- [REST](REST-Call.md)
- [File (read)](/user-guide/block-types/utility/file-reader-writer)
- [Data Store (read)](Data-Store.md)
- [Memory Store (read)](/user-guide/memory-store/Memory-Store)
- [Airtable](/user-guide/block-types/utility/airtable)
- [Javascript](Javascript.md)

## Example

![reporting-prep](/img/flows/batching/batching-reporting-prep.png)

- The HubSpot Read block reads batches of 100 Deals from HubSpot.
- It then gets associated Companies
- And writes the resulting data to a database table.
- The key thing is the **Batch End** block. This loops back to the HubSpot Read block until there is no more data to fetch.

## Example - Javascript
You can batch with Javascript as shown in the following example. Refer to the [Javascript Block](Javascript.md) for more details.

![JS Batching](/img/flows/batching/batching-js-heavy.png)

The first Javascript initiates the batch with ```batch(BATCH_SIZE)```. When there is no data left to process. it calls ```batchEnd()```.

<img src="/img/flows/batching/batching-js-1.png" alt="Batch Size" width="400" />

The second Block shows how you can get ```batchIteration()``` and ```batchOffset()``` values as the batch loops

<img src="/img/flows/batching/batching-js-2.png" alt="Batch Info" width="400" />

Note the Batch End Block is the point at which execution loops back until ```batchEnd()``` is called.

