---
title: Javascript Block
description: Learn how to use the Javascript block in Ziggy flows for custom code execution and complex logic. Complete guide with examples and configuration options.
keywords: [ziggy, javascript, core blocks, flows, no-code, data processing]
image: /img/ziggy-logo-light.webp
---
# Javascript

The **Javascript** Block is the catch-all Block. 
It allows you to perform any task that is not covered by another block.

## In place or full screen editing
There are two Javascript editing modes. You can edit in place in the Flow.

<img src="/img/flows/javascript/js-in-place.png" alt="In place editing" width="500" />

When your code gets too large for in-place editing, then press the expand icon in the Block header.

![Full screen editing](/img/flows/javascript/js-full-screen.png)

## Inputs and Outputs

### Inputs
Data is read from the incoming edge or edges. The Block will automatically add as many output edge connectors as there are input arguments. If you provide no arguments, then the edge data will be ignored.

<img src="/img/flows/blocks/core/javscript/js-arguments.png" alt="input args" width="450" />

In the above screenshot, you can see two arguments and two corresponding input edge connectors.

### Outputs
The return structure is examined to determine how many output edge connectors should be available.

If you have a simple ```return``` statement, then an empty object is placed on a single output edge.

You can output a primitive as follows.

<img src="/img/flows/blocks/core/javscript/js-return-primitive.png" alt="return primitive" width="450" />

Or data on multiple edges.

<img src="/img/flows/blocks/core/javscript/js-return.png" alt="return statement" width="450" />

## Branching to edges
You can handle any branching logic using the ```branchTo(edgeIndexZeroBased, data)``` method.

<img src="/img/flows/blocks/core/javscript/js-branch-to.png" alt="Brnach to" width="800" />

The output connectors will automatically be validated and created as you enter the ```branchTo()``` commands.

You should not return any data using ```return {edge1: someObj}``` when usiung ```branchTo()```.

## Accessing Ziggy objects, values and methods
You can access various objects and values from the code editor. Basic auto-completion will help you find the object or value as well as available options for each one.

## Console output
You can output information to the editor's console pane (bottom left).

```JavaScript
consoleMsg('Hello', value1, value2, ...)
```

## Writing to system logs
You can also write to the Ziggy system logs. These are hourly rotated and are located in the ```/logs``` folder.

Errors are logged as follows

```JavaScript
sysLog.error(msg: string, traceInfo: string, extraData?: any)
```

All other log level calls ```.log()```, ```.warn()```, ```.debug()```, ```.verbose()``` are as follows.

```JavaScript
sysLog.log(msg: string, extraData?: any)
```

## Connections
```javascript
const connection = connections.myConnectionName
```

This will automatically select the development/production secret as determined by the [prod/dev mode](user-guide/Dev-Prod-Modes.md).

## Secrets
Secrets can be accessed as follows.

```javascript
const pw = secrets.NORTHWIND_DB_PASSWORD
```

This will automatically select the development/production secret as determined by the [prod/dev mode](user-guide/Dev-Prod-Modes.md).

## Data Store
Refer to [Data Store methods](user-guide/block-types/utility/Data-Store.md) for available methods.

```javascript
const customer = await dataStore.get(myEntity, myKey)
```

## Memory Store
Refer to [Memory Store methods](user-guide/Memory-Store.md) for available methods.

```javascript
const customer = await memStore.get(myKey)
```

## Execution IDs
You can access the following execution IDs.

```javascript
const ctr = executionCounter
const id = executionId
const externalId = externalExecutionId
```

- ```externalExecutionId``` is an optional value that can be passed into the Flow when [launched externally](user-guide/Launching-flows.md). This allows the calling system to provide a value associated with the execution for you to work with.
- ```executionCounter``` is a simple sequential counter that resets to 0 when the Ziggy server restarts. It's main purpose is debugging and is not broadly useful.
- ```executionId``` is a GUID for the individual execution. Again, the primary purpose is debugging.

## Snooze
You can use the ```snooze()``` method to pause execution for a specified number of milliseconds.

```JavaScript
await snooze(1000)
```

## Custom client objects
You will have access to certain client objects. Which ones depends on your specific Ziggy configuration.

Assuming you have Postgres, SFTP and HubSpot clients available, you can access these using.

```JavaScript
const pgClient = new clientPG(configObj)
const ftpClient = new clientSFTP(configObj)
const hsClient = new clientHubspot(configObj)
```

... where ```configObj``` is specific to each one.

## Batching
You can perform batching operations with the Javascript Block. Please refer to [Batching](user-guide/Batching.md) for general information on Batching.

![JS Batching](/img/flows/blocks/core/javscript/js-batching.png)

### Available methods

You should use the ```batch``` object, which has the the following methods.

 ```batch.isBatch()``` - tests whether the Flow is in a batch at the point the Javascript block executes.
- ```batch.begin(batchSize)``` - informs Ziggy that this is the starting point for batch operations and the size of each batch. This returns ```{offset: x, iteration: y}``` where ```x``` is the number of records processed by the batch loops so far and ```y``` is the batch iteration.
- ```batch.terminate()``` - once there is no data left to process, call this to continue execution after the [**Batch End**](user-guide/block-types/core/Batch-End.md) Block (or Terminator if there is no Batch End Block.)
- ```batch.iteration()``` - returns the batch iteration counter.
- ```batch.offset()``` - returns the current record # offset from the first batch, in other words ```batchSize * batchIterations```.

### Alerts
You can generate a custom alert. This adds an item to the [Log](user-guide/Alerts.md) and will also send an email alert.

<img src="/img/flows/javascript/javascript-alert.png" alt="Alert" width="500" />

```JavaScript
alert(alertLevel: string, message: stringe, extraData?: string)
```

The first parameter (required) should be one of the following.

- WARNING - this will not create an alert notification but it will show up in the Log.
- ALERT - generates a log entry and sends an alert notification.
- IMMEDIATE - sends an alert notifcation immediately rather than waiting for the digest notification to be sent.

The second parameter (required) is notification message.

The third, optional, parameter is any additional data you may want to add to the log. It will not appear in the notification.

## Security
Script code does not have access to the following global objects.

```JavaScript
process
console
global
require
Buffer
fs
child_process
os
net
http
crypto
vm
```

However, the script code is considered **trusted**. This means that although there is good protection from harmful script code, it should not be considered 100% safe.

We therefore advise that you give access to Flow creators with this in mind.

We plan to change the architecture for script code evaluation in the future. If this is important to you now, please contact us to discuss.

## Formatting
Prettier [TODO]

## Debugger
Ziggy offers [TODO]
