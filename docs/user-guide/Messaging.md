---
title: Messaging Center
---

The Messaging Center is responsible for launching flows when emails, queue/messaging system notifications or other events are received.

We currently support the following messaging types

- Email - monitors an IMAP inbox and processes on receipt.
- Internet of Things / MQTT
- Redis Event Stream
- Redis Pub/Sub

We will shortly be releasing support for

- WhatsApp
- SMS
- AWS SQS/SNS
- Azure Service Bus, Queue Storage and Event Hubs

If you have a requirement for an alternative messaging system, please email info@ziggyservices.com.

## Main listing

Below is an example of the Messaging Center with 3 items.

<img src="/img/messaging/messaging-listing.webp" alt="mqtt publish" width="1000" />

## Configuration screen

Click on an item in the listing to bring up the configuration screen.

<img src="/img/messaging/imap.webp" alt="mqtt publish" width="1000" />

- Select a [Connection](/user-guide/Connections.md) to use.
- Enter a friendly name.
- Press the **Add Topic Flow** button to add an entry into the Topic Flows listing.
- Double-click in the Topic/Event field to provide the email, channel, stream (whatever is relevant for your messaging tyoe).
- Choose a flow that will be launched when a notification is received.
- Press **Save** when finished.

You can also update the configuration at any time. 

## Ziggy Blocks

There are blocks that are related to some of these services. 

- MQTT Publish
- Email 
- Twilio SMS

More can be added upon request.

