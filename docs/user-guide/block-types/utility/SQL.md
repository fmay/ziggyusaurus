---
title: SQL Block
---

# SQL

This Block supports the following databases and data warehouses.

- Postgres
- SQL Server
- Snowflake
- MySQL (coming soon)
- Other databases can be added on request. Please email [info@ziggyservices.com](mailto:info@ziggyservices.com) if you'd like to add a new database.

The following SQL operations are supported with the query generator, 
but you can edit the generated SQL if required.

- SELECT
- INSERT
- UPDATE
- DELETE
- UPSERT
- DELETE
- RAW

## SQL injection attacks 
All operations are parameterized to avoid SQL injection attacks.

## Mapping data for field names
All operation modes assume that the data coming into the block has key names that match the database field names. 
As this is frequently not the case, you will need to transform data into the correct format.

Ziggy offers several ways to deal with this as [explained in the Edge Mapping topic](sql-mapping.md). 

## Overriding SQL
By default, the SQL is not editable. As you change the configuration, the SQL is automatically generated.

If you want to customise the query, then you can check the **Edit SQL** box. From this point onwards, 
changing the configuration will not alter the SQL.

Refer to [SQL Editing](sql-editing.md) for details.

