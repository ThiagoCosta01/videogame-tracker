# Data Model

## Purpose

Describe how data is structured, stored, and related.

This document focuses on **persistence**, unlike the domain model, which focuses on business concepts.

## Database

**Database:** [PostgreSQL / MySQL / SQL Server]

**Purpose:** Why this database is used.

## Tables

### [Table Name]

**Purpose:** What the table stores.

| Column | Type | Nullable | Description |
| --- | --- | --- | --- |
| `id` | UUID | No | Unique identifier |
| `name` | VARCHAR | No | Name |
| `created_at` | TIMESTAMP | No | Creation timestamp |

**Primary Key:** `id`

**Foreign Keys:**

- `patient_id` -> `patient.id`

## Relationships

### Example

```text
Patient 1 ---- N Appointment
Patient 1 ---- N Medication
```

## Indexes

| Index | Table | Columns | Purpose |
| --- | --- | --- | --- |
| IDX_PATIENT_EMAIL | patient | email | Fast lookup |

## Data Integrity

- Required fields
- Unique constraints
- Foreign keys
- Check constraints

## Migrations

**Tool:** [Flyway / Liquibase / Other]

Describe how schema changes are managed.
