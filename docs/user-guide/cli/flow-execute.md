---
title: Flow Execute
---

Executes flows from the specified list of flow uuids and/or a list of tags. The following are common use cases.

- To run tests that flows are executing properly **before** migrating from a development Ziggy instance to a production instance.
- To run tests that flows are executing properly **after** migrating from a development Ziggy instance to a production instance.
- For general flow automation where it is easier to use the CLI than trigger flows using API calls.

`ziggy flow execute  [--server FriendlyName] [--no-prompt] {--flow-ids uuid1 uuid2 | --tags 'tag1' 'tag2'} [--payload json] [--do-not-queue] [--parallel]`

## Payload

The `--payload` option should be supplied as JSON if the flow you are executing expects data.

In this case, you will probably run in combination with one (or possibly a few related) flow ids.

## No Prompt

Use `--no-prompt` in automation scenarios to avoid execution being interrupted by a confirmation prompt.

## Flow IDs and Tags
You must specify either one or more flow ids, or one or more tags.

## Do not queue

`--do-not-queue`

This can be important in testing scenarios. It forces Ziggy to bypass the System Queue and execute the flow immediately.

The advantage of this is that the return data you get will the the actual flow output data. If you do not get this, you will get a `201` indicating the the flow was successfully added to the queue.

## Parallel

This should be used when you want all flow to be executed simultaneously.

## Returned Data

The results are written to stdout in this format

```json
[
  {
    "flowUuid": "e5b20a86-7933-4b4c-8d8f-c2a913599498",
    "status": 201,
    "statusText": "Created",
    "data": {
      "flowStatus": "FATAL",
      "data": null
    }
  },
  {
    "flowUuid": "d2ac2377-f118-47d2-a585-413089d0d5b4",
    "status": 201,
    "statusText": "Created",
    "data": {
      "flowStatus": "SUCCESS",
      "data": {
        "a": 1,
        "b": 2
      }
    }
  }
]
```

You should inspect the `data` key for detailed response information. 

If a flow fails, you will see `"flowStatus": "FATAL"`.

If the flow succeeds and returns data, inspect the `data.data` key.