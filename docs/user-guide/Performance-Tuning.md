---
title: Performance Tuning & Monitoring
---

Ziggy does not require a great deal of performance tuning. However, there are two things can be adjusted.

## System Queue
To protect against system overload, Ziggy uses a System Queue for all Flows Executions. The only exception to this is an [externally launched Flow](user-guide/Launching-flows.md#do-not-queue) where the `doNotQueue` query parameter is set.

By default, Ziggy will execute 10 Flows simultaneously. This value can be changed by altering the `MAX_CONCURENT_JOBS` value in the `.env` file.

## Javascript workers
Javascript Block code is executed in isolated worker processes. Ziggy manages a pool of workers. By default the pool size is 5.

There are two ways to modify this.

- Alter `JS_WORKER_POOL_SIZE=5` in the `.env` file.
- Update the Pool Size value in the [System Monitor](user-guide/Global-Settings.md#system-monitor).

## Monitoring
You can [monitor the current system usage](user-guide/Global-Settings.md#system-monitor)

You can create [Alerts](user-guide/Alerts.md) if usage limits are exceeded.

## Load Testing
Ziggy has an [integrated Load Testing](user-guide/Global-Settings.md#load-test) utility that lets you test the system performance and load with individual Flows.