# Architecture Diagrams

## Purpose

This directory contains diagrams that visually document the architecture and system behavior.

## Context Diagram

Shows the system, users, and external systems.

### Example

```text
[Patient] ---> [Medical System] ---> [Email Service]
                         |
                         +---------> [Database]
```

## Container Diagram

Shows major applications and data stores.

### Example

```text
[Web App] ---> [REST API] ---> [Database]
                    |
                    +-------> [Keycloak]
```

## Component Diagram

Shows internal application components.

### Example

```text
[Controller]
     |
     v
[Use Case]
     |
     v
[Domain]
     |
     v
[Repository]
```

## Sequence Diagram

Shows interactions over time.

### Example

```text
User -> API: Create Appointment
API -> Use Case: Execute
Use Case -> Repository: Save
Repository -> Database: INSERT
Database --> Repository: Success
API --> User: 201 Created
```

## Deployment Diagram

Shows where components are deployed.

### Example

```text
[Internet]
     |
[Load Balancer]
     |
[Application Server]
     |
[Database Server]
```

## File Naming

```text
context-diagram.png
container-diagram.png
component-diagram.png
appointment-sequence.puml
deployment-diagram.png
```

## Guidelines

- Keep each diagram focused on one purpose.
- Avoid unnecessary implementation details.
- Use terminology consistent with the domain model.
- Update diagrams when architecture changes.
