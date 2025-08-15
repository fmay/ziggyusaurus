---
title: Utility Blocks
---

# Utility Blocks

Utility blocks provide specialized functionality for common integration and data processing tasks. These blocks extend Ziggy's capabilities beyond the core flow control features.

## Data Storage Blocks

- [Data Store](/user-guide/Data-Store-section) - Persistent key-value data storage
- [Memory Store](/user-guide/block-types/utility/MemStore) - High-performance in-memory storage

## File and Data Operations

- [File Reader/Writer](/user-guide/block-types/utility/file-reader-writer) - Read and write files from various sources
- [Mapper](/user-guide/block-types/utility/Mapper) - Transform and map data between formats

## Database Operations

- [SQL](/user-guide/block-types/utility/SQL) - Execute SQL queries and operations
  - [SQL Configuration](/user-guide/block-types/utility/sql/sql-configuration) - Database connection setup
  - [SQL Mapping](/user-guide/block-types/utility/sql/sql-mapping) - Data mapping for SQL operations
  - [SQL Select](/user-guide/block-types/utility/sql/sql-select) - Query data from databases
  - [SQL Insert](/user-guide/block-types/utility/sql/sql-insert) - Insert data into databases
  - [SQL Update](/user-guide/block-types/utility/sql/sql-update) - Update existing database records
  - [SQL Upsert](/user-guide/block-types/utility/sql/sql-upsert) - Insert or update database records
  - [SQL Delete](/user-guide/block-types/utility/sql/sql-delete) - Remove data from databases
  - [SQL Raw](/user-guide/block-types/utility/sql/sql-raw) - Execute custom SQL statements
  - [SQL Editing](/user-guide/block-types/utility/sql/sql-editing) - Edit and modify SQL queries

## External Integrations

- [REST Call](/user-guide/block-types/utility/REST-Call) - Make HTTP API calls to external services
- [Airtable](/user-guide/block-types/utility/airtable) - Integrate with Airtable databases

## Monitoring and Logging

- [Audit](/user-guide/block-types/utility/audit) - Comprehensive audit logging and tracking

## Use Cases

Utility blocks are essential for:

- **Data Integration**: Connecting to external databases and APIs
- **File Processing**: Reading and writing files from various sources
- **Data Transformation**: Converting data between different formats
- **Monitoring**: Tracking operations and maintaining audit trails
- **Storage**: Managing data persistence and caching

## Configuration

Most utility blocks require configuration:

- **Connections**: Database and API connection settings
- **Authentication**: API keys, credentials, and security tokens
- **Mapping**: Data structure and field mappings
- **Scheduling**: When and how often operations should run

## Best Practices

- Use appropriate storage blocks for different data types
- Implement proper error handling for external API calls
- Configure audit logging for compliance requirements
- Test database operations with small datasets first
- Monitor performance and optimize queries as needed
