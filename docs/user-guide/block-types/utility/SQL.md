---
title: SQL Block
---

# SQL Block

The SQL Block is a utility block type that provides comprehensive database operations capabilities. It allows you to execute SQL queries, perform data operations, and manage database connections within your Ziggy flows.

## Overview

The SQL Block is responsible for:
- Executing SQL queries and statements
- Managing database connections
- Performing CRUD operations
- Handling database transactions
- Managing data mapping and transformation

## Configuration

SQL blocks can be configured with various options including:
- **Database Connection**: Connection to target database
- **Query Type**: SELECT, INSERT, UPDATE, DELETE, etc.
- **SQL Statement**: The actual SQL query to execute
- **Parameters**: Query parameters and bindings
- **Error Handling**: How to handle database errors

## SQL Operations

### SELECT Operations
```sql
-- Basic SELECT query
SELECT id, name, email FROM customers WHERE status = 'active'

-- Complex SELECT with JOINs
SELECT c.name, o.order_date, o.total
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.order_date >= '2024-01-01'
```

### INSERT Operations
```sql
-- Single record insert
INSERT INTO customers (name, email, status) VALUES (?, ?, ?)

-- Batch insert
INSERT INTO customers (name, email, status) VALUES 
(?, ?, ?), (?, ?, ?), (?, ?, ?)
```

### UPDATE Operations
```sql
-- Update single record
UPDATE customers SET status = 'inactive' WHERE id = ?

-- Update multiple records
UPDATE customers SET last_login = NOW() WHERE status = 'active'
```

### DELETE Operations
```sql
-- Delete specific records
DELETE FROM customers WHERE status = 'inactive'

-- Delete with conditions
DELETE FROM customers WHERE last_login < DATE_SUB(NOW(), INTERVAL 1 YEAR)
```

## Data Mapping

### Input Mapping
- **Parameter Binding**: Map flow data to SQL parameters
- **Data Types**: Handle different data types appropriately
- **Null Handling**: Manage null values in queries
- **Array Processing**: Handle array data for batch operations

### Output Mapping
- **Result Structure**: Map database results to flow data
- **Column Mapping**: Map specific columns to output fields
- **Data Transformation**: Transform data during mapping
- **Error Handling**: Handle mapping errors gracefully

## Connection Management

### Database Types
- **MySQL/MariaDB**: Popular open-source databases
- **PostgreSQL**: Advanced open-source database
- **SQL Server**: Microsoft SQL Server
- **Oracle**: Oracle Database
- **SQLite**: Lightweight file-based database

### Connection Configuration
```javascript
// Database connection configuration
{
    "type": "mysql",
    "host": "localhost",
    "port": 3306,
    "database": "myapp",
    "username": "user",
    "password": "password",
    "options": {
        "connectionLimit": 10,
        "acquireTimeout": 60000
    }
}
```

## Parameter Binding

### Safe Parameter Usage
```javascript
// Use parameterized queries to prevent SQL injection
const query = "SELECT * FROM customers WHERE status = ? AND age > ?";
const params = [status, minAge];

// Execute with parameters
const result = await sqlExecute(query, params);
```

### Dynamic Query Building
```javascript
// Build dynamic queries safely
let query = "SELECT * FROM customers WHERE 1=1";
const params = [];

if (status) {
    query += " AND status = ?";
    params.push(status);
}

if (minAge) {
    query += " AND age > ?";
    params.push(minAge);
}

const result = await sqlExecute(query, params);
```

## Transaction Management

### Basic Transactions
```javascript
// Start transaction
await sqlBeginTransaction();

try {
    // Execute multiple operations
    await sqlExecute("INSERT INTO orders (customer_id, total) VALUES (?, ?)", [customerId, total]);
    await sqlExecute("UPDATE customers SET order_count = order_count + 1 WHERE id = ?", [customerId]);
    
    // Commit transaction
    await sqlCommitTransaction();
    
} catch (error) {
    // Rollback on error
    await sqlRollbackTransaction();
    throw error;
}
```

### Nested Transactions
```javascript
// Handle nested transaction scenarios
let transactionLevel = 0;

async function executeInTransaction(operations) {
    if (transactionLevel === 0) {
        await sqlBeginTransaction();
    }
    transactionLevel++;
    
    try {
        await operations();
        
        transactionLevel--;
        if (transactionLevel === 0) {
            await sqlCommitTransaction();
        }
        
    } catch (error) {
        transactionLevel--;
        if (transactionLevel === 0) {
            await sqlRollbackTransaction();
        }
        throw error;
    }
}
```

## Error Handling

### Database Errors
```javascript
try {
    const result = await sqlExecute(query, params);
    return result;
    
} catch (error) {
    if (error.code === 'ER_DUP_ENTRY') {
        // Handle duplicate key error
        consoleMsg('Duplicate record detected');
        return { error: 'duplicate', message: error.message };
        
    } else if (error.code === 'ER_NO_SUCH_TABLE') {
        // Handle missing table error
        consoleMsg('Table does not exist');
        return { error: 'missing_table', message: error.message };
        
    } else {
        // Handle other database errors
        consoleMsg('Database error:', error.message);
        throw error;
    }
}
```

### Connection Errors
```javascript
try {
    const result = await sqlExecute(query, params);
    return result;
    
} catch (error) {
    if (error.code === 'ECONNREFUSED') {
        // Handle connection refused
        consoleMsg('Database connection refused');
        // Implement retry logic or fallback
        
    } else if (error.code === 'ETIMEDOUT') {
        // Handle connection timeout
        consoleMsg('Database connection timeout');
        // Implement retry logic
        
    } else {
        // Handle other connection errors
        throw error;
    }
}
```

## Performance Optimization

### Query Optimization
```javascript
// Use appropriate indexes
const query = "SELECT * FROM customers WHERE email = ? AND status = ?";
// Ensure indexes on email and status columns

// Limit result sets
const query = "SELECT * FROM customers LIMIT 1000";

// Use specific columns instead of *
const query = "SELECT id, name, email FROM customers";
```

### Batch Operations
```javascript
// Batch insert for better performance
const batchSize = 1000;
const customers = getCustomerData();

for (let i = 0; i < customers.length; i += batchSize) {
    const batch = customers.slice(i, i + batchSize);
    const placeholders = batch.map(() => '(?, ?, ?)').join(', ');
    const query = `INSERT INTO customers (name, email, status) VALUES ${placeholders}`;
    
    const params = batch.flatMap(customer => [customer.name, customer.email, customer.status]);
    await sqlExecute(query, params);
}
```

## Best Practices

### Security
- **Parameterized Queries**: Always use parameter binding
- **Input Validation**: Validate all input data
- **Connection Security**: Use secure connection methods
- **Access Control**: Limit database user permissions

### Performance
- **Query Optimization**: Write efficient SQL queries
- **Indexing**: Use appropriate database indexes
- **Connection Pooling**: Implement connection pooling
- **Batch Operations**: Use batch operations for large datasets

### Reliability
- **Error Handling**: Implement comprehensive error handling
- **Transaction Management**: Use transactions for data consistency
- **Connection Management**: Properly manage database connections
- **Monitoring**: Monitor database performance and errors

## Related Blocks

- [Data Store](/user-guide/Data-Store-section) - For data storage operations
- [Memory Store](/user-guide/block-types/utility/MemStore) - For in-memory data
- [Mapper](/user-guide/block-types/utility/Mapper) - For data transformation
- [Javascript](/user-guide/block-types/core/Javascript) - For custom database logic

## Use Cases

- **Data Extraction**: Extract data from databases
- **Data Loading**: Load data into databases
- **Data Transformation**: Transform data during database operations
- **Reporting**: Generate reports from database data
- **Data Migration**: Migrate data between systems
- **Data Validation**: Validate data against database constraints
