---
title: Receiver Block
---

# Receiver Block

The Receiver Block is a core block type that serves as the entry point for flows. It accepts incoming data and requests, making it the starting point for data processing workflows.

## Overview

The Receiver Block is responsible for:
- Accepting incoming data and requests
- Serving as the entry point for flows
- Handling different input data formats
- Initiating flow execution
- Managing input validation

## Configuration

Receiver blocks can be configured with various options including:
- **Input Type**: What type of data to accept
- **Data Format**: Expected data structure and format
- **Validation Rules**: Input validation requirements
- **Error Handling**: How to handle invalid inputs
- **Authentication**: Access control and security

## Input Types

### HTTP Requests
- **REST API**: Accept HTTP GET, POST, PUT, DELETE requests
- **Webhook**: Handle incoming webhook notifications
- **File Upload**: Accept file uploads and attachments
- **Form Data**: Process HTML form submissions

### Scheduled Triggers
- **Time-based**: Execute flows at specific intervals
- **Event-driven**: Trigger on specific system events
- **Manual**: Allow manual flow execution
- **Conditional**: Trigger based on specific conditions

### Data Sources
- **Database**: Accept data from database queries
- **File System**: Process files from various sources
- **Message Queues**: Handle messages from queues
- **External APIs**: Accept data from external services

## Usage Examples

### HTTP API Receiver
```javascript
// Configure receiver for HTTP API
{
    "type": "http",
    "method": "POST",
    "path": "/api/process-data",
    "contentType": "application/json",
    "validation": {
        "required": ["userId", "data"],
        "types": {
            "userId": "string",
            "data": "object"
        }
    }
}
```

### Scheduled Receiver
```javascript
// Configure receiver for scheduled execution
{
    "type": "scheduled",
    "schedule": "0 */6 * * *", // Every 6 hours
    "parameters": {
        "defaultData": "scheduled-execution"
    }
}
```

### File Receiver
```javascript
// Configure receiver for file processing
{
    "type": "file",
    "source": "s3://bucket/path",
    "fileTypes": ["csv", "json", "xml"],
    "maxSize": "10MB"
}
```

## Data Handling

### Input Validation
- **Required Fields**: Ensure essential data is present
- **Data Types**: Validate data type and format
- **Size Limits**: Check data size constraints
- **Content Validation**: Verify data content and structure

### Data Transformation
- **Format Conversion**: Convert between data formats
- **Structure Mapping**: Map incoming data to expected structure
- **Data Cleaning**: Remove invalid or unnecessary data
- **Normalization**: Standardize data formats

### Error Handling
- **Validation Errors**: Handle invalid input data
- **Connection Errors**: Manage external connection issues
- **Timeout Handling**: Deal with slow or hanging requests
- **Fallback Options**: Provide alternative processing paths

## Best Practices

### Security
- **Input Validation**: Always validate incoming data
- **Authentication**: Implement proper access controls
- **Rate Limiting**: Prevent abuse and overload
- **Data Sanitization**: Clean and sanitize input data

### Performance
- **Efficient Processing**: Handle data efficiently
- **Resource Management**: Manage memory and CPU usage
- **Connection Pooling**: Optimize external connections
- **Caching**: Cache frequently accessed data

### Reliability
- **Error Handling**: Implement comprehensive error handling
- **Logging**: Log all incoming requests and errors
- **Monitoring**: Monitor receiver performance and health
- **Backup Plans**: Have fallback processing options

## Related Blocks

- [Terminator](/block-types/core/Terminator) - For ending flows
- [Branch](/block-types/core/Branch) - For conditional flow control
- [Javascript](/block-types/core/Javascript) - For custom data processing
- [Variable-Set-Get](/block-types/core/Variable-Set-Get) - For managing variables

## Use Cases

- **API Endpoints**: Create REST API endpoints for external systems
- **Data Ingestion**: Accept data from various sources
- **Webhook Processing**: Handle incoming webhook notifications
- **File Processing**: Process uploaded or dropped files
- **Scheduled Tasks**: Execute flows on a schedule
- **Event Processing**: Respond to system events

## Configuration Examples

### Basic HTTP Receiver
```javascript
{
    "name": "Data Processing Receiver",
    "type": "http",
    "method": "POST",
    "path": "/process",
    "description": "Accepts data for processing"
}
```

### Advanced Receiver with Validation
```javascript
{
    "name": "Secure Data Receiver",
    "type": "http",
    "method": "POST",
    "path": "/secure/process",
    "authentication": "bearer",
    "validation": {
        "required": ["data", "timestamp"],
        "types": {
            "data": "object",
            "timestamp": "string"
        },
        "custom": "validateTimestamp"
    },
    "rateLimit": {
        "requests": 100,
        "window": "1m"
    }
}
```
