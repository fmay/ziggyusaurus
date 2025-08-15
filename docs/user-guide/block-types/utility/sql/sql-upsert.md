---
title: UPSERT
---

# UPSERT

This block **upserts** data using the data available on the input edge.

The example below shows the incoming edge with `age`, `name` and `id` populated by the Receiver's test data.

The `id` field for each imcoming array element is be used to perform lookups in this example. 
If the id exists, the record will be updated, otherwise a new record will be inserted. 

<img src="/img/flows/blocks/utility/SQL/sql-upsert.png" alt="Upsert" width="1200" />

Notice when have specified the edge key `id` that is used for matching
as well as the database field `id` used for matching.

The correct SQL statement will be generated to suit the target database. We have shown both a Postgres 
and a SQL Server example. It doesn't really matter to you as a user, but it's worth noting the different 
syntax that's being used in the background.

## Field name mapping
In the screenshot above, you can see that the edge tokens `$$name, $$age` and `$$id` are referenced.
These values are the same values as the table field names.

In many cases, your incoming edge data will not be the same as the table field names. To handle this,
there are several approaches to make this as easy as possible.

Please refer to [Edge mapping](/user-guide/block-types/utility/sql/sql-mapping) for details.

## Editing
For more complex scenarios, you can let Ziggy generate the basic query for you and then
select the **Edit SQL** box to customise. Refer to [Editing SQL](/user-guide/block-types/utility/sql/sql-editing) for details.

Note that any modifications you make are expected to confirm to the templated approach.
In practice, this means editing the `$$token` values to address the incoming edge key rather
than using other [mapping techniques](/user-guide/block-types/utility/sql/sql-mapping).

