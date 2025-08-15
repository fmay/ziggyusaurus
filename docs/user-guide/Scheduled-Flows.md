---
title: Scheduled Flows
---

# Scheduled Flows

Scheduled Flows allow you to automate the execution of Ziggy flows at predetermined intervals or specific times. This feature is essential for recurring data processing, maintenance tasks, and automated workflows.

## Overview

Scheduled Flows provide:
- Automated flow execution
- Flexible scheduling options
- Time-based triggers
- Recurring task automation

## Scheduling Options

### Time-based Scheduling
- **Daily**: Execute flows at specific times each day
- **Weekly**: Run flows on specific days of the week
- **Monthly**: Execute flows on specific dates each month
- **Custom**: Define custom intervals and patterns

### Event-based Scheduling
- **File Watchers**: Trigger flows when files appear
- **Database Triggers**: Execute flows on data changes
- **API Endpoints**: Trigger flows via HTTP requests
- **Message Queues**: Process flows based on queue events

## Configuration

Scheduled flows can be configured with:
- **Schedule**: Timing and frequency settings
- **Triggers**: What events start the flow
- **Parameters**: Input data for the flow
- **Error Handling**: What to do if execution fails
- **Notifications**: Alerts for success/failure

## Use Cases

- **Data Synchronization**: Keep systems in sync automatically
- **Report Generation**: Generate reports at regular intervals
- **Data Cleanup**: Perform maintenance tasks automatically
- **Backup Operations**: Automated backup processes
- **Monitoring**: Regular health checks and monitoring

## Best Practices

- **Test Schedules**: Verify timing works as expected
- **Monitor Execution**: Track success/failure rates
- **Resource Management**: Consider system load during execution
- **Error Handling**: Implement proper error recovery
- **Documentation**: Document what each scheduled flow does

## Monitoring and Management

- **Execution History**: View past executions
- **Status Monitoring**: Check current schedule status
- **Manual Triggers**: Run scheduled flows manually when needed
- **Schedule Modifications**: Update timing without recreating flows

## Related Topics

- [Flows Listing](/editor/Flows-listing) - Managing your flows
- [Global Settings](/global-settings/Global-Settings) - System configuration
- [Monitoring](/monitoring/Monitoring) - Flow execution monitoring
- [Alerts](/alerts/Alerts) - Setting up notifications
