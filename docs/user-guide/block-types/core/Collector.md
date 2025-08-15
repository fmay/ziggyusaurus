---
title: Collector Block
---

# Collector Block

The Collector Block is a core block type that gathers data from multiple input sources and combines them into a single output stream. It's essential for aggregating data from various systems and sources.

## Overview

The Collector Block is responsible for:
- Gathering data from multiple input paths
- Combining data streams into unified output
- Managing data synchronization
- Handling different data formats

## Configuration

Collector blocks can be configured with various options including:
- Input path management
- Data combination rules
- Synchronization settings
- Output formatting options

## Usage

Collector blocks are typically placed before data processing or output blocks to aggregate data from multiple sources.

## Related Blocks

- [Splitter](/block-types/core/Splitter) - For dividing data streams
- [Merger](/block-types/core/Merger) - For merging related data
- [Joiner](/block-types/core/joiner) - For joining data based on relationships

## Use Cases

- **Data Aggregation**: Combine data from multiple sources
- **System Integration**: Merge data from different systems
- **Reporting**: Collect data for analysis and reporting
- **Data Consolidation**: Unify data from various inputs

## Best Practices

- Ensure all input paths are properly connected
- Monitor data synchronization timing
- Handle different data formats appropriately
- Consider memory usage when collecting large datasets
