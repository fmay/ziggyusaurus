---
title: Transferring Data
---

# Transferring Data

You will usually encounter the situation where you are working on Flows in one Ziggy instance and want to transfer them to another.

- You are working on Ziggy source code and want to move the entire database to production.
- You are working on Flows locally on behalf of a client and want to move Flows, Secrets, Connections and Variables to their development or production platform.

Ziggy lets you handle both of these situations.

## Entire database
This is a "kitchen sink" transfer of the entire database to another Ziggy instance. You can manage this process from [Global Settings](/user-guide/Global-Settings.md#housekeeping) - **System Transfer**.

![System transfer](/img/global-settings/gsettings-housekeeping.png)

**Important** - please note the following.

- The target platform's database will be disabled when restoring data, so UI access an integrations will not be available.
- If you have a large database (a lot of Execution History and Log content) then you should consider a) running a [Full Vacuum](/user-guide/Global-Settings.md#housekeeping) b) a Purge All in the [Logs](/user-guide/Global-Settings.md#) c) deleting [Execution History](/user-guide/editor/Execution-history) .

### Create Transfer File
Press this button in your source Ziggy instance. 

The script ```trasfer-out.sh``` is executed that, by default, generates a ```ziggy.transfer``` file in the ```volume-data/transfer``` folder.

In the default scenario, you should copy ```ziggy.transfer``` to the ```volume-data/transfer``` folder in your target instance before pressing **Load Transfer File** in the target Ziggy instance to load it.

### Customising the transfer file process
You can modify this script to place the generated file in another location. For example, you might want your script to upload it to an SFTP server or an AWS S3 bucket or directly to the ```volume-data/transfer``` folder on your target instance.

Below is an excerpt from the default script. You should place any modifications after the indicated line.

```bash
# Define the file name with timestamp
OUTPUT_FILE="$ROOT_PATH/ziggy.transfer"

# Run the pg_dump command with the dynamic file name
pg_dump -U ziggy -h "$HOST" -p "$PORT" -Fc "$DB" -f "$OUTPUT_FILE"

####### CUSTOM MODIFICATIONS CAN GO HERE #########
```

### Load Transfer file
Pressing this button will load ```ziggy.transfer``` in the ```volume-data/transfer``` of the target Ziggy instance.

It does the following.

- Creates a backup database dump ```volume-data/transfer/ziggy.pretransfer.backup```. In the worst case, this file can be renamed to ```ziggy.transfer``` to reload it should the process fail.
- Renames the existing Ziggy database (```ziggy_dev``` or ````ziggy_prod```) to ```ziggy_transfer_save```. This will contain the same contents as ```volume-data/transfer/ziggy.pretransfer.backup``` but is a regular Postgres database.
- Creates a new, empty Ziggy database (```ziggy_dev``` or ````ziggy_prod```) 
- Loads ```volume-data/transfer/ziggy.transfer``` into the database.
- Deletes ```volume-data/transfer/ziggy.pretransfer.backup```

If the load aborts after the Ziggy database has been emptied, you will need to use ```psql``` to rename ```ziggy_transfer_save``` back to ```ziggy_dev``` or ````ziggy_prod``` and then restarting the server.

## Selected items
In many cases, rather than transferring the whole database, you will want to transfer selected Flows, Secrets, Connections, Variables and Structures to another Ziggy instance.

