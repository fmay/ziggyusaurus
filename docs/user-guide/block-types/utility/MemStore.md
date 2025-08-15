---
title: Memory Store
---

# Memory Store
Write to and read from the Memory Store, a very simple, bare-bones key/value pair memory store. [Read more about the Memory Store](/user-guide/Memory-Store).

## Overview
This Block takes data that arrives on the input edge and stores it in the Memory Store.

- The **Namespace** field is optional and is useful for partitioning your keys. This is useful if you are using keys that might conflict but are in fact used in different contexts. 
- You can specify the data path to the edge data that should be stored in the **Key** field.
- Often, the edge data you want to store will be an array, in which case the array will be iterated over and each element will be stored against its own key. This means there must be a unique id in each array element.
- If the edge data does not have a unique id, then you should leave the **key** field empty and a UUID will be generated for you.

![Memory store](/img/flows/blocks/utility/memstore/memstore-block.png)

## Using the **Key** field
Key values will be set using the data encountered on the input edge.

If **Key** is NOT enclosed in quotes.

- Arrays will store one key per array element.
- Primitive value will store a single key.

If **Key** IS enclosed in quotes.

- This literal value will be used for the key. The entire edge object will be stored against this key.

## Operation Types
The example Flow below shows data being set and then immediately fetched.

### Set
This will set **namespace** + **key** in the memory store. You may omit namespace.

You can also set a timeout unit and value. This is useful in situations where you want to refresh data after a specific time period. However, it order to take advantage of this, you will need to use the Javascript Block to handle the refresh.

### Get
Reads the **namespace** (optional) + **Key** from the store based on the input edge data.

**Important** : you should not connect both outputs to the same node. This will cause the Flow to timeout as only one edge will be called. You can see the correct configuration in the above image.

### Delete
Deletes the **namespace** (optional) + **Key** from the store based on the input edge data.



