---
title: Javascript Block
---

# Javascript Block

The Javascript Block is one of the most powerful and versatile core blocks in Ziggy. It allows you to execute custom JavaScript code within your flows, providing unlimited flexibility for data processing, system integration, and custom logic implementation.

## Overview

The Javascript Block is responsible for:
- Executing custom JavaScript code
- Processing and transforming data
- Integrating with external systems via APIs
- Implementing complex business logic
- Handling asynchronous operations
- Accessing system resources and connections

## Configuration

Javascript blocks can be configured with various options including:
- **Code Input**: JavaScript code to execute
- **Input Data**: Data passed to the script
- **Output Mapping**: How to handle script results
- **Error Handling**: What to do if the script fails
- **Timeout Settings**: Maximum execution time
- **Security Settings**: Script execution permissions

## Code Execution

### Basic Structure
```javascript
// Access input data
const inputData = data;

// Process the data
const processedData = processData(inputData);

// Set output data
data = processedData;
```

### Input Data Access
- **`data`**: The main data object passed to the block
- **`flowData`**: Access to flow-level variables and state
- **`connections`**: Access to configured system connections
- **`secrets`**: Access to stored secrets and credentials

### Output Data
- **`data`**: The main output data object
- **`flowData`**: Set flow-level variables
- **Return values**: Can return data directly

## Common Use Cases

### Data Transformation
```javascript
// Transform data structure
data = data.map(item => ({
    id: item.record_id,
    name: item.full_name,
    email: item.email_address
}));
```

### API Integration
```javascript
// Make HTTP requests
const response = await fetch('https://api.example.com/data', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
});
data = await response.json();
```

### Business Logic
```javascript
// Implement business rules
if (data.amount > 1000) {
    data.priority = 'high';
    data.requiresApproval = true;
} else {
    data.priority = 'normal';
    data.requiresApproval = false;
}
```

### Error Handling
```javascript
try {
    // Risky operation
    data = await processData(data);
} catch (error) {
    // Handle errors gracefully
    data.error = error.message;
    data.status = 'failed';
}
```

## System Integration

### Console Output
```javascript
// Write to console for debugging
consoleMsg('Processing data:', data);
consoleMsg('Data count:', data.length);
```

### System Logging
```javascript
// Write to system logs
sysLog.log('Info message');
sysLog.warn('Warning message');
sysLog.error('Error message');
sysLog.debug('Debug message');
sysLog.verbose('Verbose message');
```

### Flow Control
```javascript
// Control flow execution
if (data.shouldStop) {
    flowData.stopExecution = true;
}

// Set flow variables
flowData.processedCount = data.length;
```

## Security Considerations

### Code Execution Safety
- Scripts run in a sandboxed environment
- Access to system resources is controlled
- Timeout limits prevent infinite loops
- Input validation is recommended

### Best Practices
- Validate all input data
- Sanitize user-provided code
- Use parameterized queries for databases
- Implement proper error handling
- Limit script execution time

## Performance Optimization

### Efficient Code
```javascript
// Use efficient data structures
const lookup = new Map();
data.forEach(item => lookup.set(item.id, item));

// Avoid unnecessary operations
if (data.length > 0) {
    // Process data only when available
    data = data.filter(item => item.active);
}
```

### Batch Processing
```javascript
// Process data in batches
const batchSize = 100;
for (let i = 0; i < data.length; i += batchSize) {
    const batch = data.slice(i, i + batchSize);
    await processBatch(batch);
}
```

## Debugging and Testing

### Console Debugging
```javascript
// Debug output
consoleMsg('Input data:', JSON.stringify(data, null, 2));
consoleMsg('Data type:', typeof data);
consoleMsg('Data length:', Array.isArray(data) ? data.length : 'N/A');
```

### Error Handling
```javascript
// Comprehensive error handling
try {
    // Your code here
} catch (error) {
    consoleMsg('Error occurred:', error.message);
    consoleMsg('Stack trace:', error.stack);
    data.error = {
        message: error.message,
        stack: error.stack,
        timestamp: new Date().toISOString()
    };
}
```

## Related Blocks

- [Variable-Set-Get](/user-guide/block-types/core/Variable-Set-Get) - For setting and getting variables
- [Console-Message](/user-guide/block-types/core/Console-Message) - For simple console output
- [Iterator](/user-guide/block-types/core/Iterator) - For looping through data
- [Branch](/user-guide/block-types/core/Branch) - For conditional logic

## Examples

### Data Validation
```javascript
// Validate required fields
const requiredFields = ['name', 'email', 'phone'];
const missingFields = requiredFields.filter(field => !data[field]);

if (missingFields.length > 0) {
    data.validationError = `Missing required fields: ${missingFields.join(', ')}`;
    data.isValid = false;
} else {
    data.isValid = true;
}
```

### Data Aggregation
```javascript
// Aggregate data by category
const aggregated = data.reduce((acc, item) => {
    const category = item.category || 'uncategorized';
    if (!acc[category]) {
        acc[category] = { count: 0, total: 0 };
    }
    acc[category].count++;
    acc[category].total += item.value || 0;
    return acc;
}, {});

data.aggregated = aggregated;
```

## Best Practices

- **Keep scripts focused**: Each script should do one thing well
- **Use meaningful variable names**: Make code readable and maintainable
- **Implement proper error handling**: Always handle potential failures
- **Document complex logic**: Add comments for complex operations
- **Test thoroughly**: Test scripts with various data scenarios
- **Monitor performance**: Watch for performance bottlenecks
- **Follow JavaScript best practices**: Use modern ES6+ features when possible
