---
title: Collector Block
---

# Collector

The Collector Block has one main purpose and one secondary purpose.

![Collector](/img/flows/blocks/core/block-collector.png)

- It acts as a gathering point for the completion of prior Blocks. It won't pass data onwards until all incoming edge data is populated.
- You can set the **Sleep** value so it also waits the specified amount of time before passing execution to subsequent Blocks.

