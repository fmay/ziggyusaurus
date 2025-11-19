---
title: Overview
---

A Ziggy cluster addresses your scalability and high availability requirements.

<img src="/img/cluster/flow-monitor.png" alt="flow execution monitor" width="800" />

## Before you create your cluster
You should be familiar with the performance tuning settings before you add instances. This will help you tune your instances which still applies when running multiple servers.

## Load Testing
Ziggy comes with its own [load testing](user-guide/Global-Settings.md#load-test) feature that lets you experiment with different load scenarios and system settings.

It is important to understand how to adjust the main settings that will influence performance on a single server. You can make these adjustments and immediately see the impact when running a load test.

## Scaling
A single Ziggy server can handle large numbers of simultaneously executing flows. However, if you are dealing with very high load, then creating a cluster is the answer.

## Redundancy
There are different ways to configure your cluster for high-availability scenarios. See the [Levels page](/user-guide/cluster/levels.md).

## Load Balancing
You will need to configure a load balancer to point to the servers in your cluster.



