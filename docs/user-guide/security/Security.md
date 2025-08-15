---
title: Security
---

# Security

There are a few areas of security you will want to control. 

## API Security 
When calling Ziggy from an external source, you pass a secret key in the API call. These secret keys are managed in the [Global Settings](Global-Settings.md).

You can issue and revoke multiple keys. Keys are only displayed when they are created. If you lose this key then you will need to issue another one.

You can assign a name to a key for identifying an individual who might be using it. This allows you to revoke access for that person.

## Data Persistence
The only data that has to be persisted is the Flow itself as well as various configuration settings. 

It is up to you how and when you persist execution history data snapshots. By default, only errored executions will persist the snapshot data. However, snapshot data can be further refined by 

- Disabling snapshot data entirely.
- Disabling/enabling for specific Flows.
- Auto deleting snapshot data that is older than X hours/minutes.

Please review [Execution History](Execution-history.md) for details.

## Secrets
Ziggy has its own Secretes management for storing Flow internal secrets. This data is encrypted in the database.

### Queue Persistence
Queues are backed by Redis. You are able to specify whether your Queues persist or not after a restart. If you enable persistence, then you should be aware that payload data only will be persisted to disk until a queue item has been processed. 

You can specify the time after which memory data is persisted to disk. 

## Ziggy user security
Ziggy has its own internal user management in order to reduce the need for reliance on external platforms. All sensitive user information is stored fully encrypted in the database.

All communication between the Ziggy UI and the Ziggy server uses JWT web tokens.

## Logs
Ziggy does not log payload information or Flow data in the system logs unless Debug mode is enabled in [Global Settings](Global-Settings.md#security).

## Javascript Block Execution
Please refer to the [Javascript Block](Javascript.md#security) for information about security on script code.