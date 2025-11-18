---
title: Leader
---

When you start your Docker containers, the first one will become the **Leader** and is responsible for running background tasks such as [Alerts](/user-guide/Alerts.md) and [Scheduled Flows](/user-guide/Scheduled-Flows.md).

If the Leader fails then one of the other servers will take over as the Leader.

You should be aware that in a [**Level 1 cluster**](/user-guide/cluster/levels.md), if the server that fails is running the databases and Redis, then this will bring the system down. If high availability is important then you should use a [**Level 2 cluster**](/user-guide/cluster/levels.md).

