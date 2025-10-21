---
title: Queuing & Rate Limiting
---

Ziggy supports dedicated rate-limit protection in a couple of ways.

## Rate Limiting
### Hubspot Blocks
Currently, all Hubspot Blocks are protected. This means that you should never exceed the imposed rate limits even if you multiple Flows are executing simultaneously.

### General Rate Limit Protection
You should use [Ziggy Queues](user-guide/Queuing.md) for general rate limit protection.

### REST Block
The [REST Block](user-guide/block-types/utility/REST-Call.md#rate-limit) also has support for rate limit protection. This is implemented at the Block level.

However, this only protects within the Flow itself. If there is any chance that Flows will execute simultaneously then you should use [Ziggy Queues](user-guide/Queuing.md).


## Queues
There are two types of queues.

- **System Level Queue** : all Flows are automatically placed in this queue to prevent system overload.
- **User Defined Queue** : the best way to apply rate limit protection for 3rd party (or internal) services, often REST API calls.

Please refer to [Queuing](user-guide/Queuing.md) for full details.