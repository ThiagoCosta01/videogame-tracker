# Integrations

## Purpose

Document external systems, APIs, services, queues, and other systems the application communicates with.

## Integration Overview

| System | Type | Purpose | Protocol |
| --- | --- | --- | --- |
| Keycloak | Identity Provider | Authentication | OIDC |
| Payment API | External API | Payments | REST |
| RabbitMQ | Message Broker | Async communication | AMQP |

## Integration: [System Name]

**Purpose:** Why the integration exists.

**Direction:** [Inbound / Outbound / Bidirectional]

**Protocol:** [REST / SOAP / OIDC / AMQP]

**Authentication:** [OAuth2 / API Key / mTLS]

**Endpoint:** `https://example.com/api`

## Failure Handling

Describe what happens when the external system fails.

### Example

- Retry transient failures up to 3 times.
- Use exponential backoff.
- Log failures.
- Return a controlled error if recovery fails.

## Data Mapping

| External Field | Internal Field |
| --- | --- |
| `customerId` | `customer.id` |
| `fullName` | `customer.name` |

## Security Considerations

Document authentication, credentials handling, encryption, and sensitive data.

**Never store real secrets in this document.**

## Dependency Criticality

**Criticality:** [Low / Medium / High / Critical]
