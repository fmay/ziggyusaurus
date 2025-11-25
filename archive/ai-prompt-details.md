---
title: Detailed Prompt Guidance
description: Master AI prompt engineering for Ziggy's search functionality. Learn to customize and optimize prompts for better AI search results and accuracy.
keywords: [ziggy, ai prompts, prompt engineering, ai search optimization, search customization, nlp prompts]
image: /img/ziggy-logo-light.webp
---

Engineering the prompt is the most important part of search. Ziggy provides you with default prompt templates. However, you can add your own customizations to refine each search operation.  

## Prompt Templates
Most of the prompt is taken care for you by Ziggy. We currently support the following standard prompt templates.

- SQL searches - this covers most databases and data warehouses that support SQL.
- Elastic Search
- Hubspot

When configuring a new search, you should select a Default from the Prompt Template dropdown and then press **Replace Template** to insert it.

You will see the following ##tokens## in the prompt template. You should not remove these without good reason. These are replaced with actual values when the prompt executes.

- ##query##
- ##fields##
- ##customizations##

and additionally for SQL queries

- ##sql dialect##
- ##sql schema##
- ##sql table##

You are free to edit the prompt template as you wish. It will not be overwritten unless your press the **Replace Template** button again.

You are generally safer to put your customizations in the Customizations tabs as these are not overwritten if you replace the template later.

## Customizations
This where you add your own additional instructions. These are added to whatever is in the prompt template when your Flow executes.

## Tester
This lets you test and arbitrary query. It will return the generated query in the pane below. By using this, you can test and refine your prompt configuration.

## Debugging the Flow
You can use Ziggy's [debugging](/user-guide/editor/Debugging.md) features to run the Flow and inspect edge data for further testing.

