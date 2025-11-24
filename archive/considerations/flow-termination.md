---
title: Flow termination
---

Each Flow must have at least one [Terminator Block](../../docs/user-guide/block-types/core/Terminator.md). Whenever the Terminator Block is executed, the Flow will immediately end.

Note that if the Terminator has multiple edges connected to its input port, the Block will not execute until all incoming edges have data (an empty array is considered data for this purpose).

## Sinkhole Block
You may want to make use of the [Sinkhole Block](../../docs/user-guide/block-types/core/sinkhole.md). This will not terminate the Flow, but it gracefully stops execution of that branch of the Flow. This is often used in conjunction with error condition where a Block allows you to output errors to a second edge.

