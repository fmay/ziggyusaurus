--- 
title: Protected Server
---

If you are running a [**Level 1 cluster**](/user-guide/cluster/levels.md), one of your server containers will be running the database and Redis servers. In this case, you can add the environment variable (in the `docker-compose` file or the `.env` file) `NO_PROCESS_FLOWS=true`.

This is only required for high load scenarios and usually when 3 or more servers in your cluster. It will prevent that server from executing flows, leaving it free for the database and Redis.

If you are running a [**Level 2 cluster**](/user-guide/cluster/levels.md) (database and Redis are in external clusters of their own) then you do not need to protect your servers.

