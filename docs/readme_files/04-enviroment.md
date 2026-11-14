# Infra and Development Enviroment

## Development Environment

**Description:** how to run the project and add new features.

### Requirements

- Spring/Java
- Postgres
- Git
- Docker

#### Setup

1. Clone the repository.
2. Run enviroment on docker.
3. Configure environment variables.
4. Start required services.
5. Run the application.

#### Development Workflow

Create issue
     ↓
Create feature branch
     ↓
Develop
     ↓
Run tests
     ↓
Commit
     ↓
Pull Request
     ↓
Code Review
     ↓
Merge

## Infrastructure

**Description:** where the application runs.

### Hosting

| Service | Provider | Purpose |
| --- | --- | --- |
| Database | Neon | Database cloude hosting |
| Static website | GitHub Pages | Frontend hosting |

### Database

| Service | Technology | Purpose |
| ---------------- | --------------------- | ------------------------- |
| Main Database | PostgreSQL | Application |
| — | — | — |

### External Services

| Service | Purpose |
| --- | --- |
| JWT/Oauth2.0 | Authentication |
| RabbitMQ | Message broker |
