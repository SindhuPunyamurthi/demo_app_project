
## Project Overview

This project is a simple **Flask web application** containerized using **Docker** and managed with **Docker Compose**.  
It demonstrates **Docker networking**, **port mapping**, and a **CI pipeline using GitHub Actions** that builds and pushes the Docker image to Docker Hub.

The application exposes:
- `/` – main endpoint
- `/health` – health check endpoint

---
**File Structure**
demo_app_project/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md   


## How to Run (Docker Compose)

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
git clone https://github.com/SindhuPunyamurthi/demo_app_project.git
cd demo_app_project
docker compose up --build
````

### Access the Application

```text
http://localhost:8080/
http://localhost:8080/health
```

To stop the application:

```bash
docker compose down
```

---

## Port Explanation (MOST IMPORTANT)

### Port Configuration

```yaml
ports:
  - "8080:5000"
```

### Explanation

| Component                  | Port |
| -------------------------- | ---- |
| Flask app inside container | 5000 |
| Docker container port      | 5000 |
| Host (local machine) port  | 8080 |

### How Traffic Flows

```
Browser → localhost:8080 → Docker → Container:5000 → Flask App
```

### Why This Is Important

* Flask runs on **5000** inside the container
* Host exposes **8080**
* Demonstrates understanding of **Docker port mapping**
* Avoids host port conflicts
* Common real-world container networking pattern

---

## CI Pipeline Explanation

This project uses **GitHub Actions** for Continuous Integration.

### CI Workflow Steps

1. Triggered on push to `main` branch
2. Builds Docker image
3. Logs in to Docker Hub using GitHub Secrets
4. Pushes image to Docker Hub

### Secrets Used

Stored in:

```
GitHub Repository → Settings → Secrets and variables → Actions
```

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`

Secrets ensure credentials are **secure and not hard-coded**.

---

## Image Tagging Strategy

Docker image is tagged as:

```text
yourdockerhubusername/port-demo-app:latest
```

### Tagging Reason

* `latest` tag simplifies CI demonstration
* Suitable for learning and validation
* Can be extended to:

  * Version tags (`v1.0.0`)
  * Git commit SHA tags

---

## Architecture Diagram

```
+-----------+
|  Browser  |
+-----------+
      |
      | http://localhost:8080
      v
+----------------+
| Docker Host    |
| Port: 8080     |
+----------------+
      |
      | Port Mapping
      v
+----------------+
| Docker         |
| Container      |
| Flask App      |
| Port: 5000     |
+----------------+
```

---

## Decisions Made

### 1. Used Flask

* Lightweight framework
* Minimal setup
* Ideal for demo and learning purposes

### 2. Different Host and Container Ports

* Shows Docker networking knowledge
* Demonstrates real-world port mapping
* Prevents host port conflicts

### 3. Used GitHub Actions

* Industry-standard CI tool
* Easy Docker integration
* Secure secret management

### 4. Used Docker Compose

* Simplifies container management
* Cleaner configuration
* Scalable for future services

---

## Conclusion

This project demonstrates:

* Docker containerization
* Port mapping concepts
* CI automation
* Secure credential handling
* Real-world DevOps practices

```

---


