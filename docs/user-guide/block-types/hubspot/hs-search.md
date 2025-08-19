---
title: Hubspot Search
---

This is used to perform a HubSpot search. It is typically used in conjunction with the [AI Search Prompt Block](/user-guide/block-types/ai/ai-search-prompt), in which case you can ignore the information below.

![HubSpot search](/img/flows/blocks/hubspot/hs-search-flow.png)

## Configuration

### Connection
Choose a [Connection](/user-guide/Connections#hubspot-object) that points to the HubSpot instance you want to query.

## Independent execution

You can use this independently to run a HubSpot search query, in which case the previous block should output the following array.

```javascript
[
  {
    objectType: "deals",
    limit: 5,
    properties: ["dealname", "amount", "dealstage", "closedate"],
    after: "",
    sorts: [],
    filterGroups: [
      {
        filters: [
          {
            propertyName: "amount",
            operator: "GT",
            value: 10000,
          },
        ],
      },
    ],
    isCount: false,
  },
  {
    limit: 5,
    offset: 0,
    query: "deals worth more than 10000",
    callingUserId: "freddy.may@ziggyservices.com",
  },
]
```

The first array element contains an object that is passed to the HubSpot API. Refer to the [HubSpot API docs](https://developers.hubspot.com/docs/guides/api/crm/search?p=7895%2F) for more information.

The second array element contains pagination and other information. Refer to [Search Flows](/search/search-prompt-flows#receiver-data-object) for information about this object.

## Edge Output
The edge output will contain data in a standardised format and depends on the `responseType` value (optional) in the second array element.

You should run various queries that generate listings or aggregated output on the output edge to see the data returned.
