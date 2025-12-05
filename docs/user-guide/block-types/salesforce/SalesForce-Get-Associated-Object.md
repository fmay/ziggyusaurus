---
title: Salesforce Get Associated Object
description: Retrieve related Salesforce objects and relationships using Ziggy's Get Associated Objects block. Guide for complex CRM data relationships.
keywords: [ziggy, salesforce associations, related objects, crm relationships, salesforce data, object relationships]
image: /img/ziggy-logo-light-bg.webp
---

# SalesForce Get Associated Object

Fetches associations between specified SalesForce objects.

The following image shows 91 companies being fetched and 830 association deals with those 91 companies.

<img src="/img/flows/blocks/salesforce/sf-get-associated.png" alt="SalesForce get associated" width="900" />

For this to work, the following is assumed that the elements in the incoming edge data array
have one key `Id` to uniquely identify a SalesForce object by its `Id`.

The SalesForce Read block always returns an `Id` key, even if not specified in the properties to fetch.

If you are not using a SalesForce Read block, then your data is expected to have the `Id` key regardless.

You should then configure the block as follows.

- **Object on input** - this is the Object that relates to the `Id` on the incoming edge. Ziggy filters objects in the dropdown to contain only standard and custom objects. If you want the full set of SalesForce objects, check the **All** box.
- **Object to output** - this is the Object you want to associate with. Ziggy filters objects in the dropdown to contain only standard and custom objects. If you want the full set of SalesForce objects, check the **All** box.
- **Association Type** - this dropdown will contain the associations that are defined in SalesForce between the To and From objects.
- **Properties to fetch** - the properties to fetch from **Object to output**.
- **Output both XXX and YYY** - this will create an output record that contains both objects with an object prefix (see below).
- **Output association label** - this will output the association label as a key.

The above configuration results in the following data.

<img src="/img/flows/blocks/salesforce/sf-get-associated-data-out.png" alt="SalesForce get associated data out" width="500" />

## Many to Many / Junction relationships
SalesForce manages these as so-called *Junction Objects*. The best way to deal with these is to use the [SalesForce Write](/user-guide/block-types/salesforce/sf-write-object) 
object where you specify the Junction Object as the Object Name and then write the Ids for both side of the 
relationship by specifying the fields that contain data on the input edge, 