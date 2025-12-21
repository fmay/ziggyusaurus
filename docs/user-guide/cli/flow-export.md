---
title: Flow Export
---

You can manage the import and export of flows using

`ziggy flow export`
`ziggy flow import`


This is very useful for 

- Automating the migration of flows from one Ziggy instance to another.
- Committing to a Git repo for point-in-time snapshots

## Tags or Flow UUIDs
You can export using a list of flow uuids and/or a list of tags. 

Using tags is often beneficial so you do not have to manage long lists of uuids. For example. you might tag your production flows with `production` and then perform an export with `ziggy export --server FiendlyName --tags production --file-path /some/local/path/file.json`. 

## What is exported

If a Flow references Connections or Secrets, then these are export, too. However, Secrets do not have their secret data exported. This means you will need to ensure that your secret is properly configured when you import to a new Ziggy instance. This actual configuration can be done after the import.

**Important** : If your Connection contains a value that *should* really be stored as a secret, then this value will be exposed in the export. For this reason, it is always good practice to reference secrets from the Connection configuration.

## Export command

`ziggy flow export --server FriendlyName [--no-prompt] [--flow-ids uuid1 uuid2] [--tags 'tag1' 'tag2'] --save-path /some/local/path/file.json`

Note the use of the `--no-prompt` option. You will want to use this in automation scenarios to prevent the confirmation prompt from running.

It is advisable to always use `--server` to be specific about which server you are exporting from.

If you specify neither `flow-ids` not `--tags`, all flows will be exported.


## Response data

The result stats is returned as JSON to `stdout`. All other messages are written to `stderr`.

Any errors will be stored in the returned JSON object.