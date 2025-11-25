---
title: Overview
---

It is recommended you read the [Feature Summary](docs/etl/etl-features.md) to get a general understanding of the most important Ziggy features.

## Before you start
A few pointers before you start building your first flow.

- Check out the [Flow Editor](/user-guide/editor/Editor.md) section.
- A flow must have a [Receiver block](/user-guide/block-types/core/Receiver.md) as the entry point and a [Terminator block](/user-guide/block-types/core/Terminator.md) do terminate the flow.
- Blocks in a flow path must be connected. You can leave them unconnected if they are not connected to a flow path. Use the [Sinkhole](/user-guide/block-types/core/sinkhole.md) block to stop a Flow branch without terminating the flow.
- Make use of test data in the Receiver block.
- Your flows can be [launched using API calls](/user-guide/Launching-flows.md) as well as the Ziggy UI.
- Use [Subflows](/user-guide/block-types/core/Subflow.md) for reusable functionality
- Document flows with [Annotation blocks](/user-guide/block-types/core/Annotation.md) and the [Information sidebar](/user-guide/editor/Flow-documentation.md).
- The [Javascript](/user-guide/block-types/core/Javascript.md) block is [AI supported](/user-guide/block-types/core/Javascript.md#ai-assistant), so even if you are not a developer you can perform custom data transformations.
- Use the [debugger](/user-guide/editor/Debugging.md) to debug and to step through your flows one block at a time.
