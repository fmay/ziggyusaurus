---

title: About Ziggy
description: Discover Ziggy's no-code data platform for AI-powered search, data flows, and integrations. Connect any data source with visual flows and natural language queries.
keywords: [ziggy, no-code data platform, AI search, data integration, ETL, flows, automation, hubspot, salesforce]
slug: /
image: /img/ziggy-logo-light.webp
---

# About Ziggy

Ziggy is for any software/platform company that needs to make it incredibly easy to access its data.

It lets **non-developers** read data from and write to your platform whether for  

- your customers 
- or your own internal usae.

This means your developers can focus on their core product responsibilities and your customers don't have to try to find scarce developer resource to integrate with your platform.

## Example - HubSpot
The screenshot below shows a simple example of getting company data and associated contacts out of HubSpot and into a Snowflake data warehouse. 

<img src="/img/about/about-hs-associations.png" alt="Alert" width="900" />

- It reads a batch of 100 records from HubSpot Companies.
- Fetches associated Contact records for each of the companies fetched.
- Writes them to a Snowflake data warehouse.
- Data can be viewed, validated and transformed as it moves from Block to Block.
- You can step through the Flow one Block at a time - great when building and debugging Flows.

## Your Platform's own Custom Blocks
The secret to making your company's data easy to access is the **Custom Block**. You can add as many Custom Blocks as makes sense for your platform.

Continuing the HubSpot example, below are some of the custom HubSpot Blocks (there are 12 in total). Each one focuses on making one specific task as easy as it can be,

Of course, you can achieve the same the API but it is a non-trivial API and, of course, only developers can find their way around it.

<img src="/img/about/about-hs-blocks-group.webp" alt="Alert" width="900" />

As data moves around the Flow from Block to Block, you can validate and transform this data in any way you choose and send it to other platforms (such as files, databases, APIs or other platforms' Custom Blocks).

A Custom Block can access your platform in several ways and abstract away all the complexity.

- Your platform API - the preferred and usual way.
- Direct database access - may be ok for read access but likely unsafe for write access unless protected.

## What about Zapier or Make.com?
Both of these platform can also be used by non-developers. However, they have some drawbacks, especially for medium to large size companies.

- You have no control over security and have no control over how or where your data is stored - Ziggy gives you **absolute** control.
- You have no control over performance - Ziggy gives you **absolute** control.
- Usage based costs escalate over time in a way that is hard to predict and budget for. Ziggy's pricing is independent of usage.

## Security, Performance and Pricing
Ziggy is perfect for both you as a platform company and your customers. here's why.

- Ziggy can run on your own cloud infrastructure, meaning you control all aspects of access and security.
- Each customer gets their own, isolated Ziggy server, providing reassurance that their data is fully isolated from other customers.
- The Ziggy server is highly performant but for most cases runs very happy in a $12 per month AWS Instance. 
- Ziggy can run large number of flows simultaneously and has superb queuing and rate-limiting support. It copes very nicely even with Internet of Things applications where large volumes of data need to be processed.
- Performance can be tuned in many ways depending on the nature of your Flows and volumes.
- We do not have usage based pricing making it easy for you and your customers to budget.

## Product or Services
If you want assistance in building Custom Blocks or designing Flows, we are here to help.

- Custom Block development
- Building end-to-end solutions
- Flow design and development
- Training
- Support

## Contacting us

If you have any questions or require a demonstration, please [contact us here](https://www.ziggyservices.com/contact).
