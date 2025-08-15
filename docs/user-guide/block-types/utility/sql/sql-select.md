---
title: SELECT
---

# SELECT

There are two modes for the SELECT operation.

## Batch mode
Reads data in chunks defined by **Batch Size** and for a maximum of **Max iterations** iterations.

Setting iterations to 0 will run the batch until no more rows are available.

Refer to [Batching](/user-guide/Batching) for details about batching and the [Batch End](/user-guide/block-types/core/Batch-End) block, which is required.

<img src="/img/flows/blocks/utility/SQL/sql-select-batch.png" alt="Batch mode" width="500" />


## Edge mode
This used data on the input edge to perform fetch data using a key to denote the value to lookup in the database.

You need to specify two fields.

- **Edge key for matching** - the key on the input edge whose value will be used for the lookup.
- **DB field to match against** - they database field to use for the lookup.

<img src="/img/flows/blocks/utility/SQL/sql-select-edge.png" alt="Edge mode" width="700" />

You can see what is going on behind the scenes by looking at the generated SQL. For Postgres, it will look like this.

```SQL
SELECT "name", "age"
FROM "test_schema"."insert-test"
WHERE id IN $$id;
```

At run time, `$$id` will be replaced by the list of values referenced by **Edge key for matching**.

## Where editor
When you set a where condition, the following dialog will appear.

<img src="/img/flows/blocks/utility/SQL/sql-where.png" alt="Where editor" width="600" />

This generates the following WHERE clause.

```SQL
WHERE ("age" > 18 or "age" < 30)
```
You can also use tokens for the values ([see Editing SQL](/user-guide/block-types/utility/sql/sql-editing)) instead of literal values.

```SQL
WHERE ("age" > $$lowerValue or "age" < $$upperValue)
```
