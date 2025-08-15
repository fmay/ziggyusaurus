---
title: Error Handling
---

# Error Handling

If a Flow encounters an error, the following happens.

- If the Terminator has blocks connected to the Error output connector, this Flow will be executed.
- If the errored part of the Flow contains an [Audit block](/user-guide/block-types/utility/audit) then the error will be written to the audit log. 
This is only important if you are performing [External Auditing](/user-guide/Auditing).
- An entry is written to the [Execution History](/user-guide/editor/Execution-history).
- The reason for failure is written to the UI log (if launched from the UI).

## Error handler
If you connect blocks to the error edge, then you should terminate that portion of the Flow with a [Sinkhole](/user-guide/block-types/core/sinkhole) block.

<img src="/img/flows/error-handling/error-handling.png" alt="Error handling" width="700" />
