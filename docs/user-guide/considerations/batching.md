---
title: Batching
---

Batching allows to you handle pagination scenarios on your data source.

[Click here](user-guide/Batching.md) for full documentation on Batching.

Your data source might contain very large numbers of records. It is therefore necessary to process these in batches to avoid overload and fetch limits imposed by 3rd parties.

There are several Blocks that support batching operations

- HubSpot Read
- SalesForce Read
- REST (all methods)
- DataStore (Read)
- MemStore (Read)
- File (Read)
- SQL (Read)
- Javascript (when using batch.begin())
- Iterator
- Loop 

Some systems might enforce limits (such as HubSpot, where it limits the maximum number of records you can read). In other cases, for example SQL, you will make your own judgment about sensible batch sizes in order not to overload the system.

In most batching supported blocks, with the exception of Iterator and Loop Blocks, you can 

- enable or disable batching
- specify the size of the batch (number of records to read)
- specify the maximum number of iterations to process.


