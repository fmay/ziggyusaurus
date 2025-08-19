---
title: EDGE
---

This is used to perform a SQL search. It is typically used in conjunction with the [AI Search Prompt Block](/user-guide/block-types/ai/ai-search-prompt), in which case you can ignore the information below.

![Edge mode](/img/flows/blocks/utility/SQL/sql-edge-mode.png)

## Configuration

### Operation
Select **EDGE** from the dropdown.

### Connection
Choose a [Connection](/user-guide/Connections#database-object) that points to the database you want to query. 

Then, choose the schema and table as well as the fields the query should return.

## Independent execution 

You can use this independently to run a SQL query, in which case the previous block should output array with the first element containing the following object.

```javascript
[
  {
    sql: {
      sql: `
        SELECT 
          ordernumber, 
          SUM(quantityordered * priceeach) AS total_sales, 
          MAX(customername) AS customername, 
          MAX(orderdate) AS orderdate, 
          MAX(country) AS country, 
          MAX(state) AS state, 
          'transform' as transform 
        FROM public.sales_data_sample 
        GROUP BY ordernumber 
        ORDER BY total_sales DESC
      `,
      countSql: `
        SELECT COUNT(*) 
        FROM (
          SELECT ordernumber 
          FROM public.sales_data_sample 
          GROUP BY ordernumber
        ) AS subquery
      `,
    },
  },
  {
    query: "Show me all sales, highest first",
    limit: 10,
    offset: 0,
    fetchIds: false,
    isAIQuery: true,
  },
]
```

The `countSql` is optional. If included, it will also perform the count operation.

The second array element contains pagination and other information. Refer to [Search Flows](/search/search-prompt-flows#receiver-data-object) for information about this object.

## Edge Output
The edge output will contain data in a standardised format and depends on the `responseType` value (optional) in the second array element.

You should run various queries that generate listings or aggregated output on the output edge to see the data returned. You can examine by [debugging](/user-guide/editor/Debugging.md) the Flow.