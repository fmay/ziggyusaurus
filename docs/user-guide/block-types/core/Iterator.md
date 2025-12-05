---
title: Iterator
description: Learn how to use the Iterator block in Ziggy flows for looping through data arrays. Complete guide with examples and configuration options.
keywords: [ziggy, iterator, core blocks, flows, no-code, data processing, loops, arrays]
image: /img/ziggy-logo-light-bg.webp
---

# Iterator
Iterates over an array pointed to by the **Iterator path** field.

![Iterator](/img/flows/blocks/core/iterator/block-iterator.png)

The usual case does not require you do specify any values for **Iterator key** or **Parent fields to include**, in which case it will

- iterate over the array on the inpput edge
- it will pass on the whole (nth) element of the array to the output edge.

## Input key
If you specify this, then it assume that the key you pint to contains an array.

## Parent fields to include
Specifying this lets you limit the data that is passed to the output edge. If you have an array of object where each object contains 200 keys and you only need to pass on ```object_id``` and ```name``` then you would enter a comma separated list such as ```object_id, name```.

The output edge will then contain two keys.

- **parent** contains the specified **Parent fields** (or the entire object if empty)
- **element** contains the input edge's array element

## Batch End
Do not forget to add a **Batch End** block to terminate the Iterator's loop.

