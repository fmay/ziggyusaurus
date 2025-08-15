---
title: Block Types
---

# Block Types

Ziggy provides a comprehensive set of block types to handle various integration and data processing tasks. Each block type is designed for specific use cases and can be combined to create powerful workflows.

## Core Blocks

Core blocks provide fundamental flow control and data processing capabilities:

- [Receiver](/block-types/core/Receiver) - Accept incoming data
- [Terminator](/block-types/core/Terminator) - End flow execution
- [Javascript](/block-types/core/Javascript) - Custom code execution
- [Iterator](/block-types/core/Iterator) - Loop through data
- [Joiner](/block-types/core/joiner) - Combine data streams
- [Splitter](/block-types/core/Splitter) - Divide data streams
- [Merger](/block-types/core/Merger) - Merge multiple data sources
- [Collector](/block-types/core/Collector) - Gather data from multiple sources
- [Branch](/block-types/core/Branch) - Conditional flow control
- [Branch-To-Subflow](/block-types/core/Branch-To-Subflow) - Call subflows
- [Subflow](/block-types/core/Subflow) - Reusable flow components
- [Batch-End](/block-types/core/Batch-End) - Batch processing control
- [Variable-Set-Get](/block-types/core/Variable-Set-Get) - Variable management
- [Console-Message](/block-types/core/Console-Message) - Debug output
- [Annotation](/block-types/core/Annotation) - Add documentation
- [Commander Block](/block-types/core/commander-block) - Command execution

## Utility Blocks

Utility blocks provide specialized functionality for common tasks:

- [Data Store](/block-types/utility/Data-Store-section) - Persistent data storage
- [Memory Store](/block-types/utility/MemStore) - In-memory storage
- [File Reader/Writer](/block-types/utility/file-reader-writer) - File operations
- [SQL](/block-types/utility/SQL) - Database operations
- [REST Call](/block-types/utility/REST-Call) - HTTP API calls
- [Mapper](/block-types/utility/Mapper) - Data transformation
- [Airtable](/block-types/utility/airtable) - Airtable integration
- [Audit](/block-types/utility/audit) - Audit logging

## Integration Blocks

Platform-specific integration blocks:

- [HubSpot](/block-types/hubspot) - HubSpot CRM integration
- [Salesforce](/block-types/salesforce) - Salesforce CRM integration
- [Store Helpers](/block-types/store-helpers) - Data store utilities

## Creating Custom Blocks

Learn how to extend Ziggy with your own custom blocks:

- [Custom Utility Blocks](/customisation/custom-utility-blocks) - Building custom functionality
