# API

## Purpose

Document the public or internal API contracts exposed by the system.

## API Overview

**Protocol:** HTTP/HTTPS

**Style:** REST

**Base URL:** `https://api.example.com`

**Authentication:** [JWT / OAuth 2.0 / API Key / Other]

## Endpoints

### GET /patients/{id}

**Purpose:** Retrieve a patient.

**Authentication:** Required

**Response:** `200 OK`

```json
{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com"
}
```

### POST /patients

**Purpose:** Create a patient.

**Request:**

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Response:** `201 Created`

## Error Handling

### Example

```json
{
  "status": 400,
  "code": "INVALID_REQUEST",
  "message": "The request is invalid."
}
```

## Versioning

### Example

```text
/api/v1/patients
/api/v2/patients
```

## Pagination

### Example

`GET /patients?page=0&size=20`

## Rate Limiting

**Example:** 100 requests per minute per client.

## API Documentation

Link to OpenAPI/Swagger documentation if available.
