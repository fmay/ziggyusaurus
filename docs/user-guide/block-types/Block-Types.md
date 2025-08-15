---
title: Block Types
---

# Block Types

Ziggy provides a comprehensive set of block types to handle various integration and data processing tasks. Each block type is designed for specific use cases and can be combined to create powerful workflows.

## Core Blocks

Core blocks provide fundamental flow control and data processing capabilities:

- [Receiver](/user-guide/block-types/core/Receiver) - Accept incoming data
- [Terminator](/user-guide/block-types/core/Terminator) - End flow execution
- [Javascript](/user-guide/block-types/core/Javascript) - Custom code execution
- [Iterator](/user-guide/block-types/core/Iterator) - Loop through data
- [Joiner](/user-guide/block-types/core/joiner) - Combine data streams
- [Splitter](/user-guide/block-types/core/Splitter) - Divide data streams
- [Merger](/user-guide/block-types/core/Merger) - Merge multiple data sources
- [Collector](/user-guide/block-types/core/Collector) - Gather data from multiple sources
- [Branch](/user-guide/block-types/core/Branch) - Conditional flow control
- [Branch-To-Subflow](/user-guide/block-types/core/Branch-To-Subflow) - Call subflows
- [Subflow](/user-guide/block-types/core/Subflow) - Reusable flow components
- [Batch-End](/user-guide/block-types/core/Batch-End) - Batch processing control
- [Variable-Set-Get](/user-guide/block-types/core/Variable-Set-Get) - Variable management
- [Console-Message](/user-guide/block-types/core/Console-Message) - Debug output
- [Annotation](/user-guide/block-types/core/Annotation) - Add documentation
- [Commander Block](/user-guide/block-types/core/commander-block) - Command execution

## Utility Blocks

Utility blocks provide specialized functionality for common tasks:

- [Data Store](/user-guide/block-types/Data-Store-section) - Persistent data storage
- [Memory Store](/user-guide/block-types/utility/MemStore) - In-memory storage
- [File Reader/Writer](/user-guide/block-types/utility/file-reader-writer) - File operations
- [SQL](/user-guide/block-types/utility/SQL) - Database operations
- [REST Call](/user-guide/block-types/utility/REST-Call) - HTTP API calls
- [Mapper](/user-guide/block-types/utility/Mapper) - Data transformation
- [Airtable](/user-guide/block-types/utility/airtable) - Airtable integration
- [Audit](/user-guide/block-types/utility/audit) - Audit logging

## Integration Blocks

Platform-specific integration blocks:

- [HubSpot](/block-types/hubspot) - HubSpot CRM integration
- [Salesforce](/block-types/salesforce) - Salesforce CRM integration
- [Store Helpers](/user-guide/block-types/store-helpers/store-helpers) - Data store utilities

## Creating Custom Blocks

Learn how to extend Ziggy with your own custom blocks:

- [Custom Utility Blocks](/customisation/custom-utility-blocks) - Building custom functionality
