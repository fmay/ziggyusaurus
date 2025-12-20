---
title: System Backup
---

This can also be manually executed from [Global Settings](/user-guide/Global-Settings.md#db-backup).

Performs a full database backup to the specified path.

`ziggy system backup --server FriendlyName --no-prompt --file-path \some\local\path`

You must include a full path and file name. Use the `.gz` file extension as the returned file is compressed.

If the file exists, it will be overwritten.