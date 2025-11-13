---
title: Batching
---

You will often want to create a block that initiates [Batching](/user-guide/Batching.md). 

The Ziggy CLI can help you create such a block. 

- Run `ziggy plugin block add`.
- When prompted, say `Yes` to creating a batching block. This will create a new block with the following server code.

```javascript
export async function executeBatcherBlockV1(props: BlockExecutionProps): Promise<void> {
  const { blockToExecute: block } = props
  if (!block) {
    throw new Error('Block to execute is not defined')
  }
  const config = block.data.config as BatcherBlockV1Config
  let batchItem: BatchStackProps | null = null

  // Get Axios client
  // Axios is only required for this template example. Your method may require its own client for data fetching
  const client = axios.create({
    baseURL: `https://dummyjson.com/recipes`,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  const startTime = new Date()

  try {
    // Log message (optional, writes to log file)
    logMessage(props, block, `Executing Batcher`)

    // Wait for all incoming edges to be populated
    // Note that safeWaitForInputEdgeData() let's you wait for just one specific edge
    const inputEdges = await safeWaitForAllInputEdgeData(props, block)
    if (!inputEdges) throw new Error('No input edges for this block')

    // Get the actual payload data
    const inputData = inputEdges.map(edge => edge.payload)

    // Are we in batch mode? config.isBatch is just a regular block property, so not required
    // If your block always operates in batch mode then remove the if statement
    if (config.isBatch) {
      batchItem = getBatchStackItem(props, block)
    }

    // This helper checks whether there is no more data or max iterations is reached
    // You can replace this with a customised termination test if required
    // in which case call terminateBatch(props, batchItem) then return if test is true
    if (batchItem && shouldTerminateBatchHelper(props, batchItem, config.maxIterations)) return

    // GET SOME DATA
    // Replace this code as required
    const limit = config.batchSize
    const offset = batchItem ? batchItem.offset : 0
    const response = await client.get(`?limit=${limit}&skip=${offset}`)
    const outputData = response.data.recipes as unknown[]

    // Update batch information
    // batchItem.noMoreData = true should be set when you determine that there is no more data to fetch
    // This code may need to be adapted to suit your pagination mode
    // If using cursor based pagination, see documentation
    if (batchItem) {
      if (outputData.length < limit) batchItem.noMoreData = true
      batchItem.offset += outputData.length
    }

    // Record execution time
    block.data.executionTime = new Date().getTime() - startTime.getTime()

    // Send data to the next block(s) via output edges
    // This must be always called to allow Flow execution to continue
    const outEdges = outgoingEdgeAssignment(
      props,
      block,
      0, // Output edge index (0 = first output)
      inputData[0] ?? null,
      outputData, // Your fetched data to send to next block
      batchItem || undefined, // Add the block's batchItem. Undefined if your block can operate on non-batch mode
    )

    // Log execution time
    props.logTime(props, block, inputData, outEdges, block.data.executionTime)
  } catch (error) {
    if (error instanceof Error) {
      formulateFatalError(props, block, error.stack || error.message)
    } else {
      formulateFatalError(props, block, String(error))
    }
  }
}

```

## Batch setup
`getBatchStackItem()` sets up the batching. Note that `if (config.isBatch) {...}` is optional and is included for illustrative purposes only. If your block always operates in batch mode, then you would not define `isBatch` in your [config](./config.md) file.

```javascript
    if (config.isBatch) {
      batchItem = getBatchStackItem(props, block)
    }
```

## Terminating the batch
At some point, your batch will need to terminate

- When there is no more data available 
- If you have a config property `maxIterations` and the batch has performed that many iterations.

Call the following helper function to check whether there is no more data or `maxIterations` has been reached. You only need modify the last parameter.

````javascript
    if (batchItem && shouldTerminateBatchHelper(props, batchItem, config.maxIterations)) return
````

If you want to manage your own termination logic, then you can call `terminateBatch(props, batchItem)` when you determine that the batch should terminate.

## Setting noMoreData
You should include some logic to tell the batching whether there is any more data to fetch. Below we are checking whether the amount of data returned by the `const response = await client.get(`?limit=${limit}&skip=${offset}`)
` is less than the `limit` value. In this case, we can assume that there is no more data to fetch and therefore set `batchItem.noMoreData = true`.

```javascript
   if (batchItem) {
      if (outputData.length < limit) batchItem.noMoreData = true
      batchItem.offset += outputData.length
    }
```

