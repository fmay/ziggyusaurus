---
title: Data Store
---

# Data Store

The Data Store is a key/value store that is used for temporary storage of data. 
It is especially useful in migrations or situations where you need to store data somewhere that gets used in a subsequent Flow.

## Platform Settings

### Internal
This stores data inside the Ziggy database. 
It is intended for scenarios where the total number of keys stores is in the hundreds of thousands. 
When this gets too large, the performance will slow down. 

### AWS
This uses AWS DynamoDB to store data. As a result, it is infinitely scalable and can contain any 
number of keys. When running Ziggy Solo, you will need to configure the following environment variables.

- `DATA_STORE_AWS_REGION=your_aws_region`
- `DATA_STORE_AWS_ACCESS_KEY=your_access_key`
- `DATA_STORE_AWS_SECRET=your_secret`

### Azure
We will shortly be adding support for CosmosDB for anyone running Ziggy Solo on Azure.

## Name and Key
The data store is a Key/Value store but it also provides an additional field **```name```** so you can create a namespace for your data. 

The combination of **```name + key```** must be unique within the store.

## Data Store Block
The [Data Store Block](Data-Store.md) gives you access to Data Store operations without the need to write any Javascript code.

## Javascript API
You can also perform Data Store operations from the Javascript Block. The following methods are available.

**Important** : all methods are asynchronous.

| Method | Description |
|--------|-------------|
| `fetch(fetchProps)` | Retrieve keys using `fetchProps` whose type definition includes:<br/>• `limit` : maximum records to retrieve<br/>• `offset` : offset from start<br/>• `flowUuid` : flow's unique id (optional)<br/>• `key` : keyname (optional)<br/>• `name` : namespace name (optional)<br/>• `data` : search for data (currently exact match only, optional) |
| `async findName(name: string, limit: number, offset: number)` | Retrieve all keys within the specified namespace.<br/>• `limit` : maximum keys to retrieve<br/>• `offset` : relative to this offset value |
| `findNameKey(name: string, key: string)` | Retrieve the specified key within the specified namespace.<br/>• `name` : namespace<br/>• `key` : key |
| `insert(name: string, key: string, data: any)` | Insert a new key into the specified namespace. Will error if the namespace+key combination already exists.<br/>• `name` : namespace<br/>• `key` : key |
| `upsert(name: string, key: string, data: any)` | Insert a new key into the specified namespace if it doesn't exist, update if it does.<br/>• `name` : namespace<br/>• `key` : key |
| `updateOneNameKey(name: string, key: string, data: any)` | Update a key/value pair in the specified namespace.<br/>• `name` : namespace<br/>• `key` : key<br/>• `data` : data to store |
| `deleteOneNameKey(name: string, key: string)` | Delete a key/value pair in the specified namespace.<br/>• `name` : namespace<br/>• `key` : key |

## Data Store browser
You can browse and search for data in the Data Store using the [Store Browser](Data-and-Memory-Store-Browser.md). 
This works for **Internal** mode only.
