---
title: Data Store
---

[Click here](../../docs/user-guide/Data-Store-section.md) for detailed information on the Data Store.

The Data Store is an extremely useful way of storing data in Ziggy in a key/value format. It is highly recommended to understand how and when to use this.

In summary

- You can store data in a persistent fashion within the Ziggy platform.
- It is fast.
- You can store any form of intermediate data for other Flows to access at a future point.
- You can use it to write errors and logs for manual or Flow based inspection.

## Alternatives
You may have a use case where it makes more sense to store such data in a database. In these cases, you might want to consider using the SQL block.

## Limitations and considerations
Because the Data Store data is stored in the Ziggy Postgres database, if the data store becomes very large (> 1 million records), performance will start to degrade. There are a couple of ways to mitigate this.

- Delete data when you no longer needs it. This can be done using the Data Store Block or manually in the Data Store Browser.
- Use the Reorganize button in Settings. This will fully flush deleted records from the database.

If you need to store a very large amount of data, then you can configure AWS or Azure to act as the Data Store. This will allow unlimited storage but the general performance will not be as fast as the Ziggy based Data Store.

## Memory Store
Although Ziggy provides a Memory Store Block, the Data Store is preferred in most situations, given its speed and persistence.