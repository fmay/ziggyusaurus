---
title: Editing SQL
---

# Editing SQL

<img src="/img/flows/blocks/utility/SQL/sql-sql-edit.png" alt="Edit SQL" width="500" />

After you have checked the **Edit SQL** box, the SQL becomes editable. 
However, changes in the configuration will no longer be reflected in the SQL.

You can edit the SQL within the block, or press the **Editor** button for a popup editor. 

You should also note that any edits should confirm to the nature of the templated operation.

For example, if you have a SELECT operation and edit it to another command 
such as `DELETE FROM my_table`, it will fail.

## Practical use of editing the SQL
In practice, the most useful edits you will make are to map incoming edge data to the database table field names. 

By default, Ziggy generates an edge key token, `$$token`, with the same name as the database field name. 
This is fine is you are using [edge based mapping](/user-guide/block-types/utility/sql/sql-mapping). 

However, a quick and easy way to map is to editor the SQL to refer to the edge key name. 
For example, if you see this in the SQL ...

```SQL
INSERT INTO "test_schema"."insert-test" 
("name", "age")
VALUES
($$name, $$age)
```
...but your edge keys are `personName` and `personAge`, then you can modify the SQL to the following.

```SQL
INSERT INTO "test_schema"."insert-test" 
("name", "age")
VALUES
($$personName, $personAge)
```

If you have run the Flow up to the block so the edge has some data on it, then you can use keyboard shortcuts 
to list the values, as explained below.

## Keyboard shortcuts in the SQL editor
The following shortcuts can be used to insert tokens into the SQL.

**Important** : note that when inserted, there should be exactly two token prefix characters.

- **@** - list of all fields in the configured table
- **$** - list of all keys on the incoming edge. You should first run or step through the flow to the block so the edge has data on it.
- **#** - special token for batch and insert values. See below.

<img src="/img/flows/blocks/utility/SQL/sql-helper.png" alt="Helper" width="500" />

The screenshot shows the list of database fields appearing in the popup list.

If the popup list is truncated, which can happen when editing in the block, press the **Editor** button and edit from there.

### Special tokens
- **##batch_offset** - used in a SELECT operation, this indicates the offset, in rows, within the batch.
- **##batch_size** - the **Batch size** value specified in the configuration.
