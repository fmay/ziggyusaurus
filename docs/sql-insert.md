---
title: INSERT
---

# INSERT

Inserts data into the database based on data on the input edge.

The example below, the imcoming edge will contain an array of two elements, 
each of which contains `age` and `name`. We've used the Receiver's test data to illustrate this.

As a result, two records will be inserted into the `insert-test` table.

![Insert](sql-insert.png#width=700)

## Field name mapping
In the screenshot above, you can see that the edge tokens `($$name, $$age)` is generated. 
These values are the same values as the table field names.

In many cases, your incoming edge data will not contain the correct field names. To handle this, 
there are several approaches to make this as easy as possible. 

Please refer to [Edge mapping](sql-mapping.md) for details.

## Editing
For more complex scenarios, you can let Ziggy generate the basic query for you and then 
select the **Edit SQL** box to customise. Refer to [Editing SQL](sql-editing.md) for details.

Note that any modifications you make are expected to confirm to the templated approach. 
In practice, this means editing the `$$token` values to address the incoming edge key rather 
than using other [mapping techniques](sql-mapping.md).

