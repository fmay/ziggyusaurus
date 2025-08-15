---
title: Core Blocks
---

# Core Blocks

Core blocks are the fundamental building blocks of Ziggy flows. They provide essential flow control, data processing, and execution capabilities.

## Flow Control Blocks

- [Receiver](/user-guide/block-types/core/Receiver) - Accept incoming data and requests
- [Terminator](/user-guide/block-types/core/Terminator) - End flow execution
- [Branch](/user-guide/block-types/core/Branch) - Conditional flow routing
- [Branch-To-Subflow](/user-guide/block-types/core/Branch-To-Subflow) - Call subflows conditionally
- [Subflow](/user-guide/block-types/core/Subflow) - Reusable flow components

## Data Processing Blocks

- [Iterator](/user-guide/block-types/core/Iterator) - Loop through data collections
- [Joiner](/user-guide/block-types/core/joiner) - Combine multiple data streams
- [Splitter](/user-guide/block-types/core/Splitter) - Divide data into multiple streams
- [Merger](/user-guide/block-types/core/Merger) - Merge data from multiple sources
- [Collector](/user-guide/block-types/core/Collector) - Gather data from multiple inputs
- [Batch-End](/user-guide/block-types/core/Batch-End) - Control batch processing

## Data Management Blocks

- [Variable-Set-Get](/user-guide/block-types/core/Variable-Set-Get) - Set and retrieve variables
- [Has-Data](/user-guide/block-types/core/Has-Data) - Check if data exists
- [Key-Filter](/user-guide/block-types/core/Key-Filter) - Filter data by keys

## Execution Blocks

- [Javascript](/user-guide/block-types/core/Javascript) - Execute custom JavaScript code
- [Console-Message](/user-guide/block-types/core/Console-Message) - Output debug messages
- [Commander Block](/user-guide/block-types/core/commander-block) - Execute system commands

## Utility Blocks

- [Annotation](/user-guide/block-types/core/Annotation) - Add documentation to flows
- [Test Data](/user-guide/block-types/core/test-data) - Generate test data
- [Sinkhole](/user-guide/block-types/core/sinkhole) - Discard unwanted data

## Block Combinations

Core blocks are designed to work together seamlessly. Common patterns include:

- **Data Flow**: Receiver → Processing → Output
- **Conditional Logic**: Branch → Different Paths → Merger
- **Batch Processing**: Iterator → Processing → Batch-End
- **Error Handling**: Try → Catch → Error Processing

## Best Practices

- Use Receiver blocks as entry points
- Implement proper error handling with conditional logic
- Use Subflows for reusable functionality
- Document flows with Annotation blocks
- Test flows with Test Data blocks
