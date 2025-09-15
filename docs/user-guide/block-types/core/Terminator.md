---
title: Terminator Block
description: Learn how to use the Terminator block in Ziggy flows for stopping flow execution. Complete guide with examples and configuration options.
keywords: [ziggy, terminator, core blocks, flows, no-code, flow control, execution]
image: /img/ziggy-logo-light.webp
---

# Terminator

The Terminator Block will end a Flow as soon as it has edge data on all incoming edges.

If you want to stop execution without actually stopping the Flow, you should use the [Sinkhole Block](sinkhole.md).

<img src="/img/flows/blocks/core/terminator-block.png" alt="Terminator" width="300" />

## Send data in response
If the Flow is [launched via the API](user-guide/Launching-flows.md) (as opposed to the editor) and you want to 
return the data arriving at the Terminator, then you should check 
the **Send data in response** box.

If the Terminator has multiple incoming edges, each edge will be represented in the 
response as shown below.

```javascript
{
    "data0": "OK",
    "data1": [
        {
          hubspot_id: '125005142222'
        },
        {
          hubspot_id: '125005142215'
        }
    ]
}
```

<div class="keywords">terminate</div>
<div class="ai-info">At least one Terminator should be in a Flow</div>
