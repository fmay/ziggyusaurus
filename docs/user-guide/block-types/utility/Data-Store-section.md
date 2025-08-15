---
title: Data Store
---

# Data Store

The Data Store is a key/value store that is used for temporary storage of data. 
It is especially useful in migrations or situations where you need to store data somewhere that gets used in a subsequent Flow.

## Platform Settings

### Internal
This stores data inside the Ziggy database. 
It is intended for scenarios where the total number of keys stores is in the hundreds of thousands. 
When this gets too large, the performance will slow down. 

### AWS
This uses AWS DynamoDB to store data. As a result, it is infinitely scalable and can contain any 
number of keys. When running Ziggy Solo, you will need to configure the following environment variables.

- `DATA_STORE_AWS_REGION=your_aws_region`
- `DATA_STORE_AWS_ACCESS_KEY=your_access_key`
- `DATA_STORE_AWS_SECRET=your_secret`

### Azure
We will shortly be adding support for CosmosDB for anyone running Ziggy Solo on Azure.

## Name and Key
The data store is a Key/Value store but it also provides an additional field **```name```** so you can create a namespace for your data. 

The combination of **```name + key```** must be unique within the store.

## Data Store Block
The [Data Store Block](Data-Store.md) gives you access to Data Store operations without the need to write any Javascript code.

## Javascript API
You can also perform Data Store operations from the Javascript Block. The following methods are available.

**Important** : all methods are asynchronous.

<table>
    <tr>
        <td>Method</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>fetch(fetchProps)</code></td>
        <td> Retrieve keys using <code>fetchProps</code> whose type definition is <code>
 {
  limit: maximum records to retrieve,
  offset: offset from start ,
  flowUuid?: flow's unique id,
  key?: keyname,
  name?: namespace name,
  data?: search for data (currently exact match only)
}
</code>
            <ul>
                <li><code>key</code> : a globally unique key</li>
                <li><code>value</code> : any data</li>
                <li><code>timeoutUnit</code> : "seconds"|"minutes"|"hours"|"days"|"never"</li>
                <li><code>timeoutValue</code> : timeout value in the units specified by <code>timeoutUnit</code></li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><code>  async findName(name: string, limit: number, offset: number) {
    return this.storeRepo.findName(name, limit, offset)
  }</code></td>
        <td>Retrieve all keys within the specified namespace.
            <ul>
                <li><code>limit</code> : maximum keys to retrieve</li>
                <li><code>offset</code> : relative to this offset value</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><code>findNameKey(name: string, key: string)</code></td>
        <td>Retrieve the specified key within the specified namespace.
            <ul>
                <li><code>name</code> : namespace</li>
                <li><code>key</code> : key</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><code>insert(name: string, key: string, data: any)</code></td>
        <td>Insert a new key into the specified namespace. Will error isf the namespace+key combination already exists.
            <ul>
                <li><code>name</code> : namespace</li>
                <li><code>key</code> : key</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><code>upsert(name: string, key: string, data: any)</code></td>
        <td>Insert a new key into the specified namespace if it doesn't exist, update if it does.
            <ul>
                <li><code>name</code> : namespace</li>
                <li><code>key</code> : key</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><code>updateOneNameKey(name: string, key: string, data: any) {</code></td>
        <td>Update a key/value pair in the specified namespace.
            <ul>
                <li><code>name</code> : namespace</li>
                <li><code>key</code> : key</li>
                <li><code>data</code> : data to store</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><code>deleteOneNameKey(name: string, key: string) {</code></td>
        <td>delete a key/value pair in the specified namespace.
            <ul>
                <li><code>name</code> : namespace</li>
                <li><code>key</code> : key</li>
            </ul>
        </td>
    </tr>
</table>

## Data Store browser
You can browse and search for data in the Data Store using the [Store Browser](Data-and-Memory-Store-Browser.md). 
This works for **Internal** mode only.
