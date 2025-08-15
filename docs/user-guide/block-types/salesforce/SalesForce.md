---
title: SalesForce
---

# SalesForce
This section contains SalesForce specific blocks.

Please note that you should create a SalesForce connection in the [Connection Manager](Connections.md)
as well as a Secret in the [Secrets Manager](Secrets.md).

The SalesForce Connection object will look like this.

```javascript
{
    username: "myemail4@agentforce.com",
    password: "H8KK87KHJA7JGH7",
    token: '987JHGehKJHh7KJh8wOiu77dd'
}
```

You should define a secret to contain your Private App token that is referenced from the Connection.

You then specify this Connection in the dropdown in the block.
In this way, it is possible to address multiple SalesForce instances.