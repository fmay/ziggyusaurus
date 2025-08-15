---
title: Variables
---

# Variables

Variables store values that are like secrets, but not secret! Open the Variables dialog from the menu bar.

When a Flow executes, all Variables are cloned and can be freely manipulated by the Flow without affecting the default values.

## Accessing from Blocks
You will work with variables in various Blocks. 

### Javascript Block
Access variable values.

```javascript
const myVar = variables.myVariableName
variables.someVar = 'A new value'
```

Note that you can add new variables for the lifetime of a Flow and change the variable's value during the Flow's lifetime.

If you set a variable and that variable name does not exist on the ```variables``` object then it will be created and is available from that point onwards. It will not create an entry in the Variables dialog.

## Other Blocks
Some Blocks have fields that reference a value as literals. 

For example, the Data Store key field name can be specified by entering ```userId```.

However, you could get the name from a variable using ```{variables.keyFieldName}```.

