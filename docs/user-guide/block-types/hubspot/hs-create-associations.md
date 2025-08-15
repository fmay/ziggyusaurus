---
title: HubSpot Set Associations
---

# HubSpot Set Associations

This block creates associations between two object types. 
The Migration Tutorials contains an example of this being used. 
Please refer to 

- Migration 30 - HubSpot Company -> Deal Associations
- Migration 31 - HubSpot Deal -> Line Items Associations

## Edge data
This block expects the incoming edge data to contain two keys that contain an `hs_object_id` value. One for each of the objects to associate.

The data below shows two keys **customer** and **deal**. Each of these contains an `hs_object_id` key.

<img src="/img/flows/blocks/hubspot/hubspot-set-associations-data.png" alt="HubSpot set associated" width="400" />

You can now specify the path to each of these for the **From** and **To** objects as shown below.

<img src="/img/flows/blocks/hubspot/hubspot-set-associations.png" alt="HubSpot set associated" width="300" />



