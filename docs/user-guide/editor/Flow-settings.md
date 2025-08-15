---
title: Flow settings
---

# Flow settings

![Flow settings](/img/flows/flow-settings.png){width=500}

## Identifier
Each Flow has a unique id. This is the value you will need to used when [launching flows via an API call](/user-guide/launching/Launching-flows).

## API Launch URL
Press this button to paste the URL that [external systems should use to launch the Flow](/user-guide/launching/Launching-flows). 

## Flow name
The Flow name.

## Tags
These are really useful if you have a lot of Flows and want to be able to find them using tag 
filtering in the [Flows listing](Flows-listing).

## Timeout
A Flow will be aborted if this period is exceeded. It will be ignored if stepping though flows in the UI.

## Execution history level
Execution History is useful for debugging when things go wrong and when building new Flows. 

Read the [Execution History topic](Execution-history) for full configuration details. 

## Subflow
Check the box to allow this Flow to be called from another Flow.

## Commander
Identifies this as a [Commander Flow](Commander).