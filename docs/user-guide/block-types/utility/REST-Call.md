---
title: REST Call Block
---

# REST Block
This Utility Block is used to make REST API calls. If you require more features, you can use the Axios module from the Javascript Block.

![rest](rest-block.png){width="500"}

The Block shows the current configuration, which can be changed by pressing the Edit button.

![Edit REST](rest-block-edit.png)

## Method
The usual REST method (GET, POST, PUT, PATCH, DELETE) should be selected from the dropdown.

## URL
The URL can contain query and path parameters. These can be literal values but you can also insert tokens in the format ```token.qualifier```

<table>
    <tr>
        <td>Token</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>$</code></td>
        <td> References data on the input edge.
            <ul>
            <li>{$} would replace the token with the complete edge data.</li>
            <li>{$.limit} would replace the token with the edge's ```limit``` key value</li>
        </ul></td>
    </tr>
    <tr> 
        <td><code>variables</code></td>
        <td>Replace token with a variable value.<br/><code>{variables.limit}</code> for example.</td>
    </tr>
    <tr> 
        <td><code>secrets</code></td>
        <td>Replace token with a secret's value.<br/><code>{secrets.apiKey}</code> for example.</td>
    </tr>
    <tr>
        <td><code>batch</code></td>
        <td>For both limit/offset and cursor pagination see **Pagination** below.
        </td>
    </tr>
</table>

## Pagination
If you want to paginate your REST calls, then you should check the **loop until no data** box. This will process in batches (make sure you have a **Batch End** block to close the loop).

### Using offset/limit
If the API expects offset and limit values, then you would include something like the following in the URL.

- ```&limit=100``` or ```&limit={$.limit}``` if the limit value in reference by taking the value from the input edge data.
- ```&offset={batch.offset}}``` - the batch offset value is managed internally so you do not need to set this value anywhere.

### Using a pagination cursor
Some APIs use a cursor, in which case you need to tell Ziggy where to find the cursor in the response data. Several HubSpot APIs return a cursor, which you reference using

- ```paging.next.after```

You would include this cursor in the URL as follows.

- ```&after={batch.paging||"!remove!"}```

Read on for information about ```!remove!```

## Using '!remove!'
Some API endpoints may not function correctly if a query parameter is empty. For example, HubSpot APIs that support pagination will error if you pass either ```&after=``` or ```after=''```'. In other words, if the ```after``` parameter, if used, must contain a value.

You solve this by adding ```!remove!``` which strips the query parameter out of the URL if it's empty, so ```&after={batch.paging||"!remove!"}```.

## Headers
You can add or remove Headers from the edit dialog. Note that you can use tokens (see above table) to access input edge data, secrets and variables.

## Body
Specify a token to indicate where the body data should come from. This will often be an {input.path} token.

## Response data path
Once the response payload has been received, you should specify the object path to the data that should be placed on the output edge.

If, for example, the returned data object is as follows, you would specify ```results``` as the data path. If you leave this field empty, then the root object will be placed on the output edge by default.

```JavaScript
{
    results: [some data array],
    paging: {
        next: {
            after: '876128763'
        }
    }
}
```

## Batching
If you are fetching large quantities of data, you will usually need to use some form of pagination.

To enable pagination (as is the case in the above screenshot) you should check the 'Loop until no data' box.

### URL query parameters

- ```limit``` and ```offset``` query or path parameters.
- Cursor pagination.

In this situation, one of the following URL tokens should be used.

```JavaScript
{batch.offset}
or
{batch.paging}
```

### Cursor Pagination
If the API is using cursor pagination, you should specify the response data path to the cursor key. 

In the above example, you can see we have specified ```paging.next.after```.

### Batch End Block
You should be sure to include a [Batch End Block](Batch-End.md) downstream of the REST Block as the loop back point. You can include other Blocks in between.

