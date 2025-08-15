---
title: File Reader / Writer
---

# File Reader / Writer

This block reads from and writes to files that are stored on the following platforms.

- **File System** - files that are stored in the Ziggy platform. See below for more information.
- **SFTP** - a remote SFTP server
- **AWS S3**
- **Azure** - coming soon. Email [info@ziggyservices.com](mailto:info@ziggyservices.com) if you require this urgently.

## Data formats
Ziggy currently supports the following data formats. The format is specified in the block configuration.

- CSV
- JSON

## Reading
Regardless of the platform, reading is a batch operation.

- There should be a [Batch End](Batch-End.md) block further down the Flow.
- You should specify the batch size and number of iterations (0 means read entire file)

## Platform - File System
You will typically write to a File on the Ziggy platform. 

If a Flow chooses to write to a Ziggy file, you can read from this file in the same or in another Flow.

### Write
![File write](file-file-write.png)

### Read

![File read](file-file-read.png#width=450)

When reading from a file, you need to specify the batch buffer size and the number of iterations to process (0 means read whole file).

## Platform - AWS S3
You need to have defined a Connection in the [Connection Manager](Connections.md). You then select the Connection in the block.

This is an NPM connection object, which will typically be as shown below. Note this references two secrets
in the [Secrets Manager](Secrets.md) to avoid exposing it.

```javascript
{
  region: 'us-east-1', 
  credentials: {
    accessKeyId: secrets.S3ExperimentorKeyId,
    secretAccessKey: secrets.S3ExperimentorSecret,
  }
}
```

You should choose the data format and read/write mode.

![S3 write](file-s3-write.png#width=300)

## Platform - SFTP

You need to have defined a Connection in the [Connection Manager](Connections.md). 
You then select the Connection in the block.

This is an NPM connection object, which will typically be as shown below. Note this references two secrets
in the [Secrets Manager](Secrets.md) to avoid exposing it.

```javascript
{
    host: 'eu-west-1.sftpcloud.io',
    port: '22',
    username: 'a875a*&6as876a876',
    password: 'XHs*8767sAsd&*aK7'
}
```

You should choose the data format and read/write mode.

![S3 write](file-sftp-write.png#width=300)
