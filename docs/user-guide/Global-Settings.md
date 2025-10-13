---
title: Global Settings
description: Configure system-wide settings for your Ziggy platform. Complete guide to global configuration, preferences, and system administration.
keywords: [ziggy global settings, system configuration, platform administration, preferences, setup]
image: /img/ziggy-logo-light.webp
---

[TODO] Update

# Global Settings

The Global Settings dialog can be opened from the gear icon in right side of the menu bar.

Apart from **Personal**, Global settings are available to Admin users only.

## Personal
Currently, this only lets you log out. More coming soon.

## Flows

<img src="/img/global-settings/gsettings-flow.png" alt="Flows" width="800" />

- **Default Flow timeout** - before Flows throw a timed out error. This can be overridden for an individual Flow in the Flow settings.
- **Default Execution Log Level** - please refer to [History log levels](/user-guide/History-data-storage-levels).
- **Execution Log Retention (hours)** - how long data remains in the execution history before being flushed automatically. This deletion is performed hourly. Please note that for data to be fully removed from the database a Full Vacuum or Scheduled Vacuum should be performed (see below).
- **Flush execution history** - allows you to flush all execution history items before the specified date and time. You can also flush in a more selective manner from the [Dashboard](/user-guide/editor/Execution-history).

**IMPORTANT** - note that flushed data will remain in the database until you perform a database reorganisation. This can be done

- In the Housekeeping section in these Global Settings.

## Queues
Manage your Queues.

<img src="/img/global-settings/gsettings-queues.png" alt="Queues" width="800" />

- **Add a Queue** - you can queue Flow execution by selecting the Queue in the [Receiver Block](/user-guide/block-types/core/Receiver).
- **Rate limit** - this will ensure that Flows are executed according to a per second rate limit value you specify here. This feature works across all Flows that use the same Queue ensuring you never exceed the target API's ceiling value.
- **Alert threshold** - if the queue size ever exceeds this value and alerts are enabled for queues, then this will be logged and an alert notification sent. See [Alerts](Alerts) for more details.
- **Delete queue** - the delete icon lets you delete a Flow. You should be careful when deleting a queue as any Flow using this Queue will fail.

## Security

<img src="/img/global-settings/gsettings-security.png" alt="Security" width="800" />

### External execution tokens
A token must be used when external systems [call the Ziggy API to launch a flow](/user-guide/Launching-flows).

- **+Execution token** - this will generate a new random token. You will be shown it one time only.
- **Rename token** - if, for example, you want to assign tokens to an individual or group, you can rename the token to make it clear who it belongs to. This is useful when revoking a token.
- **Revoke token** - press the trash icon to revoke the token. Once revoked, it cannot be restored.

### IP Whitelist
Coming soon.

## Alerts
This lets set alert options and thresholds. Please read the [Alerts](Alerts) topic for full details on alerts and the alert log.

<img src="/img/global-settings/gsetting-alerts.png" alt="Alerts" width="800" />

## Users

<img src="/img/global-settings/gsettings-users.png" alt="Users" width="800" />

Add Users, their roles and whether they should receive [alerts](Alerts). 

## Export

<img src="/img/global-settings/gsettings-export.png" alt="Export" width="800" />

This exports a JSON representation of the system (except for execution history). Secrets are exported without exposed values.

This is in preparation for a corresponding import feature that will let you selectively import entities into a new Ziggy instance.

## System Logs
You can conveniently view system logs.

<img src="/img/global-settings/gsettings-sys-logs.png" alt="system logs" width="800" />

You can select a log file to view from the **Log files** dropdown. This will then open up a log viewer.

<img src="/img/global-settings/gsettings-syslog-viewer.png" alt="flush log" width="800" />

## Housekeeping

<img src="/img/global-settings/gsettings-housekeeping.png" alt="Housekeeping" width="800" />

Perform a database reorganisation.

- **Full Vacuum** is the most thorough but it blocks the database until completed.
- **Standard Vacuum** does not block the database but will slow it down. It removes records flagged for deletion and reindexes.

Please note that these operations can take a long time and are bets performed during periods of relative inactivity.

### DB Backup
You can specify a schedule for backing up the database. 

The backup files will be created in the ```volume-data/backups``` folder and will be of the format ```ziggy_dump_20250118_133746.dump```.

You should configure you ```docker-compose.yaml``` file to persist to some location in the host. You might want to set up some extra automation to copy these backups to an S3 Bucket or other location in case your host dies and backup data is lost.

### Auto Vacuum
You can specify a schedule for performing a Full Vacuum on the database. This can be useful for the following reasons.

- Keep your database optimised for performance reasons.
- Security - if you have configured the [Execution History](/user-guide/editor/Execution-history) to store errored or full execution history, this will ensure data is fully removed from the database.

**Important** - the Scheduled Vacuum will block the database, so it should be performed at times of no activity. You should also perform this operation regularly so the amount of deletion and reorganisation required does not accumulate and therefore takes less time.

#### Auto deletion based on Retention Time
Above, in the Flows section, you can specify that Execution History data is automatically deleted after a specified number of hours. Not that this will flag such records for deletion but not actually remove them from the database. A Full Vacuum or a Scheduled Vacuum will ensure that data is fully removed.

### System Transfer
This lets you transfer your entire database to another Ziggy instance. 

- **Create Transfer File** generates the file to be transferred.
- **Load Transfer File** restores this into the target Ziggy instance.

Please refer to [Transferring Data](Transferring-Data) for more information.

## System Monitor
[TODO] screenshot and explanation