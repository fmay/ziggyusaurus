---
title: Subflow Block
---

# Subflow Block

The Subflow Block is a core block type that enables the creation of reusable, modular flow components. It promotes code reusability and maintainable flow design.

## Overview

The Subflow Block is responsible for:
- Encapsulating reusable flow logic
- Providing modular flow components
- Enabling flow composition and reuse
- Managing flow parameters and return values

## Configuration

Subflow blocks can be configured with various options including:
- Flow selection and reference
- Input parameter mapping
- Output handling configuration
- Error handling options

## Usage

Subflow blocks are typically used to break complex flows into manageable, reusable components that can be called from multiple locations.

## Related Blocks

- [Branch-To-Subflow](/block-types/core/Branch-To-Subflow) - For conditional subflow execution
- [Receiver](/block-types/core/Receiver) - For starting subflows
- [Terminator](/block-types/core/Terminator) - For ending subflows

## Use Cases

- **Code Reuse**: Implement common functionality once and reuse it
- **Modular Design**: Break complex flows into manageable pieces
- **Maintenance**: Update logic in one place for all instances
- **Testing**: Test individual components independently

## Best Practices

- Design subflows with clear input/output contracts
- Use descriptive names for subflow parameters
- Document subflow behavior and requirements
- Test subflows independently before integration
