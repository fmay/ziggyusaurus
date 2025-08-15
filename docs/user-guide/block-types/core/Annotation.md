---
title: Annotation Block
---

# Annotation Block

The Annotation Block is a core block type that allows you to add documentation and explanatory notes directly within your flows. It's essential for creating self-documenting workflows and maintaining clear flow logic.

## Overview

The Annotation Block is responsible for:
- Adding documentation to flows
- Explaining complex logic and decisions
- Providing context for flow sections
- Creating self-documenting workflows
- Maintaining flow documentation

## Configuration

Annotation blocks can be configured with various options including:
- **Content**: The annotation text or documentation
- **Format**: Text formatting and styling options
- **Position**: Where to place the annotation in the flow
- **Visibility**: Control annotation display options
- **Links**: Add references to external documentation

## Annotation Types

### Text Annotations
- **Plain Text**: Simple text explanations
- **Formatted Text**: Rich text with formatting
- **Code Examples**: Code snippets and examples
- **Links**: References to external resources

### Visual Annotations
- **Flow Diagrams**: Visual flow representations
- **Decision Trees**: Decision logic diagrams
- **Data Flow**: Data movement illustrations
- **Process Maps**: Process step visualizations

### Documentation Annotations
- **Requirements**: Business requirements and specifications
- **Assumptions**: Key assumptions and constraints
- **Dependencies**: External dependencies and requirements
- **Notes**: General notes and observations

## Usage Examples

### Basic Documentation
```markdown
# Data Processing Flow

This flow processes customer data from multiple sources:
1. Extract data from CRM system
2. Validate and clean data
3. Transform to standard format
4. Load into data warehouse

**Note**: Ensure data quality checks are enabled
```

### Code Documentation
```javascript
// This block handles data transformation
// Input: Raw customer data from CRM
// Output: Standardized customer records

// Key transformations:
// - Normalize phone numbers
// - Standardize address format
// - Validate email addresses
// - Remove duplicates
```

### Process Documentation
```markdown
## Error Handling Process

When errors occur:
1. Log error details
2. Send notification to support team
3. Attempt automatic recovery
4. If recovery fails, escalate to manual review

**Recovery Timeout**: 5 minutes
**Escalation Threshold**: 3 failed attempts
```

## Best Practices

### Content Guidelines
- **Be Clear**: Use clear, concise language
- **Be Specific**: Provide specific details and examples
- **Be Current**: Keep annotations up to date
- **Be Relevant**: Focus on important information

### Placement Strategy
- **Logical Flow**: Place annotations where they're most relevant
- **Grouping**: Group related annotations together
- **Spacing**: Use appropriate spacing for readability
- **Consistency**: Maintain consistent annotation style

### Maintenance
- **Regular Updates**: Update annotations when flows change
- **Version Control**: Include annotations in version control
- **Review Process**: Regular review of annotation accuracy
- **Cleanup**: Remove outdated or irrelevant annotations

## Annotation Formats

### Markdown Support
```markdown
# Main Heading
## Subheading
**Bold text**
*Italic text*
- Bullet points
1. Numbered lists

[Link text](URL)
![Image alt](image-url)
```

### HTML Support
```html
<h1>Main Title</h1>
<p>Paragraph text</p>
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
</ul>
<strong>Important text</strong>
```

### Code Blocks
```javascript
// JavaScript code example
function processData(data) {
    return data.map(item => ({
        id: item.id,
        name: item.name.toUpperCase(),
        processed: true
    }));
}
```

## Use Cases

### Flow Documentation
- **Purpose**: Explain what the flow does
- **Requirements**: Document business requirements
- **Assumptions**: List key assumptions
- **Constraints**: Identify limitations and constraints

### Technical Documentation
- **Architecture**: Document system architecture
- **Dependencies**: List external dependencies
- **Configuration**: Document configuration options
- **Troubleshooting**: Provide troubleshooting guidance

### Business Documentation
- **Process**: Document business processes
- **Rules**: Explain business rules and logic
- **Decisions**: Document decision points and criteria
- **Outcomes**: Describe expected outcomes

### Training and Onboarding
- **New Users**: Help new users understand flows
- **Training**: Provide training materials
- **Reference**: Create reference documentation
- **Examples**: Provide usage examples

## Integration with Other Blocks

### Flow Organization
- **Section Headers**: Mark flow sections
- **Decision Points**: Explain decision logic
- **Error Handling**: Document error procedures
- **Output Description**: Explain expected outputs

### Documentation Links
- **External Docs**: Link to external documentation
- **Related Flows**: Reference related workflows
- **API Documentation**: Link to API documentation
- **Knowledge Base**: Connect to knowledge base articles

## Related Blocks

- [Javascript](/user-guide/block-types/core/Javascript) - For code examples
- [Console-Message](/user-guide/block-types/core/Console-Message) - For runtime output
- [Variable-Set-Get](/user-guide/block-types/core/Variable-Set-Get) - For documenting variables
- [Branch](/user-guide/block-types/core/Branch) - For documenting decision logic

## Examples by Flow Type

### Data Processing Flows
```markdown
# Customer Data Processing

**Purpose**: Process and validate customer data from multiple sources

**Input Sources**:
- CRM system (primary)
- Website forms (secondary)
- API integrations (tertiary)

**Validation Rules**:
- Email must be valid format
- Phone must be 10 digits
- Required fields: name, email, phone

**Output**: Standardized customer records for data warehouse
```

### Integration Flows
```markdown
# CRM to Marketing Integration

**Purpose**: Sync customer data between CRM and marketing systems

**Sync Frequency**: Every 15 minutes
**Data Volume**: ~1000 records per sync
**Error Handling**: Retry 3 times, then alert support

**Dependencies**:
- CRM API access
- Marketing platform API
- Authentication tokens

**Security**: All data encrypted in transit
```

### Workflow Flows
```markdown
# Customer Onboarding Process

**Purpose**: Automate customer onboarding workflow

**Process Steps**:
1. Account creation
2. Email verification
3. Profile completion
4. Welcome sequence
5. First login

**Timing**: 24-hour completion target
**Escalation**: Manual review after 48 hours
```
