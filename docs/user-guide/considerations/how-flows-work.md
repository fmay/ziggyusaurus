---
title: How Flows work
---

## Blocks and Edges

- **Blocks** are the main components of a Flow. Each block serves a unique purpose such as making
  REST calls, executing Jsvscript, talking to Hubspot or SalesForce. There are also many Blocks for
  general data manipulation.
- **Edges** are the lines that connect Blocks and along which data flows.
- **Ports** are the input and output connection handles on a Block.

All Blocks should be connected with other Blocks using Edges connected to Block ports.

If a Block exists in a Flow without a connection to its input port, it will never be executed but
won't create an error.

If a Block does not connect to another Block via an output port, then the Flow will generate an
error when it has finished executing that Block.

## Block Execution

Blocks execute as soon as they can. Whether they are ready to execute or not depends on whether the
incoming edge or edges are populated with data.

if a Block never receives data, it will wait indefinitely until the Flow times out. This is
undesirable behaviour, so Flow design should bear this in mind.

If a prior block errors for any reason, the Flow will terminate with a Fatal Error.

A Block will block the execution flow for that part of the Flow until it has data ready for the
output edge, at which point the next block can execute. Parallel flow paths (see below) will not be
blocked.

## Edge Data

An edge will always be an array. If you were to return `{foo: 'bar'}` from a Javascript Blocks, this
will be placed on the output edge as `[{foo: 'bar'}]`.

This provides a consistent approach to transferring data between blocks and therefore all Blocks
expect data to be in this format.

## Waiting principle

As mentioned above, a Block will not execute until the input edge or edges are populated with data.
Empty data (an empty array) is considered valid data.

If the Block has multiple incoming edges, then it will not start execution until all of the edges
are populated. This is an important Flow design consideration.

It is very useful to exploit this feature to pause execution until all prior Blocks have completed
execution. However, there can be circumstances it will wait forever (until the Flow times out),
which is to be avoided.

## Parallel Execution

If a Flow splits into two or more edges, then Ziggy will place data on both edges as soon as it is
ready. The connected Blocks will then execute more or less immediately.,

Blocks do not block Flow execution. It will request the next Block be executed only when it is ready
to populate the output edge with data. In the meantime, other Blocks in parallel paths are free to
execute.

## Primary Edge

If a Block has more than one incoming edge on an input port, then one edge is considered the primary
edge. All incoming edges will have a number bubble indicating the edge indices. The primary edge is the edge with index 0.

This is important for edges that read data from the incoming edge. Where there is more than one edge, the primary edge will be referenced.

A good example of this is the following section **Edge data helpers**.

## Edge data helpers

Many Blocks have the ability to use data on the incoming edges as variables within the Block. In this situation. the data is taken from the first array element (of the Primary Edge).

To make life easier, you should run the Flow up to the Block (by stepping to it) and then stopping. Now the selection list will be populated with the data on that edge as a helper.

You can type in literal values within double quotes if you prefer, but using the populated edge data reduces the chance of typos, especially for nested data objects.
