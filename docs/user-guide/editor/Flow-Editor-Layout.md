---
title: Flow editor layout
---

# Flow editor layout

Below is a simple Flow in the editor. 

![Editor Flow](/img/flows/flow-editor-explanation.png

The general concepts are hopefully self-explanatory but here are some things to point out.

- **Settings** - change the Flow name, timeout, execution history data storage, tags etc.
- **Flow Info** - [document/explain your Flow](/user-guide/editor/Flow-documentation) with markdown
- **Add Block** - add a new Block to the canvas.
- **Clone** - clones your Flow.
- **Test** - indicates which [Tests](/user-guide/Tests) this Flow is associated with.
- **Debug Info** - for developers working with [source code](/customisation/Custom-Utility-Blocks).
- **Debug Flow** - run and step through your flow using the [visual debugger](/user-guide/editor/Debugging).
- **Execution History** - each time your Flow is executed, it logs it along with the complete flow data (optional).
- **Named save** - you can create a save with a name you choose. You can then restore from this at a later date.
- **Production/Development** - click on this to toggle modes. Each mode has its own secrets and connection settings.
- **Edges** - as a flow executes, data is passed along the edges. You can validate and map the data from one *Structure* to another. When you click on the bubble, you can inspect the data.
- **Console** - the Javascript Block can write data to this pane with the ```consoleMsg()``` method.
- **Flow Execution output** - as the Flow executes, each block that executes is displayed here. Any Fatal error details are shown here.

## Execution times and Block note
When a Flow has run, the execution time (ms) of each Block is displayed in the header.

You can also add a note to a Block to explain the context better.

<img src="/img/flows/flow-execution-times.png" alt="Block ms and info" width="290" />



