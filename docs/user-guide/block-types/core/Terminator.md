---
title: Terminator Block
---

# Terminator Block

The Terminator Block is a core block type that ends flow execution. It provides a clean way to terminate flows and can be used for error handling or normal completion.

## Overview

The Terminator Block is responsible for:
- Ending flow execution cleanly
- Providing exit status information
- Handling flow completion scenarios

## Configuration

Terminator blocks can be configured with various options including:
- Exit status codes
- Completion messages
- Error handling options

## Usage

Terminator blocks are typically placed at the end of a flow to handle completion or error scenarios.

## Related Blocks

- [Receiver](/block-types/core/Receiver) - For starting flows
- [Branch](/block-types/core/Branch) - For conditional flow control
- [Error Handling](/error-handling/Error-Handling) - For error management

## Use Cases

- **Normal Completion**: End flows after successful execution
- **Error Termination**: Stop execution when errors occur
- **Flow Control**: Provide clean exit points for subflows
- **Status Reporting**: Return completion status to calling systems

## Best Practices

- Use Terminator blocks at the end of all flow paths
- Provide meaningful exit status codes
- Include completion messages for debugging
- Consider error scenarios when designing flows
