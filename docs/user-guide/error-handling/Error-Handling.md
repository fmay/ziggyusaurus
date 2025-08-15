---
title: Error Handling
---

# Error Handling

If a Flow encounters an error, the following happens.

- If the Terminator has blocks connected to the Error output connector, this Flow will be executed.
- If the errored part of the Flow contains an [Audit block](audit.md) then the error will be written to the audit log. 
This is only important if you are performing [External Auditing](Auditing.md).
- An entry is written to the [Execution History](Execution-history.md).
- The reason for failure is written to the UI log (if launched from the UI).

## Error handler
If you connect blocks to the error edge, then you should terminate that portion of the Flow with a [Sinkhole](sinkhole.md) block.

![Error handling](error-handling.png#width=700)
