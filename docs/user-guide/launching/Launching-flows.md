---
title: Launching flows
---

# Launching flows
All Flows can be launched from the UI. For migrations, this is the typical approach,

# Launching a Flow with an API call
For most integration scenarios, you will want to launch your Flows from an external source.
An API call is the usual approach.

## Execution Keys
You will first need to generate an API key. An administrator should

- Navigate to **Global Settings** (gear icon in the navigation bar).

<img src="/img/flows/launching/global-settings-icon.png" alt="400" width="400" />

- Select the **Security** tab.

<img src="/img/flows/launching/execution-keys.png" alt="600" width="600" />

You can generate and revoke multiple keys.

**Important** : the key cannot be viewed a second time, so when prompted for the key, please put it somewhere secure. If you lose it, simply generate another one and revoke the previous one.

## Endpoint
To get the endpoint for the Flow

- Click on the Flow name or the **Gear** icon in the Flow info bar.

<img src="/img/flows/launching/flow-info-bar.png" alt="500" width="500" />

- The Flow identifier can be seen at the top , and forms an integral part of the endpoint URL.
- Press the **URL** button to generate the full url.
- Note this is a **POST** request.

```javascript
https://hubspot.ziggyservices.com/api?flowUuid=<your flow uuid>&execution-key=<your execution key>&executionEnvironmentMode=DEV&executionId=f4b6b4c6-9525-4c0e-94e3-b93e3d798b57
```

You can also send the execution key in the **execution-key** header.

## Execution ID
The `executionId` query parameter is optional. It lets you pass in a **unique** string that identifies the Flow. 

If you are launching Flows programmatically, then you might want to query the execution status of the Flow (see below). 
In this case you should generate a unique id (a UUID is ideal) in your code and pass this value as the `executionId`.

This value will also be shown when viewing the [Execution History](/user-guide/editor/Execution-history) and when using the [Audit block](/user-guide/block-types/utility/audit).

## Passing data to the Flow
Data you want to pass to the Flow should be included in the request body in JSON format.

Any Test Data you might have in the **Receiver** block will be ignore when called with an API call.

## System Queuing
When a Flow is launched, it is added to the system execution queue. 

You can set the number of parallel Flow executions using the `MAX_CONCURENT_JOBS` parameter in your `.env` file. This is 10 by default.

If Ziggy is able, it will immediately execute the Flow. You can check the execution status as explain below.

## Checking Flow execution status
If you are launching Flows programmatically, you can check the execution status with the following **GET** request.

```javascript
http://localhost:3000/api/ziggy/execution-status/<execution-id>
```

This returns an object of the following shape.

```javascript
export class ExecutionStatusResponse {
  executionId: string
  terminationStatus: string
  ms: number
  executionEnvironmentMode: string
  createdAt: Date
  flowUuid: string
  flowName: string
}
```

If it returns a `4XX` error, the Flow has not yet been released from the Queue or has not finished executing.

## Test with Postman
The simplest way to experiment is to use Postman.

- Paste the URL and set the method (POST for executing, GET for checking status)
- Add your **execution-key** as a header or query parameter.
- Add an `executionId` as a query parameter (optional).
- Put any data you want to pass to the Flow in the body and ensure it is JSON encoded (raw/JSON in Postman).
