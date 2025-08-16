---
title: Data Store
---

# Data Store

Write to and read from the Data Store. You can choose between the following Platforms if you are running Ziggy Solo.

- **Internal** : storing data volumes in the hundreds of thousands.
- **AWS** : recommended if running Ziggy Solo on AWS
- **Azure** : recommended if running Ziggy Solo on Azure.

You can also access the Data Store from the [Javascript Block](Data-Store-section.md).

## Data Store Browser
If using **Internal**, you can [view the Data Store contents](Data-and-Memory-Store-Browser.md) from the Store menu item in the navigation bar.

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

![Data Store upsert](data-store-upsert.png){width="300"}

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

![Batch read array](data-store-batch-array.png){width="500"}

### Read (edge data driven)
You can also read data from the data store using values specified in the incoming edge data.

Ziggy will fetch all the Data Store key/value pairs based on what you specify in the 
**Select key or "literal"** field - `recordId` in the screenshot below.

**Tip** - to make life easier, run the Flow up to the block so the drop-down is populated 
with keys found on the input edge. Otherwise, type the name of the key in the input field and press enter.

![Batch read array](data-store-edge-read.png){width="300"}

### Delete
Deletes the **Key** from the store based on the incoming edge data. 
All elements on the edge will be deleted using the specified edge key in **Select key or "literal"**.

**Tip** - to make life easier, run the Flow up to the block so the drop-down is populated
with keys found on the input edge. Otherwise, type the name of the key in the input field and press enter.


![Data store delete](data-store-delete.png){width="300"}

## Delete all namespace keys
This is used to delete all data from the specified namespace(s).

![Data store delete namespaces](data-store-delete-namespaces.png){width="300"}
