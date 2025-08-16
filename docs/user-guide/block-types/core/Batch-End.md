---
title: Batch-End Block
---

# Batch End

You should always use the Batch End Block in combination with any Block that supports batching.

- Javascript Block that contains the ```batch.begin()``` method
- SQL
- Data and Memory Store block - reads
- File Block - reads
- REST - GET operations that support paging
- HubSpot Read, HubSpot Get All Owners

It signals the end point of the batch loop so Ziggy can return control to the initiating Block.

If you don't use the Batch End Block (but it is strongly recommended that you do), then the Terminator Block will act as the loop-back point 
until there is now more data, at which point the Flow will terminate. 

![Batch End](block-batch-end.png)

The above image shows the Batch End block looping back to the SQL block. It will continue to loop back 
until there are no more records available or until the maximum number of iterations has been reached (0 iterations means read all).

## Wait for all input edges
By default, this will not loop back until all input edges are populated. 
However, there are cases where you want to loop back as soon as one input edge is populated.

## Show progress
When there are large numbers of records to be processed, the Batch End block can send progression 
information to the Queue page (navigation bar). 

You can see how far through a job a Flow has progressed on this page. 

![Batch End](batch-end-progress.png)
