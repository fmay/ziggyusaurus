---
title: Queuing
---

## System Queue

Ziggy operates its own background queuing mechanism for all Flows. This ensures that the system is
not overloaded with requests.

All Flows will first be placed into the System Queue before being released for execution.

You can set the number of parallel Flow executions using the `MAX_CONCURENT_JOBS` parameter in your
`.env` file. This is 10 by default.

Flows will be released for execution immediately up to `MAX_CONCURENT_JOBS`. Thereafter, they will
be queued and released as Flows complete.

The only way to circumvent the system queue is when [launching Flows from an external API call](user-guide/Launching-flows.md). However, this should not be abused in high volume situations as system overload protection is bypassed.

## User Defined Queue

It is often helpful to use a user defined queue to stay within API rate limits. You can define these
in Ziggy from [Global Settings](Global-Settings).

![Queue settings](/img/flows/queueing/queue-settings.png)

Queues are applied globally and work across all your Flows.

### Defining a Queue

You can manage queues and assign rate limits for each queue by clicking on the Queue section in Global Settings.

<img src="/img/flows/queueing/queue-settings-edit.png" alt="Queue settings" width="450" />


### Using a Queue from a Block

You specify that a Block should use a Queue. This will then place that block into the queue when it executes.

<img src="/img/flows/queueing/queue-block-set.png" alt="Queue settings" width="350" />

- Click in the Block header on the **?** icon.
- Select the Queues Tab

<img src="/img/flows/queueing/queue-define.png" alt="Queue settings" width="450" />

- Choose (or remove) the queue from the dropdown. 
- If a queue is selected, you will see a red **Q** icon in the header, as shown above.

## Monitoring

You can access Queue stats from Queue menu bar.

![Queue monitor](/img/flows/queueing/queues-menu.png)

## Security & Performance

Queues are never persisted to disk, they are retained in memory. As a result, you should be aware that queues with a large number of entries can impact memory usage, although it would usually requre a large overflow to cause problems.

