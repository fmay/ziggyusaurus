---
title: AI Search
---

This is the most important AI related Block. It handles the translation of a natural language query
into a platform specific query.

The output of the Block is a query that the Block's prompt has translated into the query object for
the search Block that will follow.

Take a look at this part of a search Flow. This is taking a natural language query and then performs
a search on a SQL database.

![Edge data](/img/flows/blocks/ai/ai-search-flow-example.png)

If you click on the edge bubble, you will see the following.

![Edge data](/img/flows/blocks/ai/ai-search-flow-edge-from-prompt.png)

You can see the prompt has output the `sql` key with the generated SQL for the query itself asl well
as a count query.

## Block Configuration

### Model
You need to specify a [Models Connection](/user-guide/Connections.md) that this block uses for prompt execution. Having done this, select the model you want to use. ChatGPT 4.1 Mini is usually very good.

When adding a new Connection, from the **Type** dropdown, be sure to choose an LLM type (ChatGPT, Cohere etc.)

### Database
If you are connecting to a SQL database or warehouse, then check the box and provide the connection details. You will need to have defined a database connection in [Connections](/user-guide/connections) first.

You should click the **Load Fields** button so Ziggy can perform a table discovery and populate the Fields section (see below).

### Prompt
The real power of this Block is the Prompt. This is described in detail below.

### Other settings
These value can usually be ignored unless you see a specific need to set them. Some of these values will be ignored by certain LLM models.

### Fields
If this is not a SQL search (you have not checked **Use database**), then you should press the **Paste Fields Config** button. For this to work, you should first go the Block that has a corresponding **Copy Fields Config** button (Elastic Ingest for example). This takes that Block's fields and puts them on the clipboard. You can then paste them for final tweaking.

Check the fields that you want to use in the query. You can also use the **Prompt helper** field to provide assistance to the LLM model for non-obvious field meanings that the LLM may not figure out for itself. For example in a Movies database, there may be a field **avg_vote**. You could enter **Rating** if you think the user is likely to query with something like *find me the movie with the highest rating*. 

## Detailed Prompt Configuration

Engineering the prompt is the most important part of search. Ziggy provides you with default prompt templates. However, you can add your own customizations to refine each search operation.

### Prompt Templates
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

### Customizations
This where you add your own additional instructions. These are added to whatever is in the prompt template when your Flow executes.

![Customizations](/img/flows/blocks/ai/ai-prompt-customization.png)


### Tester
This lets you test and arbitrary query. It will return the generated query in the pane below. By using this, you can test and refine your prompt configuration. Below are the test results for an Elastic query.

![Customizations](/img/flows/blocks/ai/ai-prompt-tester.png)


## Debugging the Flow
You can use Ziggy's [debugging](/user-guide/editor/Debugging.md) features to run the Flow and inspect edge data for further testing.

