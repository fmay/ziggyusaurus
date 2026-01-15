---
title: MQTT and Internet of Things (Beta)
---

You can configure message handling from the Messaging dialog. The available messaging options are currently

- AWS IoT Core
- Generic MQTT messaging

![mqtt messaging](/img/flows/messaging/mqtt-edit-config.png)

## Topic -> Flow association

Ziggy will receive messages for the specified configuration as a Subscriber. When it receives messages, it looks up the topic in the Topic Flows list and then launches the selected Flow.

The payload is passed into that Flow, where it can be processed.

Each messaging configuration can be associated with one or more topics. 

## Publishing Messages
Please refer to the [Messaging](/user-guide/Messaging) for information on how to publish messages within a Flow.