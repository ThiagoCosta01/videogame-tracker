# Domain Model

## Purpose

Describe the important business concepts, their responsibilities, relationships, and domain rules.

The domain model focuses on **business concepts**, not database tables.

## Domain Concepts

### [Entity / Aggregate Name]

**Description:** Business meaning.

**Responsibilities:**

- [Responsibility]

**Attributes:**

- `attribute`: Description

**Relationships:**

- [Related concept]

### Example

#### Patient

Represents a person receiving medical care.

**Relationships:**

- Has appointments.
- Has medical conditions.
- Has medications.

## Aggregates

### [Aggregate Name]

**Aggregate Root:** [Entity]

**Purpose:** Describe the consistency boundary.

## Value Objects

### [Value Object]

**Description:** Explain the concept.

### Example

**EmailAddress:** Represents a validated email address without independent identity.

## Domain Relationships

### Example

```text
Patient
  +-- Appointment
  +-- Medical Condition
  +-- Medication
```

## Domain Rules

- A patient cannot have two appointments at the same time.
- An appointment must belong to a registered patient.
