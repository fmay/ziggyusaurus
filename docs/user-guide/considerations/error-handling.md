---
title: Error Handling
---

Flows can throw errors in two general areas

- Block based errors
- Edge based validation, transformation or mapping errors

## Block errors
If an error is thrown in a Block, some Blocks offer a checkbox "Output errors to second edge", allowing you to explicitly trap them. You can then ignore them or use Blocks on the error edge to log somewhere (Data Store, SQL table etc.).

You can also use the output ports of the Terminator Block to handle errors.

If an error is thrown in a Block that does not provide an error port, then the Flow will terminate with an error.

## Edge based errors
The [edge configuration dialog](user-guide/Structures-and-mapping.md) offers various ways of dealing with errors so that the Flow does not terminate with an error.

