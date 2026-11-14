# Architecture Decision Records (ADR)

Architecture Decision Records (ADRs) are short documents used to record important architectural and technical decisions made during a project.

An ADR should explain what was decided, why it was decided, and what consequences the decision has.

The purpose is not to document every technical choice, but to preserve decisions that may be relevant to future development and maintenance.

## Why Use ADRs?

ADRs help the team:

- Understand why a technology or architectural approach was chosen.
- Avoid revisiting decisions without new information.
- Preserve historical context when team members change.
- Make trade-offs explicit.
- Document decisions that are difficult or expensive to reverse.
- What Should Be an ADR?

## Good candidates include decisions about

- Architecture
- Frameworks and major technologies
- Databases
- Communication between services
- Authentication and authorization
- Deployment strategies
- Important design patterns
- Infrastructure
- Significant changes to existing architecture
- Examples

## Good ADR 1

Use PostgreSQL as the primary relational database.

This is an architectural decision that affects the system significantly.

## Good ADR 2

Use REST instead of GraphQL for the public API.

This establishes an important communication strategy.

## Good ADR 3

Use JWT-based authentication with Keycloak.

This affects security and application architecture.

Usually not worth an ADR:

Rename getUser() to findUser().

Change a button's color.

Add a validation to a form.

These are implementation details that normally do not require architectural history.

## Example  

### ADR-001: Use PostgreSQL as the Database

#### Status

Accepted

#### Context

The application requires a relational database...

#### Decision

We will use PostgreSQL as the primary database.

#### Alternatives Considered

- MySQL
- SQL Server
- MongoDB

#### Consequences

##### Positive

- Strong relational capabilities
- Open source
- Good ecosystem

##### Negative

- Requires PostgreSQL-specific knowledge
