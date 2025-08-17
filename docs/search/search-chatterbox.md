---
title: ChatterBox
---

ChatterBox is Ziggy's own UI for searching any of your data. 

TODO:Video (longer one)

## Source Code
The source code is freely available should you want to modify and tailor it to your own requirements. It is an React application.

## How it works
ChatterBox requires basic customization. For standard cases, this can be done in an hour or so. However, almost any aspect can be fine-tuned and enhanced so more complex requirements will take longer.

We can perform these customizations for you, or you can do it yourself with the source code.

Here are a few key points.

- ChatterBox connects with a simple Ziggy Flow to perform the actual search.
- You can connect to multiple data targets. Each different target has a button in the header area. 
- You use natural language queries to perform any search.
- The search results are automatically displayed as listings, tables or crosstabs, depending on the nature of the data returned.
- Aggregation queries can show a pie, line or bar chart.
- Listings can be customised to show whatever fields you want to see and how each field should be formatted.
- You can drill down from any record to display some or all fields in a customizable card.
- The history of all queries and results are saved ot the listing so you can recall them at any time.
- Your query history can also be shown and managed.

## Search Flows
When ChatterBox users enter a query, ChatterBox passes control to a Ziggy Flow. These Flows are simple and quickly configured.

Most [Search Flows](search-prompt-flows.md) will contain an [AI Prompt Block](TODO) and a platform specific search Block.

Data is returned to ChatterBox in a standardised format so ChatterBox can instantly render in the appropriate listing format.

Note that all Ziggy Flows are API callable so you can manage the UI yourself if you prefer.

## Want us to configure ChatterBox (or Flows) for you?
If you want any assistance configuring any aspect of Ziggy, including ChatterBox, please [contact us](https:/ziggyservices.com/contact) to discuss.

