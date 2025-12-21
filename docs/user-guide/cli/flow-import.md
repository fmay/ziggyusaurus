---
title: Flow Import
---

When migrating regularly from development to production, you will usually want to overwrite existing flows. As a 'just-in-case', all flows that are overwritten will first have a [named save](/user-guide/editor/Named-Saves.md) **Pre import** created.

## Overwrite rules

An import will first check to see if the Flow UUID exists in the target system. If it does and you have specified `--overwrite` then it will overwrite this flow.

If there is no matching UUID (for example the first time you migrate from development to production), then it will check to see if there is a Flow with the same name. If there is, it will be overwritten.

If neither a UUID nor Name match is found, it will create a new flow.

The same rules apply for Connections and Secrets.

Overwrite behavior is specified using one of the following options

- `--skip`
- `--duplicate`
- `--overwrite`

In an automation scenario, you will generally use `--overwrite`

## Database Backup

In order to mitigate accidental imports, Ziggy will automatically create a database backup before importing. 

If you want to prevent this, use the `--no-backup` option.

## Import command

`flow import --no-prompt --server FriendlyName --overwrite --no-backup --file-path /some/local/path/zexport.json`

It is mandatory to specify the `--server` name. This prevents unintentional loading of data to the wrong server.

Note the use of the `--no-prompt` option. You will want to use this in automation scenarios to prevent the confirmation prompt from running.

The `--file-path` option specifies the location of a previous export file created by `ziggy flow export`.

## Response data

The import status results are returned as a JSON object to `stdout`. Detailed information for each import item is returned.

```json
{
  "status": 201,
  "statusText": "Created",
  "data": {
    "flowsProcessed": [
      {
        "uuid": "c4492541-118e-4e23-9450-f2d28204ebee",
        "name": "SMS Test",
        "result": "OVERWRITE",
        "matchMethod": "uuid",
        "isProcessed": true
      }
    ],
    "connectionsProcessed": [
      {
        "uuid": "417c5997-296e-4e7d-b482-7c899406041f",
        "name": "Twilio",
        "result": "OVERWRITE",
        "matchMethod": "uuid",
        "isProcessed": true
      }
    ],
    "secretsProcessed": []
  }
}
```
