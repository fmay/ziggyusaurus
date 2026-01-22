---
title: Email
---

This block sends email via an SMTP server.

<img src="/img/flows/blocks/utility/email/email-flow.webp" alt="email flow" width="700" />

The block will send an email for each array element on the incoming edge.

## Configuring

### Connection

Select an [SMTP Connection](/user-guide/Connections.md#smtp) to use.

### Fields

Generally, you should run/step the flow up to the Email block so the block has data to work with. You can then specify fields content as follows.

- Reference edge data by clicking in a field. The dropdown will show all available edge key values.
- Hard code any field by entering the value in `"your value"` (use double quotes). You can see this in the above screenshot for the Recipient field `"info@ziggyplatform.com"`.  
