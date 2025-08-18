---
title: Feature summary
---

<iframe 
  src="https://player.vimeo.com/video/1055633021" 
  width="100%" 
  height="400" 
  allow="fullscreen; picture-in-picture" 
  allowfullscreen>
</iframe>

Below is a quick summary of Ziggy's key features.

### Flow

Ziggy provides a canvas where you design Flows, which are made up of interconnected Blocks.

A key concept of Ziggy is to make communication with target Platforms as easy as possible. The Hubspot blocks are an excellent example of this.

The Flow shown below is a good example of this.

![data prep](/img/etl-intro/intro-data-prep.png)

- Read in all Hubspot Deals (in batches of 100). There is a Filter applied to only take deals with a value of > $1000. A few Hubspot properties are retrieved.
- Get the associated Companies using a specific association type and fetches the specified Company properties.
- Writes the combined Deal and Company information to the output edge (an example is shown below)
- Writes the data to a SQL database table.

```json
{
  deal_amount: null,
  deal_createdate: "1998-04-15T23:00:00Z",
  deal_dealname: "Königlich Essen",
  deal_hs_acv: "2160.00",
  deal_hs_lastmodifieddate: "2025-04-17T09:30:06.997Z",
  deal_hs_object_id: "169335052481",
  deal_hs_tcv: "2160.00",
  company_name: "Königlich Essen",
  company_country: "Germany"
}
```

### Core Blocks

These are simple Blocks that are commonly used.

![core blocks](/img/etl-intro/intro-core-blocks.png)

### Utility Blocks

The perform more complex tasks such as:

- Writing CSV/JSON data to files on S3, SFTP etc.
- Writing to and reading from databases.
- REST calls.
- Writing to and reading from Ziggy's key/value Data Store.

![utility blocks](/img/etl-intro/intro-utility-blocks.png)

### Hubspot Blocks

These blocks are designed to simplify interactions with Hubspot.

![hubspot blocks](/img/etl-intro/intro-hubspot-blocks.png)

### Javascript Block

The Javascript Block is a very flexible Block. Use it to:

- Make custom REST API calls
- Embed logic inside your flow
- Create Custom Blocks in a Subflow

![js example](/img/etl-intro/intro-js-example.png)

## Debugger

Ziggy provides a full step-through debugger. You can inspect data and view logs.

![debugging](/img/etl-intro/intro-debugging.png)

## Key Features

### Data Inspection

You can inspect data at any point in your Flow by clicking on the edge "bubble". This will show you the first few records that have passed through that edge.

![edge bubble](/img/etl-intro/intro-edge-bubble.png)

You can also inspect data by right-clicking on an edge and selecting "Inspect Data". This will show you a paginated view of the data.

![edge inspect data](/img/etl-intro/intro-edge-inspect-data.png)

### Edge Validation and Mapping

You can validate and map data on edges. This is useful for ensuring data quality and transforming data as it flows through your Flow.

![edge validate map](/img/etl-intro/intro-edge-validate-map.png)

### Edge Transformation

You can also transform data on edges using Javascript. This is useful for more complex data transformations.

### Subflows

You can create Subflows to organize your Flow and reuse common patterns. Subflows can be called from other Flows and can accept parameters.

### Execution History

Ziggy keeps a history of all Flow executions. You can view the results of previous executions and debug issues.

### Batching

Ziggy can process data in batches to improve performance and reduce memory usage.

### Queuing

Ziggy can queue Flow executions to ensure they run in the correct order and prevent resource contention.

### Alerts and Logging

Ziggy provides comprehensive logging and alerting capabilities. You can set up alerts for Flow failures and monitor Flow performance.

### Secrets Management

Ziggy provides a secure way to store and manage secrets such as API keys and database passwords.

### Variables

You can define variables in your Flow and use them in Blocks. Variables can be set at runtime or defined in the Flow configuration.

### Connections

Ziggy provides a way to define and manage connections to external systems such as databases and APIs.

### Data Store

Ziggy provides a key/value Data Store that can be used to store data between Flow executions.

### Memory Store

Ziggy provides an in-memory store that can be used to store data during Flow execution.

### Commander

Commander is Ziggy's command-line interface that allows you to manage Flows, connections, and other resources.

### Development and Production Modes

Ziggy provides separate development and production modes to ensure safe testing and deployment of Flows.

### Scheduler

Ziggy provides a built-in scheduler that allows you to run Flows on a schedule.

### Deployment Options

Ziggy can be deployed in various ways to meet your infrastructure requirements.

### Data Transfer

Ziggy provides efficient data transfer capabilities for moving large amounts of data between systems.

### Security Controls

Ziggy provides comprehensive security controls to ensure your data and Flows are protected.

## Deployment (Ziggy Solo)

Ziggy Solo gives you complete deployment flexibility:

- Deploy on your own dedicated server or cloud infrastructure
- Available as a Docker container for bare-bones installation
- Choose your own database and Redis instance
- Full control over your data and infrastructure

## Security Principles

Ziggy is designed with security in mind:

- You have full control over API access and user management
- Choose what data to persist and what to keep ephemeral
- All security controls are under your management

## Source Code

Ziggy's source code is available upon request.