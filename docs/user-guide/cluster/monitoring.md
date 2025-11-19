---
title: Monitoring
---

Monitoring is important for higher load scenarios.

You should pay particular attention to the System Queue overflow (on the Queues page) as this will slow overall performance and is a sign that performance needs to be adjusted or a Ziggy cluster is required.

You should also be aware of Ziggy's [Performance Tuning](/user-guide/Performance-Tuning.md) options.

## Flow Execution Monitor
The [Flow Execution Monitor](docs/user-guide/flow-execution-monitor.md) - shows you live flow throughput and key server indicators (CPU, Memory, System Queue status).

<img src="/img/cluster/flow-monitor.png" alt="flow execution monitor" width="1200" />

## System Monitor
The [System Monitor](user-guide/Global-Settings.md#system-monitor), in Global Setting provides more detail and allows performance fine-tuning.

<img src="/img/flows/blocks/core/javscript/js-system-monitor.png" alt="System monitor" width="1200" />

## Queues page
The [Queues page](/user-guide/Queuing.md) shows you key System Queue metrics as well as user queues for rate-limiting.

![Queue monitor](/img/flows/queueing/queues-menu.png)

If the **System Queue** Peak Overflow value is non-zero, this is a sign that some [performance tuning](/user-guide/Performance-Tuning.md) may be needed or another server adding to the cluster.

You can press the icon in the Peak overflow column to reset the peak value after adjusting performance values.