---
title : Server code
---

## Building
In order for the Ziggy server to pick up on changes in your code, your plugin needs to be rebuilt. You should use one of the `package.json` scripts. With `dev`, it will build on any changes.

The Ziggy server will pick up on changes in real-time. If you do not see changes in the Ziggy UI, then reload the browser.

If you have added new blocks, then you should run `ziggy plugin register`.

## The code
`my-block.v1.server.ts` contains the code that executes on the server when your Flow runs. 

## Basic Block
```javascript
export async function executeMyBlockBlockV1(props: BlockExecutionProps): Promise<void> {
  const { blockToExecute: block } = props

  if (!block) {
    throw new Error('Block to execute is not defined')
  }

  const config = block.data.config as MyBlockBlockV1Config
  const startTime = new Date()

  try {
    logMessage(props, block, `Executing My Block block: ${config.name}`)

    // Wait for all incoming edges to be populated
    // Note that safeWaitForInputEdgeData() let's you wait for just one specific edge
    const inputEdges = await safeWaitForAllInputEdgeData(props, block)
    if (!inputEdges) throw new Error('No input edges for this block')

    // Get the actual payload data
    const inputData = inputEdges.map(edge => edge.payload)

    // Get the data from the first input edge, if you're interested in it
    const firstEdgeData = inputData[0]

    // TODO: Implement your block logic here
    const outputData = {
      name: config.name,
      timestamp: new Date().toISOString(),
      // Anything else you might want to output to the outgoing edge
    }

    block.data.executionTime = new Date().getTime() - startTime.getTime()
    const outEdges = outgoingEdgeAssignment(props, block, 0, inputEdges, outputData)

    props.logTime(props, block, inputData ? [inputData] : [], outEdges, block.data.executionTime)
  } catch (error: any) {
    formulateFatalError(props, block, error.stack || error.message)
  }
}
```

### Waiting for input edge data
When a Ziggy server block is called, it should (almost) always wait for data to arrive before anything else. 

```javascript
    const inputEdges = await safeWaitForAllInputEdgeData(props, block)
```

This function does just that. It will wait until all incoming edges are populated with data before executing.

There is an alternative function `safeWaitForInputEdgeData()` that lets you wait for a specific edge (usually `i0`) before executing. You would only needs this in special cases.

```javascript
    const inputData = inputEdges.map(edge => edge.payload)
```

This line extracts the edge data from the edge. If you are only interested in the first edge (a common case) then you would access `inputData[0]`.

## Outputting data to an edge
Once your code has got some data (in the above example, it has hard-coded `outputData`) then you use the following function to output it to the outgoing edge.

```javascript
    const outEdges = outgoingEdgeAssignment(props, block, 0, inputEdges, outputData)
```

Note that the 3rd parameter allows you to specify which edge you are populating, which is usually `0`. If your function is doing somewhere more complex involving multiple output edges, then you would make multiple `outgoingEdgeAssignment()` calls.

## Log timing
The following function is responsible for passing timing information to the client block, where it is rendered in the top right of the block.

```javascript
    props.logTime(props, block, inputData ? [inputData] : [], outEdges, block.data.executionTime)
```

## Error handling
So any errors are output to the UI log and server logs, throw an error in the code, which will be caught and managed by `formulateFatalError()`.


