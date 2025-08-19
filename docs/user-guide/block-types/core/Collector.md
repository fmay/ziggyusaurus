---
title: Collector Block
description: Learn how to use the Collector block in Ziggy flows for gathering data from multiple sources. Complete guide with examples and configuration options.
keywords: [ziggy, collector, core blocks, flows, no-code, data collection, aggregation]
image: /img/ziggy-logo-light.webp
---

# Collector

The Collector Block has one main purpose and one secondary purpose.

![Collector](/img/flows/blocks/core/block-collector.png)

- It acts as a gathering point for the completion of prior Blocks. It won't pass data onwards until all incoming edge data is populated.
- You can set the **Sleep** value so it also waits the specified amount of time before passing execution to subsequent Blocks.

