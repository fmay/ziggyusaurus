---
title: Memory Store
---

# Memory Store

There are two Memory Store implementations available.

- **Simple** - this is intended for use on Ziggy deployments that only use one Ziggy server. It is very much a bare-bones implementation.
- **Redis** - for multi-server deployments or where you want access to the full range of Redis commands.

In either case, Ziggy provides an identical API, so you can switch between the two without any code changes.

If you are using Redis for advanced features, then you should address the Redis instance directly.

## Persistence
The Simple Memory Store is persistent across all Flows but is not persisted to disk. A restart will lose the Memory Store contents. If you require full persistence 

- either use the [Data Store](Data-Store.md) if performance is not a primary considerations
- or use Redis

## Memory Store Block
There block lets you handle Memory Store operations without needing to write Javascript.

- Read the [Memory Store Block topic](/user-guide/block-types/utility/MemStore).

## Standard interface for Javascript
We provide the following methods for simple use cases. You should bear in mind that the management capabilities of the Simple Memory Store are basic and do not handle persistence or out-of-memory situations. Should you require these, please use Redis.

Below is an example Flow that uses the Memory Store Block and Javascript commands that access the Memory Store. This example illustrates how timed out Memory Store keys can be refreshed.

![Example](/img/flows/example-flows/example-mem-store.png)

Note that if you are using Redis, you can still use these methods.

**Important** : all methods are asynchronous.

| Method | Description |
|--------|-------------|
| `async set(key: string, value: any, timeoutUnit: MemStoreTimeoutUnit, timeoutValue: number)` | Set a key/value pair along with optional timeout value, after which the item will be deleted.<br/>• `key` : a globally unique key<br/>• `value` : any data<br/>• `timeoutUnit` : "seconds"\|"minutes"\|"hours"\|"days"\|"never"<br/>• `timeoutValue` : timeout value in the units specified by `timeoutUnit` |
| `async get(key: string)` | Retrieve a key value pair.<br/>• `key` : the globally unique key to retrieve |
| `async delete(key: string)` | Delete a key/value pair by key name.<br/>• `key` : the globally unique key to retrieve |

## Memory Store browser
You can browse and search for data in the Data Store using the [Store Browser](/user-guide/data-browser/Data-and-Memory-Store-Browser).

## Redis
If you wish to use Redis, please contact us.

