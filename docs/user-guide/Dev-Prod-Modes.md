---
title: Dev-Prod Modes
---

# Dev/Prod Modes

## Secrets and Connections

The principle way Dev/Prod Mode operates is by referincing either the Dev or Prod version of [Secrets](user-guide/Secrets.md) and [Connections](user-guide/Connections.md).

The selected mode will then reference the required value at runtime.

## Select the mode in the editor
You can change mode by clicking the large box in the top right of the Flow editor.

![development](/img/flows/devprod/devprod-dev.png)

![development](/img/flows/devprod/devprod-prod.png)

## Select mode when launching via the API
You can also specify which mode a Flow should operate in when launching a Flow from the API. This is explained in more detail in the [Launching Flows](user-guide/Launching-flows.md) topic.

