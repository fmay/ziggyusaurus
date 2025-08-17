---
title: Monitoring
---

# Execution History Dashboard

The Execution History Dashboard lets you monitor Flow executions. 

Depending on your Global Settings and Flow Settings, you can also examine the data snapshot and edge data for an individual Flow execution.

**Important** : for secure environments, you can set whether snapshot data is stored or not at the system or Flow level. 
Please read the [next topic](History-data-storage-levels.md) for more information.

![Dashboard](/img/flows/dashboard/flows-dashboard-1.png)
 
## Filters
Select any combination of filters in the left pane to narrow down the execution history list.

Terminator Status and Flows selections can be individually deselected by clicking on them again.

## Stats
The right hand pane shows the execution history information, reflecting the current filters.

At the top is key statistical information.

## Deleting
Press the trash icon to delete the execution history for the current filters.

## Examining an execution
You can click on any execution history item in the list. This will load the Flow snapshot and, if present, will show you the full execution log and edge data.

This is especially useful for diagnosing errored executions. In the above screenshot you can see how there is a fatal error. If you click on it, the Flow will load with the data snapshot.

![fatal history item](/img/flows/dashboard/fatal-history.png)

- Note how the edge after the first data has data on it but no other edges do. Clearly the Flow failed in the Javascript Block.
- Examine the log pane to see more information. If you click on the log row, a data viewer will appear.

![Log row data](/img/flows/dashboard/log-row-data.png)
