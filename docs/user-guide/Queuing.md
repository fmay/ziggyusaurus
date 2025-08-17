---
title: Queuing
---

# Queuing
Ziggy operates its own background queuing mechanism for all Flows. 
This ensures that the system is not overloaded with requests.

However, it is often necessary to use a user defined queue to stay within API rate limits.

## Define Queues
You can define your Queues in [Global Settings](Global-Settings).

![Queue settings](/img/flows/queueing/queue-settings.png)

Generally, you might use the following strategy if you were integrating Hubspot with Microsoft Dynamics.

- Define a **General** queue for miscellaneous Flows.
- Define a **Hubspot** queue for all Flows that access the Hubspot Api, (which has rate limiting, typically 10 requests per second).
- Define a **Dynamics** queue for Flows making calls to Microsoft Dynamics.

## Rate limits
You can assign a rate limit to a Queue by clicking on the Queue in Global Settings.

<img src="/img/flows/queueing/queue-settings-edit.png" alt="Queue settings" width="450" />

## Assigning a Flow to a Queue
You can assign a request to a Queue within the Receiver Block. If no Queue is specified, the Flow will execute immediately. Otherwise, the Flow will be added to the chosen Queue and then processed by the Queue Worker.

<img src="/img/flows/queueing/queues-receiver.png" alt="Receiver" width="400" />

The queue worker processes any jobs found in the queue on an FIFO basis. 

## Monitoring and pausing Queues
You can access Queue stats from Queue menu bar. You can also pause and restart queues.

![Queue monitor](/img/flows/queueing/queues-menu.png)

## Security
Users with the most stringent security requirements may be concerned about any form of data persistence.

Queuing persists the data by default. Ziggy uses Redis for queue management and it is set to persist queues by default.

You can disable this in ```redis.conf``` if you are running Ziggy solo.