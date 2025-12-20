---
title: Flow Import and Export
---

You can manage the import and export of flows using

`ziggy flow export`
`ziggy flow import`


This is very useful for 

- Automating the migration of flows from one Ziggy instance to another.
- Committing to a Git repo for point-in-time snapshots

## Export

### Tags or Flow UUIDs
You can export using a list of flow uuids and/or a list of tags. 

Using tags is often beneficial so you do not have to manage long lists of uuids. For example. you might tag your production flows with `production` and then perform an export with `ziggy export --server FiendlyName --tags production --file-path /some/local/path/file.json`. 

### What is exported

If a Flow references Connections or Secrets, then these are export, too. However, Secrets do not have their secret data exported. This means you will need to ensure that your secret is properly configured when you import to a new Ziggy instance. This actual configuration can be done after the import.

**Important** : If your Connection contains a value that *should* really be stored as a secret, then this value will be exposed in the export. For this reason, it is always good practice to reference secrets from the Connection configuration.

### Export command

`ziggy flow export --server FriendlyName [--no-prompt] [--flow-ids uuid1 uuid2] [--tags 'tag1' 'tag2'] --save-path /some/local/path/file.json`

Note the use of the `--no-prompt` option. You will want to use this in automation scenarios to prevent the confirmation prompt from running.

It is advisable to always use `--server` to be specific about which server you are exporting from.

If you specify neither `flow-ids` not `--tags`, all flows will be exported.


### Response data

The result stats is returned as JSON to `stdout`. All other messages are written to `stderr`.

Any errors will be stored in the returned JSON object.

## Import

It is important to understand how the import command works as you can specify how existing flows are handled.

When migrating regularly from development to production, you will usually want to overwrite existing flows. As a 'just-in-case', all flows that are overwritten will first have a [named save](/user-guide/editor/Named-Saves.md) **Pre import** created.

### Overwrite rules

An import will first check to see if the Flow UUID exists in the target system. If it does and you have specified `--overwrite` then it will overwrite this flow.

If there is no matching UUID (for example the first time you migrate from development to production), then it will check to see if there is a Flow with the same name. If there is, it will be overwritten.

If neither a UUID nor Name match is found, it will create a new flow.

The same rules apply for Connections and Secrets.

Overwrite behavior is specified using one of the following options

- `--skip`
- `--duplicate`
- `--overwrite`

In an automation scenario, you will generally use `--overwrite`

### Import command

`flow import --no-prompt --server FriendlyName --overwrite --file-path /some/local/path/zexport.json`

It is mandatory to specify the `--server` name. This prevents unintentional loading of data to the wrong server.

Note the use of the `--no-prompt` option. You will want to use this in automation scenarios to prevent the confirmation prompt from running.

The `--file-path` option specifies the location of a previous export file created by `ziggy flow export`.

### Response data

The import status results are returned as a JSON object to `stdout`. Detailed information for each import item.
