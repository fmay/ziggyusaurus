---
title: Rate Limiting
---

Ziggy supports dedicated rate-limit protection for specific platforms.

## Hubspot Blocks
Currently, all Hubspot Blocks are protected. This means that you should never exceed the imposed rate limits even if you multiple Flows are executing simultaneously..

If you would like to have rate limit protection for other platforms, please inquire.

## General Rate Limit Protection
You should use [Ziggy Queues](user-guide/Queuing.md) for general rate limit protection.

## REST Block
The [REST Block](user-guide/block-types/utility/REST-Call.md#rate-limit) also has support for rate limit protection. This is implemented at the Block level.

However, this only protects within the Flow itself. If there is any chance that Flows will execute simultaneously then you should use [Ziggy Queues](user-guide/Queuing.md).

