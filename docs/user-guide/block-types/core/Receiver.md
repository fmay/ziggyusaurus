---
title: Receiver Block
---
# Receiver

A Flow must have a single Receiver Block that acts as Flow's entry point.

<img src="/img/flows/blocks/core/receiver/receiver-block.png" alt="Receiver" width="300" />

## Passing data to the Flow
You will often [trigger a Flow from an API call](user-guide/Launching-flows.md). You may also 
pass data to the Flow in the REST body, which will be received by this Receiver Block.

## Test data
While building your Flow, you can simulate data being passed into the Flow by adding test data 
in the block as shown above.

When the Flow is launched from an API call, the test data is ignored. 

## Webhooks
3rd party systems will often launch a Flow using a Webhook. The Webhook can pass data to the Flow in the same way. Using the Test data is an efficient way of testing your Flow without having to make changes in the originating platform.   

## Queue
If you want a Flow to be managed by a [Queue](user-guide/Queuing.md), specify the Queue name from the dropdown (see above image).

Note that certain platforms (HubSpot, SalesForce) have automatic rate-limit protection, so you do not need to use q Queue for this purpose.

<div class="keywords">webhook, entrypoint, start, required</div>
<div class="ai-info">Must be present in a Flow.</div>