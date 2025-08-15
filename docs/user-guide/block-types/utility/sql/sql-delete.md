---
title: DELETE
---

# DELETE

This block deletes records based on a key fields in the input edge. It is assumed that one of the keys 
contains an `id` type value that is used in the WHERE clause.

<img src="/img/flows/blocks/utility/SQL/sql-delete.png" alt="Delete" width="700" />

In the above example, you can see that the incoming data (supplied by the test data in the Receiver) contains two ids.

At runtime, these will be inserted into the `IN (...)` list.

## Editing SQL
You can perform more aggressive forms of deletion by checking the **Edit SQL** box and then
entering something like.

```SQL
DELETE FROM "test_schema"."insert-test"
WHERE id>=1;
```

It will not perform a delete operation without a WHERE clause. The following will fail.

```SQL
DELETE FROM "test_schema"."insert-test"
```