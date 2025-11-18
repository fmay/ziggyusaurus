---
title: Cluster Levels
---

We will refer to these levels in the documentation. They indicate whether your cluster is intended to be highly available. 

## Level 1
Ziggy runs in a Docker container and one of these runs the database and Redis. This is fine for scaling, but it is not suitable for high-availability.

## Level 2
For true high-availability, you will need to operate external clusters for the database and Redis.

You are free to configure these using managed services or your own clusters. You point to these in the `.env` file.

The following entries should be adjusted.

```dotenv
APP_DATABASE=postgresql://ziggy:ziggy@db:5432/ziggy
TENANT_DATABASE=postgresql://ziggy:ziggy@db:5432/ziggy_tenant
REDIS=redis://:ziggy@redis:6379
```
