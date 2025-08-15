---
title: HubSpot Write
---

# HubSpot Write

This block writes data on the incoming edge to the specified HubSpot object.

**Important** : all fields on the input edge should be valid HubSpot properties and contain valid data for each property.

![HubSpot Write](hubspot-write.png#width=300)


# Connection
Choose a Connection that you have defined in the [Connection Manager](Connections.md). 
This will contain your HubSpot API key or reference a secret containing it. If there is only one HubSpot connection
defined, it should be auto-selected.

# Object 
The HubSpot object to update.

# Operation type
## Upsert
You can choose to **Upsert** (default) or update. Upserting requires one of the following keys to be present on the input edge.

- A valid Hubspot object Id
- An external system field that uniquely identifies the data. This will usually be the unique ID in another system or database for the chosen object.

If you uncheck **Upsert**, data will be updated. The record is expected to exist already in HubSpot.

## Perform data property validation
This scans the incoming edge data and checks it against the available properties for the specified HubSpot object.
It checks both the existence of the property and that the data about to be updated is suitable for the data type of the property.

## Invalid to second output edge
If you have selected **Perform data property validation** then this option places the input edge data items that failed the validation
onto the second output edge.

This lets you deal with errored data as you see fit. You might, for example, write it to the data store so you can inspect it later.

If you don't select this option, data that failed the validation will be discarded.

## Edge data
The upsert operation is performed on the following basis.

- The edge is assumed to have data that is in the right format for HubSpot to receive.
- The edge data should contain data (whether array or not) that is a collection of key/value pairs with no extra data.
- HubSpot will throw an error if data contains a property key where the property does not exist. You should there use the above mentioned validation to avoid this.

## Edge key for matching 
You need to specify which key on the incoming edge contains the data that should be looked up in HubSpot.
This should a HubSpot property that is unique and should be used as the basis for the upsert/update lookup.

## HS properties to write
Specify which properties on the incoming edge should be written to HubSpot. 
If left empty, all properties on the edge will be written.

