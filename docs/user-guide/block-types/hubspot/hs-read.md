---
title: HubSpot Read
---

# HubSpot Read

This block reads data from any Hubspot object in two ways.

- **Batch operation** - all records are read from the object in batches.
- **Lookup** - the records to read are determined by the incoming edge data.

## Batch

<img src="/img/flows/blocks/hubspot/hubspot-read-batch.png" alt="Hubspot Batch Read" width="700" />

You can see that we are reading batches of 100 records from Companies.

You can also specify which properties you fetch. If you leave this field empty, it will fetch all properties. 
Unless you need all properties, you should select only the properties you need. This will increase performance.

The fetched data will be placed on the output edge.

## Lookup
The configuration below shows how we are using data on the incoming edge to perform a lookup in Hubspot Companies.

<img src="/img/flows/blocks/hubspot/hubspot-read-lookup.png" alt="Hubspot Lookup Read" width="900" />

- We are using test data in the [Receiver block](/user-guide/block-types/core/Receiver) to demonstrate the way the lookup function works.
- In the **Edge key to search with** field, you specify which key on the incoming edge contains the value to lookup.
- In **HS property to search on**, you then specify which Hubspot property should be used for the lookup. It will show you only unique properties. The **Record Id** field is selected. 
- Finally, specify which properties to fetch. If you leave this field empty, it will fetch all properties.
  Unless you need all properties, you should select only the properties you need. This will increase performance.

**Tip** - run the Flow up to the Read block so there is some edge data available. 
This will populate the **Edge key to search with** dropdown. Alternatively, enter the key name and press enter.

You can see from the image, that the incoming edge has two elements (the ones in the Receiver) 
and the outgoing edge also has two elements (the ones that were looked up and fetched).

If you click on the outgoing edge, you'll see this.

<img src="/img/flows/blocks/hubspot/hubspot-read-lookup-outgoing.png" alt="Hubspot outgoing edge" width="500" />
