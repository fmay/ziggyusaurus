---
title: Receiver Block
---
# Receiver

A Flow requires a single Receiver Block that acts as the entry point.

<img src="/img/flows/blocks/core/receiver/receiver-block.png" alt="Receiver" width="300" />

## Passing data to the Flow
You will often [trigger a Flow from an API call](user-guide/Launching-flows.md) and optionally 
pass data into the Flow in the REST body.

While building your Flow, you can simulate data being passed into the Flow by adding test data 
in the block as shown above.

When the Flow is launched from an API call, the test data is ignored. 

## Queue
If you want a Flow to be managed by a [Queue](user-guide/Queuing.md), specify the Queue name from the dropdown (see above image).