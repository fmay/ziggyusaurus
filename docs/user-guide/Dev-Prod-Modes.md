---
title: Dev-Prod Modes
---

# Dev-Prod Modes

Ziggy supports separate development and production modes to ensure safe testing and deployment workflows. This feature allows you to develop and test flows in a controlled environment before deploying to production.

## Overview

Dev-Prod Modes provide:
- **Development Environment**: Safe testing and experimentation
- **Production Environment**: Stable, optimized execution
- **Environment Isolation**: Separate configurations and data
- **Deployment Control**: Controlled promotion of flows

## Mode Configuration

### Development Mode
- **Testing Environment**: Safe place to develop and test flows
- **Sample Data**: Use test datasets without affecting production
- **Debug Features**: Enhanced logging and debugging capabilities
- **Connection Testing**: Test external system connections safely

### Production Mode
- **Live Environment**: Real data and production systems
- **Performance Optimized**: Optimized for production workloads
- **Security Enhanced**: Stricter security and access controls
- **Monitoring Enabled**: Full production monitoring and alerting

## Environment Settings

### Development Settings
```javascript
// Development mode configuration
{
    "mode": "development",
    "debug": true,
    "logging": "verbose",
    "connections": "test",
    "dataStores": "dev"
}
```

### Production Settings
```javascript
// Production mode configuration
{
    "mode": "production",
    "debug": false,
    "logging": "standard",
    "connections": "live",
    "dataStores": "prod"
}
```

## Mode Switching

### Switching to Development
1. **Global Settings**: Set system mode to development
2. **Flow Settings**: Configure flows for development
3. **Connection Setup**: Use test connection configurations
4. **Data Preparation**: Set up test datasets

### Switching to Production
1. **Validation**: Ensure flows are thoroughly tested
2. **Configuration**: Update to production settings
3. **Connection Update**: Switch to live connections
4. **Monitoring**: Enable production monitoring

## Best Practices

### Development Phase
- **Test Thoroughly**: Test all flow paths and edge cases
- **Use Sample Data**: Never use production data in development
- **Document Changes**: Keep track of modifications and improvements
- **Peer Review**: Have team members review flow logic

### Production Deployment
- **Gradual Rollout**: Deploy to production incrementally
- **Rollback Plan**: Have a plan to revert if issues arise
- **Monitoring**: Watch closely during initial deployment
- **Documentation**: Update production documentation

### Environment Management
- **Separate Configurations**: Keep dev and prod configs separate
- **Version Control**: Use version control for configuration changes
- **Backup Strategy**: Regular backups of production configurations
- **Access Control**: Limit production access to authorized users

## Use Cases

- **Flow Development**: Develop new flows in development mode
- **Testing**: Test flow modifications before production
- **Debugging**: Debug issues in a safe environment
- **Training**: Train users on new flows without production risk
- **Staging**: Final validation before production deployment

## Related Topics

- [Global Settings](/global-settings/Global-Settings) - System configuration
- [Deployment](/deployment/Deployment) - Production deployment
- [Testing](/tests/Tests) - Flow testing procedures
- [Security](/security/Security) - Security considerations
