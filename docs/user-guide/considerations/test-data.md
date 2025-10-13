---
title: Test data
---

When testing a Flow, you can simulate the data that might be passed in if the Flow is being called as a [Subflow](user-guide/block-types/core/Subflow.md) or [launched with an API call](user-guide/Launching-flows.md).

If Flows are launched from WebHook calls, then using test data means you do not have to constantly trigger events from the triggering platform while testing.

This is done by providing test data in the [Receiver Block](user-guide/block-types/core/Receiver.md).

Note that when a Flow is not run from the Ziggy UI, test data is ignored.

