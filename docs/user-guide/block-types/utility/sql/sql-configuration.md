---
title: Configuration
---

# Configuration

For all operations, you need to configure the following.

- **Operation** - SELECT, INSERT, UPDATE, DELETE, UPSERT
- **Database** - this is only required for certain platforms (currently Snowflake). For others, the database to connect to is specified within the Connection itself.
- **Connection** - a centrally defined [Connection](/user-guide/Connections).
- **Schema**
- **Table**
- **Fields** - to be used in the `SELECT [fields selected] FROM` clause
- **Where** - for SELECT operations
- **Order** - for SELECT operations

<img src="/img/flows/blocks/utility/SQL/sql-insert.png" alt="Config" width="900" />

When you modify the Connection, Schema and Table, the fields that depend on the modified field will be reloaded.

You should be aware that some database servers, such as Azure SQL Server, 
can sleep, so you may need to wake for the server to come online.
