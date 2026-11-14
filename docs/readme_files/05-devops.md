# DevOps Pipeline

Documentation of the project's DevOps processes, including CI/CD pipelines, automation, deployment, infrastructure, and monitoring.

---

## 📑 Contents

- [CI — Continuous Integration](#ci--continuous-integration)
- [CD — Continuous Delivery - Deployment](#cd--continuous-delivery---deployment)
- [Automation](#automation)
- [Infrastructure](#infrastructure)

---

## CI — Continuous Integration

**Description:** Processes executed when code is integrated or updated in the repository, such as commits and pull requests.

## CD — Continuous Delivery - Deployment

**Description:** Processes responsible for building and deploying the application.

### Deploy

**File:** `deploy.yml`

**Purpose:** Builds the application and deploys it to the target environment.

**Trigger:**

- Push to main or master

**Process:**

```text
Push to main/master*
      ↓
Install dependencies
      ↓
Build
      ↓
Upload artifact
      ↓
Deploy
```

## Automation

**Description:** Automated processes that support development and project maintenance but are not necessarily part of CI/CD.

### Available Automations

| Automation       | File                  | Description               |
| ---------------- | --------------------- | ------------------------- |
| README Generator | `generate_readme.yml` | Generates the main README |
| —                | —                     | —                         |

## Infrastructure

### Docker

**Purpose:** Builds the application enviroment in a container.
