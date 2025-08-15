---
title: UPDATE
---

# UPDATE

This block updates data in the database based on data on the input edge.

The example below, the incoming edge will contain an array with two 
elements with the keys `age`, `name` and `id` - populated by the Receiver's test data.

![Update](/img/flows/blocks/utility/SQL/sql-update.png){width=1200}

Notice when have specified the edge that is used for matching 
as well as the database field to be using for matching (see highlighted section).

The correct (parameterized) SQL statement will be generated to suit the target database. 
At runtime, the `id` field will be used for matching.

## Field name mapping
In the screenshot above, you can see that the edge tokens `$$name, $$age` and `$$id` are referenced.
These values are the same values as the table field names.

In many cases, your incoming edge data will not be the same as the table field names. To handle this,
there are several approaches to make this as easy as possible.

Please refer to [Edge mapping](sql-mapping) for details.

## Editing
For more complex scenarios, you can let Ziggy generate the basic query for you and then
select the **Edit SQL** box to customise. Refer to [Editing SQL](sql-editing) for details.

Note that any modifications you make are expected to confirm to the templated approach.
In practice, this means editing the `$$token` values to address the incoming edge key rather
than using other [mapping techniques](sql-mapping).

