---
title: Execution History Level
---

# Execution History Level

Each time a Flow executes there is the option of storing snapshot data. Snapshot data consists of

- The Flow execution log (what you see in the bottom right editor pane).
- Edge data - the data object that is stored on each edge when the Flow terminates.
- The termination status - **OK**, **Fatal**, **Timed out**.

There are two primary consideration when choosing whether to store snapshot data or not.

- **Security** - if you have strict security requirements, you may not want to store any data in the database at all - especially when running in production mode.
- **Storage space** - if you are running large numbers of executions, each snapshot will take up space in the database. So, you will often only want to store snapshot data for errored or timed-out executions.

## Specifying history snapshot levels
There are two places to specify this.

### Global default
in the [Global Settings](global-settings/Global-Settings), you can specify the default for all Flows. If an individual Flow does not specify the level, then it will use this.

![History levels](/img/flows/history-levels/gsettings-log-level.png)

### Flow Settings
Open the Flow Settings to select a snapshot level for an individual Flow.

<img src="/img/flows/history-levels/fsettings-log-level.png" alt="History levels" width="700" />

