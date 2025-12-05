---
title: Data Store
description: Use Ziggy's Data Store utility block for persistent data storage and retrieval. Configuration guide with examples for data management flows.
keywords: [ziggy, utility blocks, data store, persistent storage, data management]
image: /img/ziggy-logo-light-bg.webp
---

# Data Store

Write to and read from the Data Store. You can choose between the following Platforms if you are running Ziggy Solo.

- **Internal** : storing data volumes in the hundreds of thousands.
- **AWS** : recommended if running Ziggy Solo on AWS
- **Azure** : recommended if running Ziggy Solo on Azure.

You can also access the Data Store from the [Javascript Block](user-guide/Data-Store-section.md).

## Data Store Browser
If using **Internal**, you can [view the Data Store contents](user-guide/Data-and-Memory-Store-Browser.md) from the Store menu item in the navigation bar.

## Namespace
The dropdown will contain the names of all existing namespaces if using **Internal**.
If the namespace does not yet exist or you are using **AWS** or **Azure**, enter the name in the input and press enter. 

## Operation Type
The following operation types are available.

### Create
There are three create modes. The mode is specified in the dropdown next the Operation Type dropdown.

- **Upsert** : update the record if the key exists; otherwise create a new entry.
- **Create** : create the record if it does not exist.
- **Error if exists** : create a record if the key does not exist; throw an error if the key does exist.

<img src="/img/flows/blocks/utility/data-store/data-store-upsert.png" alt="Data Store upsert" width="300" />

Ziggy will create Data Store key/value pairs based on what you specify in the
**Select key or "literal"** field - `recordId` in the screenshot above.

**Tip** - to make life easier, run the Flow up to the block so the drop-down is populated
with keys found on the input edge. Otherwise, type the name of the key in the input field and press enter.


### Update
Update a record if the key exists, otherwise ignore.

Same configuration as **Create** above.

### Read (Batch)
If **Key** is not specified, it will be treated as a Batch operation and the batch size 
specifies the number or records to read in a batch.

You can see the **sql_customers** namespace being read, 100 records at a time.

<img src="/img/flows/blocks/utility/data-store/data-store-batch-array.png" alt="Batch read array" width="500" />

### Read (edge data driven)
You can also read data from the data store using values specified in the incoming edge data.

Ziggy will fetch all the Data Store key/value pairs based on what you specify in the 
**Select key or "literal"** field - `recordId` in the screenshot below.

**Tip** - to make life easier, run the Flow up to the block so the drop-down is populated 
with keys found on the input edge. Otherwise, type the name of the key in the input field and press enter.

<img src="/img/flows/blocks/utility/data-store/data-store-edge-read.png" alt="Batch read array" width="300" />

### Delete
Deletes the **Key** from the store based on the incoming edge data. 
All elements on the edge will be deleted using the specified edge key in **Select key or "literal"**.

**Tip** - to make life easier, run the Flow up to the block so the drop-down is populated
with keys found on the input edge. Otherwise, type the name of the key in the input field and press enter.


<img src="/img/flows/blocks/utility/data-store/data-store-delete.png" alt="Data store delete" width="300" />

## Delete all namespace keys
This is used to delete all data from the specified namespace(s).

<img src="/img/flows/blocks/utility/data-store/data-store-delete-namespaces.png" alt="Data store delete namespaces" width="300" />
