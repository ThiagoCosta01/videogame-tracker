# Architecture

## Purpose
Describe the overall technical architecture, major components, responsibilities, and communication.

## Architectural Style
**Style:** [Clean Architecture / Hexagonal / Layered / Microservices / Other]

**Rationale:** Why was this style chosen?

## System Overview
Describe the main components.

### Example
- Frontend: user interface.
- API: exposes application functionality.
- Application Layer: coordinates use cases.
- Domain Layer: business logic and domain model.
- Infrastructure: database and external services.
- Database: persistence.

## Components
### [Component Name]
**Responsibility:** What it does.

**Dependencies:**
- [Dependency]

## Communication
### Example
```text
Frontend -> REST API -> Application -> Domain -> Infrastructure -> Database
```

## Architectural Principles
- Separation of concerns
- Dependency inversion
- Explicit boundaries
- Testability

## Quality Attributes
- Security
- Performance
- Scalability
- Maintainability
- Availability
