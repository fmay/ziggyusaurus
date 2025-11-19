---
title: Performance Tuning & Monitoring
---

You can adjust the system performance by adjusting the following values in the [System Monitor](user-guide/Global-Settings.md#system-monitor) section of Global Settings.

- Maximum concurrent flows
- Maximum system queue size
- Javascript Worker Pool size
- You can also run a [multi-server configuration](/user-guide/cluster/overview.md) 

<img src="/img/flows/blocks/core/javscript/js-system-monitor.png" alt="System monitor" width="1200" />

## Maximum concurrent flows
The nuber of flows that can execute simultaneously on the server. The default is 10, but you can increase this significantly higher if required. 

The impact on system resources will depend on what your flows do and how resource intensive they are. Generally speaking, memory is not heavily impacted unless your flow makes heavy use of the Memory Store block.

## Maximum system queue size
To protect against system overload, Ziggy uses a System Queue for all Flows Executions. The only exception to this is an [externally launched Flow](user-guide/Launching-flows.md#do-not-queue) where the `doNotQueue` query parameter is set.

If a flow is invoked and the number of currently active flows exceeds Maximum concurrent flows, it will be added to the system queue. This is a memory based queue that store the flow job metadata. If no data is passed into the flow then this will be very small (~1KB).

If you are passing in large payloads, then the impact on memory will be related to the size of this payload and the number of flows that are queued. The default value is 100, but you can increase this as you require. 

## System queue overflow
Once the system queue is full, flows will be persisted to the database. The throughput will drop somewhat once the overflow is being used. If the overflow size gets too large, it is a clear sign that you need to adjust **Maximum concurrent flows**, **Maximum system queue size** or add another server to a [Ziggy cluster](docs/user-guide/cluster/overview.md).

## Javascript workers
Javascript Block code is executed in isolated worker processes. Ziggy manages a pool of workers. By default the pool size is 20 but you can increase this in the [System Monitor](user-guide/Global-Settings.md#system-monitor).

## Monitoring
There are two ways to monitor the load and the flow throughput.

- In the [System Monitor](user-guide/Global-Settings.md#system-monitor) section of Global Settings.
- From the [Flow Execution Monitor](/user-guide/flow-execution-monitor.md). 

You can also configure [Alerts](user-guide/Alerts.md) if system resource limits are exceeded.

## Load Testing
For many customers and use-cases, load will not be a problem. However, for higher workloads, Ziggy's [integrated Load Testing](user-guide/Global-Settings.md#load-test) utility lets you test performance under varying levels of load.

Adjusting the above settings in combination will help you find the best settings for your flows. 