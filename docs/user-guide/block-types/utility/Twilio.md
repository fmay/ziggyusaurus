---
title: Twilio - SMS
---

This block sends an SMS using Twilio.

<img src="/img/flows/blocks/utility/twilio-sms/twilio-sms.webp" alt="email flow" width="700" />

The block will send an SMS message for each array element on the incoming edge.

## Configuring

### Connection

Select a [Twilio Connection](/user-guide/Connections.md#twilio) to use.

### Fields

Generally, you should run/step the flow up to the Twilio block so the block has data to work with. You can then specify fields content as follows.

- Reference edge data by clicking in a field. The dropdown will show all available edge key values.
- Hard code any field by entering the value in `"your value"` (use double quotes).
