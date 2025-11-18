---
title: Cluster Levels
---

We will refer to these levels in the documentation. They determine the importance of high availability to you.


## Level 1**
Ziggy runs in a Docker container and one of these runs the database and Redis. This is fine for scaling, but it is not suitable for high-availability.

## Level 2
For true hgh-availability, you will need to operate external clusters for the database and Redis.

You are free to configure these using managed services or your own clusters. You point to these in the `.env` file on each server or in `docker-compose.yaml`
