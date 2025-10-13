---
title: REST API Call Block
description: Make REST API calls with Ziggy's REST Call utility block. Complete guide for API integration, pagination, and data retrieval flows.
keywords: [ziggy, utility blocks, rest api, api calls, http requests, api integration]
image: /img/ziggy-logo-light.webp
---

This Utility Block is used to make REST API calls.

<img src="/img/flows/blocks/utility/REST/REST-block-get.png" alt="400" width="600" />

Note, you can also make REST calls using the `axios` method in the [Javascript Block](user-guide/block-types/utility/REST-Call.md).

## Method
Choose the REST method from the button.

## URL
Specify the fully URL. 

You can insert tokens in the URL field (see below). The is most commonly require for pagination where you have `offset` and `skip` type pagination query parameters.

## Headers
You can add as many headers as you require. Tokens can be inserted 

## Batching
All methods support [batching](user-guide/Batching.md). If you check the **Batch** box, then you should specify 

- **Batch size** - Ziggy expects to find a query parameter with a value token `{offset}`. This token will be replaced at runtime.
- **Max iterations** - the number of batch iterations to execute. A value of 0 indicates it should loop until there is no more data available.

This is an example of a `GET` call for batching.

`https://api.hubapi.com/crm/v3/objects/companies?limit={limit}&after={offset}`

And this shows a `POST` operations body field for this URL.

`https://api.hubapi.com/crm/v3/objects/companies/search`

```javascript
{
  query: {edge.query},
  limit: {limit},
  after: {offset},
  sorts: [],
  properties: ['name'],
  filterGroups: []
}
```





## Remove {offset} for 1st iteration
This applies to all methods when in Batch mode.

Some platforms (notably HubSpot) will error if you include the pagination value (`after` for HubSpot) query parameter for the 1st iteration. 

Checking this box instructs ziggy to remove the `{offset}` token and its associated parameter name for the 1st batch iteration.

This can be applied to the URL and the body.



## Token insertion
You can insert tokens in the following input fields.

- URL
- Header input fields
- Body



### Batch End Block
Include a [Batch End Block](user-guide/block-types/core/Batch-End.md) downstream of the REST Block as the loop back point. You can include other Blocks in between.
