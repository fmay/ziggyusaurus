---
title: Configuration
---

# Configuration

For all operations, you need to configure the following.

## Operation
The following operations are supported:

- **SELECT** - Performs a SQL Select operation. [docs](sql-select.md)
- **INSERT** - Performs a SQL Insert operation. [docs](sql-insert.md)
- **UPDATE** - Performs a SQL Update operation. [docs](sql-update.md)
- **UPSERT** - Performs a SQL Upsert operation. [docs](sql-upsert.md)
- **DELETE** - Performs a SQL Delete operation. [docs](sql-delete.md)
- **RAW** - Executes a raw SQL query. [docs](sql-raw.md)
- **EDGE** - Executes the SQL found on the incoming edge. This is often used when receiving data from the [AI Prompt Block](/user-guide/block-types/ai/ai-search-prompt.md). [docs](sql-edge.md)

## Other Settings
- **Connection** - a centrally defined [Connection](/user-guide/Connections).
- **Schema**
- **Table**
- **Database** - this is only required for certain platforms (currently Snowflake). For others, the database to connect to is specified within the Connection itself.
- **Fields** - to be used in the `SELECT [fields selected] FROM` clause
- **Where** - for SELECT operations
- **Order** - for SELECT operations

<img src="/img/flows/blocks/utility/SQL/sql-insert.png" alt="Config" width="900" />

When you modify the Connection, Schema and Table, the fields that depend on the modified field will be reloaded.

You should be aware that some database servers, such as Azure SQL Server, 
can sleep, so you may need to wake for the server to come online.

<div class="keywords">sql, select, insert, update, upsert, delete, edge, raw</div>
<div class="ai-info">Handles all SQL read, write, update, upsert and raw query operations</div>