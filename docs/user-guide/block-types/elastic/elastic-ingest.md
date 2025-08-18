---
title: Elastic Ingest
---

![Elastic ingest](/img/flows/blocks/elastic/elastic-ingest.png)

This Block performs two main functions.

- Configures an Elastic Search index
- Performs the actual ingestion when the Flow is run.

## Connection
You should select an Elastic Connection in [Connections](/user-guide/Connections).

## Index
Select the Elastic Search index from the dropdown.

You can also add a new index by pressing the **+New** button. You should then enter an index name. It should be all lowercase and no spaces or special characters.

## Rebuild Index
This will rebuild the index based on the Field information at the bottom of the Block. You should press this button whenever making field changes.

**Warning**: rebuilding the index will destroy any existing data in your index.

## Copy Fields Config
Once you have make field changes, you should press this button to copy the configuration to the clipboard. You then paste this into the [Elastic Search](elastic-search) Block so it has the matching field configuration.

## Field Configuration

### Load Fields
You should run your Flow up to this Block. This incoming edge will then have data on it that you can use to populate the fields list.

### ID field
It is important that you check the ID box to indicate which field contains the unique ID for the data.

### Store
Checking this box ensures that the field is actually used in the index. The incoming edge may have data that you don't need in the index.

### Type
This will automatically be set with a default setting based on the data read from the edge. However, you should modify this to helps Elastic configure the index properly.

- **Text** - makes it eligible for default fuzzy search.
- **Keyword** - if the field will be used for precise matching.
- **Semantic Text** - will create AI embeddings for general semantic search. 
- **Float** or **Integer** - set as appropriate for the data.
- **Date Time**
- **Boolean**

### Split
Check this box if the field contains an array of values. Text fields will then be stored in Elastic as an array. Each array element for each record is then findable.




