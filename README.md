# FastAPI Prometheus Monitoring

This project demonstrates how to monitor a FastAPI application using Prometheus. It includes a FastAPI application with Prometheus instrumentation and a `docker-compose` setup to run both services together.

## Features

- **FastAPI application** with a sample endpoint and Prometheus metrics
- **Prometheus monitoring** to scrape FastAPI metrics
- **Dockerized setup** using `Dockerfile` and `docker-compose`

## Folder Structure

```
📦 FastAPI Prometheus Monitoring
┣ 📂 __pycache__
┣ 📜 docker-compose.yml
┣ 📜 Dockerfile
┣ 📜 main.py
┣ 📜 prometheus.yml
┣ 📜 requirements.txt
```

## Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Prometheus](https://prometheus.io/docs/introduction/overview/)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally (Without Docker)
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 4. Run Using Docker
```bash
docker-compose up --build
```

## Running Prometheus

Prometheus is configured using the `prometheus.yml` file. To run Prometheus manually:
```bash
prometheus --config.file=prometheus.yml
```

## Endpoints

| Endpoint         | Method | Description                       |
|-----------------|--------|-----------------------------------|
| `/`             | GET    | Returns a random number & status |
| `/items/{id}`   | GET    | Fetches item details             |
| `/metrics`      | GET    | Prometheus metrics endpoint      |

## Monitoring with Prometheus

Once the containers are running:

- **FastAPI** runs at: [http://localhost:8000](http://localhost:8000)
- **Prometheus** runs at: [http://localhost:9090](http://localhost:9090)
- **Metrics exposed at**: [http://localhost:8000/metrics](http://localhost:8000/metrics)

## Stopping Services

To stop the running containers:
```bash
docker-compose down
```

## License

This project is licensed under the MIT License.

---

### 📌 Author
Developed by **Athul-Rameshan-K-V**  
For contributions, issues, or improvements, feel free to open a pull request or an issue.

