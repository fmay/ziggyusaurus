---
title: SalesForce Set Associations
---

# SalesForce Set Associations

This block creates associations between two object types.

## Edge data
This block expects the incoming edge data to contain two keys that contain an `Id` value. One for each of the objects to associate.

The data below shows two keys `accountId` and `wordId`. Each of these contains a SalesForce `Id`.

![SalesForce set associations](/img/flows/blocks/salesforce/sf-set-associations.png){width=900}

## Connection
Specify a valid SalesForce connection from the [Connection Manager](/user-guide/connections/Connections).

## Namespace for errors
If you want to capture errors to a namespace in the [Ziggy Data Store](Data-Store.md), choose an existing namespace 
from the dropdown or enter a new namespace name.

## From and To objects
The objects to associate.

**Important** : the From object should be the child child object in the parent/child relationship pair.

## Edge key for '***' Id
This applies to the fields in each of the From and To sections.

It tells Ziggy where to look for data on the input edge for the `Id`. In the above example, we 
specify the `wordId` and `accountId` keys.

## '***' field for '***'
For the From object, we need to specify which SalesForce object field should be written to.

## Error output edge
The second of the two output edges will contiain any data that could not be written to SalesForce. 
You do not have to use this output edge. The above example shows data being passed to the [Sinkhole](/user-guide/block-types/core/sinkhole) block. 
This allows you to inspect errored data, although you can do whatever you like with the data.

