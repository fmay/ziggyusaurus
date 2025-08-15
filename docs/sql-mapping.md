---
title: Edge Mapping
---

# Edge Mapping

All SQL operations need to map data from the incoming edge to database fields. 
If the edge data has the same keys as the database field names then you don't need to do anything. 
The default `$$edgeKeyName` tokens will be correct.

If, however, one or more of the edge keys are different, you will need to map data.
There are two high level ways of dealing with this.

## Token editing
Click the **Edit SQL** box in the SQL block and edit the `$$edgeKeyName` token to match the key name on the edge. This is the best approach if you have a one-off situation.

![Insert](sql-insert.png#width=700)

In the simple example above, you can see we are inserting two records into the `insert-test` table. 
The operation maps `$$name` and `$$age` from the edge to `"name"` and `"age"` in the database.

If, however, the incoming edge keys were called `personName` and `personAge` 
then you can map these by checking the **SQL Edit** box and changing the tokens to `$$personAge` and `$$personAge`.

## Edge based mapping
This approach is better if you regularly encounter edge data of the same structure. See [Structures, validation, mapping and transformations](Structures-and-mapping.md) 
where there is also a video overview and detailed explanation of the mapping process.

### Generate mapping object
What can be especially helpful is using the **Generate mapping object**. This will generate a Zod validation object
based on the database fields and types.

![Field object in select](sql-select-generate-mapping-object.png#width=500)

After pressing the button, you will see the following auto-generated object.

![Field object](sql-mapping-object.png#width=600)

You can then add this as a standard Structure, which can be used in this block and any others.



