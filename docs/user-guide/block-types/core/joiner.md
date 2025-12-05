---
title: Joiner
description: Learn how to use the Joiner block in Ziggy flows for joining multiple data streams. Complete guide with examples and configuration options.
keywords: [ziggy, joiner, core blocks, flows, no-code, data processing]
image: /img/ziggy-logo-light-bg.webp
---

# Joiner

This block performs the following join operations on two or more input edges.

- **Inner** join
- **Left** Outer Join
- **Right** Outer Join
- **Full** join
- **Cross** join

**Important** : the join operations are performed in sequence. You cannot define a join operation between the first and last inputs.

The screenshot below shows this in action.

<img src="/img/flows/blocks/core/joiner/joiner-flow-example.png" alt="Joiner" width="1200" />

- The first Join block joins the Departments and Users on `departmentId` from the first edge and `deptId` from the second edge.
- The second Join block joins the result of the first join operation with the Profile data. 

If you run the Flow, the output edge data is as follows.

<img src="/img/flows/blocks/core/joiner/joiner-edge-data.png" alt="Joiner edge data" width="400" />

Note the `d` and `p` keys in the data. Prefixing is explained below.

## Prefixes
The optional Prefix field allows you to specify the key under which the data from the input edge is output. In the above example, 
the Department data will appear as `d.departmentId, etc...`. If you leave the field empty, it will be output in the root of the object.

**Final Prefix** refers to the prefix applied to the last input edge.

If you leave the prefixes empty then all data is output on the root level of the output object. If there are keys with same name, 
the last key in the sequence will win.




