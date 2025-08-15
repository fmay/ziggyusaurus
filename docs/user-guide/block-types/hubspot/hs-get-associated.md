---
title: HubSpot Get Associated Object
---

# HubSpot Get Associated Object

Fetches associations between specified HubSpot objects.

The following image shows 91 companies being fetched and 830 association deals with those 91 companies.

<img src="/img/flows/blocks/hubspot/hubspot-get-associated.png" alt="HubSpot get associated" width="900" />

For this to work, the following is assumed that the elements in the incoming edge data array 
have one key `hs_object_id` to uniquely identify a HubSpot object.

The HubSpot Read block always returns an `hs_object_id` key, even if not specified in the properties to fetch.

If you are not using a HubSpot Read block, then your data is expected to have one `hs_object_id` key regardless.

You should then configure the block as follows.

- **HS Object on input** - this is the Object that relates to the `hs_object_id` on the incoming edge,.
- **HS Object to output** - this is the Object you want to associate with.
- **Association Type** - this dropdown will contain the associations types that are defined in HubSpot.
- **Properties to fetch** - the properties to fetch from **HS Object to output**.
- **Output both XXX and YYY** - this will create an output record that contains both objects with an object prefix (see below).
- **Output association label** - this will output the association label as a key.

The above configuration results in the following data.

<img src="/img/flows/blocks/hubspot/hubspot-get-associated-data-out.png" alt="HubSpot get associated data out" width="500" />
