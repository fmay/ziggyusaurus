---
title: Cluster Levels
---

We will refer to these levels in the documentation. They indicate whether your cluster is intended for scale, high-availability or both.

## Level 1
Ziggy runs in a Docker container. By default, one of these runs the database and Redis. This is fine for scaling, but not for high-availability. If the container running the database and redis fails, Ziggy will fail. 

## Level 2
For high-availability, you will need to operate separate clusters for the database and Redis.

You can configure these using managed services (AWS RDS, Redis Cluster etc.) or your own clusters. You point to these in the `.env` file on each Ziggy server.

Your own DevOps person can configure these or our Professional Services can do this for you. Poorly configured services will impact Ziggy's performance, so ensure that these services are 'close' to your Ziggy servers.

```dotenv
APP_DATABASE=postgresql://ziggy:ziggy@db:5432/ziggy
TENANT_DATABASE=postgresql://ziggy:ziggy@db:5432/ziggy_tenant
REDIS=redis://:ziggy@redis:6379
```
