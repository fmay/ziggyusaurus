---
title: Batch-End Block
---

# Batch-End Block

The Batch-End Block is a core block type that controls batch processing workflows. It marks the end of a batch and can trigger batch completion actions, making it essential for processing large datasets efficiently.

## Overview

The Batch-End Block is responsible for:
- Marking the end of batch processing
- Triggering batch completion actions
- Managing batch state and progress
- Providing batch processing control
- Handling batch completion logic

## Configuration

Batch-End blocks can be configured with various options including:
- **Batch Size**: Number of items to process per batch
- **Completion Actions**: What to do when a batch completes
- **Progress Tracking**: Monitor batch processing progress
- **Error Handling**: How to handle batch failures
- **Batch State**: Manage batch processing state

## Batch Processing Workflow

### 1. Batch Initialization
```javascript
// Start a new batch
const batchSize = 100;
batch(batchSize);
consoleMsg(`Started batch processing with size: ${batchSize}`);
```

### 2. Data Processing
```javascript
// Process items in the batch
for (let i = 0; i < data.length; i++) {
    // Process individual item
    const processedItem = processItem(data[i]);
    
    // Add to batch
    batchAdd(processedItem);
}
```

### 3. Batch Completion
```javascript
// End the current batch
batchEnd();
consoleMsg('Batch completed successfully');
```

## Batch Control Methods

### Batch Management
- **`batch(size)`**: Start a new batch with specified size
- **`batchAdd(item)`**: Add an item to the current batch
- **`batchEnd()`**: Complete the current batch
- **`batchGet()`**: Get current batch information
- **`batchClear()`**: Clear current batch data

### Progress Tracking
- **Batch Count**: Number of items in current batch
- **Total Processed**: Total items processed across all batches
- **Batch Number**: Current batch sequence number
- **Processing Status**: Current batch processing state

## Use Cases

### Data Processing
- **Large Dataset Processing**: Handle datasets too large for memory
- **Database Operations**: Process database records in batches
- **File Processing**: Process files in manageable chunks
- **API Calls**: Make API calls in batches to avoid rate limits

### Performance Optimization
- **Memory Management**: Control memory usage during processing
- **Resource Optimization**: Optimize resource utilization
- **Parallel Processing**: Enable parallel batch processing
- **Load Balancing**: Distribute processing load

### Error Handling
- **Batch Recovery**: Recover from batch processing failures
- **Partial Success**: Handle partially successful batches
- **Retry Logic**: Implement retry mechanisms for failed batches
- **Fallback Processing**: Provide alternative processing paths

## Configuration Examples

### Basic Batch Processing
```javascript
// Simple batch processing
const batchSize = 50;
batch(batchSize);

data.forEach(item => {
    const processed = processItem(item);
    batchAdd(processed);
});

batchEnd();
```

### Advanced Batch Processing
```javascript
// Advanced batch with error handling
const batchSize = 100;
const maxRetries = 3;

try {
    batch(batchSize);
    
    for (let item of data) {
        try {
            const processed = processItem(item);
            batchAdd(processed);
        } catch (error) {
            consoleMsg(`Error processing item: ${error.message}`);
            // Continue with next item
        }
    }
    
    batchEnd();
    consoleMsg('Batch completed successfully');
    
} catch (error) {
    consoleMsg(`Batch failed: ${error.message}`);
    // Handle batch failure
}
```

### Progress Tracking
```javascript
// Track batch progress
const totalItems = data.length;
const batchSize = 100;
let processedCount = 0;

batch(batchSize);

for (let item of data) {
    const processed = processItem(item);
    batchAdd(processed);
    processedCount++;
    
    // Log progress
    if (processedCount % 10 === 0) {
        const progress = (processedCount / totalItems * 100).toFixed(1);
        consoleMsg(`Progress: ${progress}% (${processedCount}/${totalItems})`);
    }
}

batchEnd();
consoleMsg(`Completed processing ${processedCount} items`);
```

## Best Practices

### Batch Size Selection
- **Memory Constraints**: Choose batch size based on available memory
- **Processing Time**: Balance batch size with processing time
- **Error Recovery**: Consider error recovery when setting batch size
- **System Resources**: Account for system resource limitations

### Error Handling
- **Individual Item Errors**: Handle errors for individual items
- **Batch-Level Errors**: Manage errors that affect entire batches
- **Recovery Strategies**: Implement recovery mechanisms
- **Logging**: Log all errors and recovery actions

### Performance Monitoring
- **Batch Timing**: Monitor batch processing times
- **Resource Usage**: Track memory and CPU usage
- **Throughput**: Measure items processed per second
- **Bottlenecks**: Identify performance bottlenecks

## Related Blocks

- [Iterator](/block-types/core/Iterator) - For looping through data
- [Javascript](/block-types/core/Javascript) - For custom batch logic
- [Collector](/block-types/core/Collector) - For gathering batch results
- [Merger](/block-types/core/Merger) - For combining batch outputs

## Integration Patterns

### With Iterator Block
```javascript
// Use with Iterator for structured processing
const iterator = createIterator(data, batchSize);

while (iterator.hasNext()) {
    const batch = iterator.next();
    processBatch(batch);
    batchEnd();
}
```

### With Collector Block
```javascript
// Use with Collector to gather results
const results = [];

batch(batchSize);
data.forEach(item => {
    const result = processItem(item);
    batchAdd(result);
    results.push(result);
});

batchEnd();
return results;
```
