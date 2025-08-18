---
title: Search Flows
---

A Search Flow is responsible for taking a natural language query and returning data from whichever platform it needs to.

TODO: IMAGE

## AI Prompt Block
This Block is responsible for turning the natual language query into a platform specific one. Its main features are

- Uses a fully customizable LLM prompt to do the query translation.
- It has templates for standard platforms so you only need to add use-case specific customizations. Or you can rewrite the entire prompt should you wish to.

## Platform specific Block
the AI Prompt Block outputs a query in the right format to the search Block. Common examples are

- SQL (includes data warehouses like SnowFlake, BigQuery etc)
- Elastic Search
- Hubspot, SalesForce (etc.)
- Any REST API 
- We can also build custom search blocks for any platform that offers an API or a well defined query language of some sort.

## Custom Logic
Many search Flows contain just the AI Prompt Block and the platform specific search Block. However, any additional logic can be added into a Flow.

Below is a Flow that can be called by both ChatterBox and Slack to perform a HubSpot search. 

- You can see the AI Prompt and Hubspot Search Blocks on the top row.
- It then simply returns data to ChatterBox if the query can from ChatterBox...
- or passes it to one of the two [Slack Blocks Formatter Block](../TODO.md) if the request came from Slack.

TODO : Image AI Hubspot Search Slack

## Non AI Search
In some cases, you may require a query that does performs a high targeted search. The one below, for example, is called when a Hubspot deal is passed in and the associated line items should be returned.

TODO: Image for AI Hubpot Line Items

## Testing Flows
You can test your search Flows directly from the Ziggy UI. You can provide test data in the [Receiver Block](../TODO.md) so you don't have to call it from whichever front end you are using.

Ziggy provides excellent [debugging features](user-guide/editor/Debugging) that let you step through the Flow, one block and a time.

You can then inspect the data flowing between Blocks to diagnose issues. For example, you might want to see exactly what data is being output from the [AI Search Prompt Block](../TODO.md). This might inform what prompt changes you need to make in that Block to pass an better query to the search block itself.

## Prompt Engineering
You have full control over the prompt itself within the [AI Search Prompt Block](../TODO.md). This includes the ability to test natural queries directly from the Block itself.


