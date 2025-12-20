---
title: Database Maintenance
---

`ziggy system reorg --server FriendlyName --no-prompt`

This can also be manually executed from [Global Settings](/user-guide/Global-Settings.md#database-reorganization).

This will perform the following tasks.

- Remove any soft deleted data from the database
- Reindexes and reorgnizes the database for optimal performance.

This operation will slow the server down while it runs. It is recommended you run this reasonably frequently during off-peak load times.