---
title: Splitter Block
---

# Splitter Block

The Splitter Block is a core block type that divides incoming data streams into multiple outputs. It enables parallel processing and data distribution across different flow paths.

## Overview

The Splitter Block is responsible for:
- Dividing data into multiple streams
- Enabling parallel processing
- Distributing data across different paths
- Maintaining data integrity during splitting

## Configuration

Splitter blocks can be configured with various options including:
- Output path configuration
- Data distribution rules
- Filtering conditions
- Performance optimization settings

## Usage

Splitter blocks are typically placed after data sources to distribute data to multiple processing paths.

## Related Blocks

- [Merger](/block-types/core/Merger) - For combining data streams
- [Joiner](/block-types/core/joiner) - For joining related data
- [Collector](/block-types/core/Collector) - For gathering data from multiple sources

## Use Cases

- **Parallel Processing**: Split data for simultaneous processing
- **Data Distribution**: Route data to different systems
- **Load Balancing**: Distribute workload across multiple paths
- **Conditional Routing**: Send data to different paths based on conditions

## Best Practices

- Ensure all split paths have proper termination
- Monitor performance of parallel processing paths
- Use appropriate filtering for data distribution
- Consider data volume when splitting streams
