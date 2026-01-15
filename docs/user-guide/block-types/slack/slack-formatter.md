---
title: Slack Block Formatter
---

You use this Block in conjunction with [Slack](/search/search-slack) apps. It handles the translation of response data into a format that Slack is able to display.

If you watch the video below, you can see how queries are entered by a user and data is returned in a nicely formatted way.

<iframe 
  src="https://nxucrsk2vrk61vtm.public.blob.vercel-storage.com/website-videos/slack-overview-UAw2NUTAo8NJHOiblOdEvfh8sSPyBT.mp4" 
  width="100%" 
  height="400" 
  allow="fullscreen; picture-in-picture" 
  allowfullscreen>
</iframe>

## Slack Block Kit Builder
Refer to the [Slack Block Kit Builder](https://app.slack.com/block-kit-builder) for details on Slack Blocks.

With this you can experiment with Blocks and then copy and paste into Ziggy for token insertion.

## Configuration Syntax

Below are the results of a simple Slack query */find deals worth more than 1000*.

![Slack query](/img/flows/blocks/elastic/slack-query.png)

Below is the Slack Block configuration for returning this data

```JavaScript
[
  {
    type: "section",
    text: {
      type: "mrkdwn",
      text: "We found *##count##* deals",
    },
  },
  {
    type: "divider",
  },
  {
    type: "repeat-section|edge_key or ommit (see below)",
    repeat: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*<https://app-eu1.hubspot.com/contacts/144231748/record/0-3/##properties.hs_object_id##|##properties.dealname##>*
*Deal Size*: £formatNumber(##properties.amount##)
*Created*: formatISODate(##properties.createdate##)
*Stage*: ##properties.dealstage##`,
        },
      },
      {
        type: "actions",
        elements: [
          {
            type: "button",
            text: {
              type: "plain_text",
              emoji: true,
              text: "Line Items",
            },
            value: `executeFlow|9b019341-8a84-44a1-aa8b-e8b9d2a7aebe|ziggy.ek-YqdAKUB/yy4ZUtU_ilKIcTvAVJv7t2|getEnvironmentMode()|{"dealId": "##properties.hs_object_id##"}`,
          },
        ],
      },
      {
        type: "divider",
      },
    ],
  },
  {
    type: "actions",
    elements: [
      {
        type: "button",
        text: {
          type: "plain_text",
          emoji: true,
          text: "Fetch more",
        },
        action_id: "fetch_more",
        value: "cachedQuery()",
        style: "primary",
      },
      {
        type: "button",
        text: {
          type: "plain_text",
          text: "Delete",
        },
        style: "danger",
        action_id: "delete_message",
      },
    ],
  },
]
```

### Repeat Section
Where you have multiple rows of data to return, you should specify `type: repeat-section`. This is a Ziggy key and is not valid Slack Block syntax. This will be replaced during Flow execution. 

**Important**: `type: "repeat-section|edge_key or ommit"`. This should be set to specify where the repeating data can be found on the incoming edge.

- `type: "repeat-section"` will just use the incoming edge data array for the repeating data. This is the most common case.
- `type: "repeat-section|data"` indicates that the repeating data can be found in the `data` key of the first element of the incoming data. You would use this if the incoming data also contains count or other data associated with the main repeating data. 

```JavaScript
{
    type: "repeat-section|edge_key or ommit (see above)",
    repeat: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*<https://app-eu1.hubspot.com/contacts/144231748/record/0-3/##properties.hs_object_id##|##properties.dealname##>*
*Deal Size*: £formatNumber(##properties.amount##)
*Created*: formatISODate(##properties.createdate##)
*Stage*: ##properties.dealstage##`,
        },
      },
      {
        type: "actions",
        elements: [
          {
            type: "button",
            text: {
              type: "plain_text",
              emoji: true,
              text: "Line Items",
            },
            value: `executeFlow|9b019341-8a84-44a1-aa8b-e8b9d2a7aebe|ziggy.ek-YqdAKUB/yy4ZUtU_ilKIcTvAVJv7t2|getEnvironmentMode()|{"dealId": "##properties.hs_object_id##"}`,
          },
        ],
      },
      {
        type: "divider",
      },
    ],
  },
```

### Tokens
By inspecting the incoming edge data, we have an array of the following data.

```JavaScript
{
    "createdAt": "1996-11-13T00:00:00.000Z",
    "archived": false,
    "id": "169292458174",
    "properties": {
      "amount": "10729.2",
      "closedate": null,
      "createdate": "1996-11-13T00:00:00Z",
      "dealname": "Piccolo und mehr",
      "dealstage": null,
      "hs_lastmodifieddate": "2025-08-07T15:52:21.660Z",
      "hs_object_id": "169292458174",
      "pipeline": null
    },
    "updatedAt": "2025-08-07T15:52:21.660Z"
  }
```

Looking at the Repeat Section code, you can see

```JavaScript
text: `*<https://app-eu1.hubspot.com/contacts/144231748/record/0-3/##properties.hs_object_id##|##properties.dealname##>*
*Deal Size*: £formatNumber(##properties.amount##)
*Created*: formatISODate(##properties.createdate##)
*Stage*: ##properties.dealstage##`
```

You can see various tokens such as `##properties.hs_object_id##`. These are replaced with the values found in the edge data.

### Functions
We provide the following list of functions to help format your data. For example `£formatNumber(##properties.amount##)`.

We are adding more functions, so if you have require one, please [contact us](https://ziggyplatform.com/contact).

- **formatNumber** - formats a number to 2 decimal places.
- **formatISODate** - converts an ISO date string into a friendly format.
- **formatISODateTime** - same, but includes time.


### Pagination
In the bottom of the full example block code above, you will see the section that handle the **Fetch more** and **Delete** buttons.

![Slack query](/img/flows/blocks/elastic/slack-query.png)

Here's the Slack Block code.

```javascript
{
    type: "actions",
    elements: [
      {
        type: "button",
        text: {
          type: "plain_text",
          emoji: true,
          text: "Fetch more",
        },
        action_id: "fetch_more",
        value: "cachedQuery()",
        style: "primary",
      },
      {
        type: "button",
        text: {
          type: "plain_text",
          text: "Delete",
        },
        style: "danger",
        action_id: "delete_message",
      },
    ],
  },
```

- `cachedQuery()` - include this to fetch the next page of data.
- the Delete button, which is optional, removes the message from Slack if you want the user to be able to keep things tidy in Slack.