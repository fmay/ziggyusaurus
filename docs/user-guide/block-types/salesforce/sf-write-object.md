---
title: Salesforce Write Object
description: Create and update Salesforce CRM objects using Ziggy's Salesforce Write block. Complete guide for Salesforce data synchronization flows.
keywords: [ziggy, salesforce write, crm integration, data update, salesforce objects, data sync]
image: /img/ziggy-logo-light.webp
---

# SalesForce Write Object

This block writes data on the incoming edge to the specified SalesForce object.

**Important** : all keys on the input edge should be valid SalesForce field names (not labels) and contain valid data for each property.

<img src="/img/flows/blocks/salesforce/sf-write.png" alt="SalesForce Write" width="300" />

# Connection
Choose a Connection that you have defined in the [Connection Manager](/user-guide/Connections).
This will contain your SalesForce API key or reference a secret containing it. If there is only one SalesForce connection
defined, it should be auto-selected.

# Object
The SalesForce object to update.

# Operation type
## Upsert
You can choose to **Upsert** (default) or update. Upserting requires one of the following keys to be present on the input edge. 

- A valid SalesForce object Id
- An external system field that uniquely identifies the data. This will usually be the unique ID in another system or database for the chosen object.

If you uncheck **Upsert**, data will be updated. The record is expected to exist already in SalesForce.

## Perform data property validation
This scans the incoming edge data and checks it against the available properties for the specified SalesForce object.
It checks both the existence of the property and that the data about to be updated is suitable for the data type of the property.

## Invalid to second output edge
If you have selected **Perform data property validation** then this option places the input edge data items that failed the validation
onto the second output edge.

This lets you deal with errored data as you see fit. You might, for example, write it to the data store so you can inspect it later.

The above screenshot shows as example of invalid data being written to the second output edge. 
This is because `Id: 'invalidId"` is not a proper SalesForce object id.

If you don't select this option, data that failed the validation will be discarded.

## Edge data
The upsert operation is performed on the following basis.

- The edge is assumed to have data that is in the right format for SalesForce to receive.
- The edge data should contain data (whether array or not) that is a collection of key/value pairs with no extra data.
- SalesForce will throw an error if data contains a property key where the property does not exist. You should there use the above mentioned validation to avoid this.

## Edge key for matching
You need to specify which key on the incoming edge contains the data that should be looked up in SalesForce.
This should a SalesForce property that is unique and should be used as the basis for the upsert/update lookup.

## SF properties to write
Specify which properties on the incoming edge should be written to SalesForce.
If left empty, all properties on the edge will be written.

## Namespace for errors
You can also write any failed writes to a Ziggy Data Store namespace. Specify the name of an existing namespace 
or enter a new name.
