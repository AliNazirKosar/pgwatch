# pgwatch
REST API for real-time PostgreSQL server monitoring. Register your servers, configure their credentials, and pgwatch automatically checks every 30 seconds whether they are available.

## What does it do?
- Registers PostgreSQL servers with their host, port, and engine type
- Manages credentials securely using reversible encryption
- Automatically checks every 30 seconds whether each server is UP or DOWN
- Exposes a REST API to query the status of servers in real time

## Stack
- **Python 3.12**
- **FastAPI** — async web framework
- **SQLAlchemy 2.0** — async ORM
- **Alembic** — database migrations
- **APScheduler** — background task scheduler
- **asyncpg** — async PostgreSQL driver
- **Cryptography** — password encryption
- **Docker** — containerization
- **Kubernetes** — container orchestration

## Requirements
- Python 3.12+
- PostgreSQL
- Docker Desktop (for containerized deployment)

---

## Option 1 — Local Installation

```bash
# Clone the repository
git clone https://github.com/AliNazirKosar/pgwatch.git
cd pgwatch

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root of the project:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/pgwatch
ENCRYPT_KEY=your_generated_key
```

To generate the encryption key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

### Migrations

```bash
alembic upgrade head
```

### Run

```bash
uvicorn main:app --reload
```

---

## Option 2 — Docker

### Build the image

```bash
docker build -t pgwatch:v1 .
```

### Configure the .env file

```
DATABASE_URL=postgresql+asyncpg://user:password@host.docker.internal:5432/pgwatch
ENCRYPT_KEY=your_generated_key
```

> Note: Use `host.docker.internal` instead of `localhost` so the container can reach your local PostgreSQL.

### Run the container

```bash
docker run -d --name pgwatch-api -p 8000:8000 --env-file .env pgwatch:v1
```

---

## Option 3 — Kubernetes (local)

### Requirements
- Docker Desktop with Kubernetes enabled

### Deploy

```bash
# Apply the deployment and service
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Verify the pod is running
kubectl get pods

# Verify the service is exposed
kubectl get services
```

### Verify

```bash
kubectl get pods
# Expected: pgwatch-deployment-xxx   1/1   Running   0
```

---

## Accessing the API

The API will be available at `http://localhost:8000`.  
Interactive documentation at `http://localhost:8000/docs`.

---

## Endpoints

### Servers

| Method | Route | Description |
|--------|-------|-------------|
| GET | /server | List all servers and their status |
| GET | /server/{id} | Get server details |
| POST | /server | Register a new server |
| PUT | /server/{id} | Update a server |
| DELETE | /server/{id} | Delete a server |

### Credentials

| Method | Route | Description |
|--------|-------|-------------|
| GET | /dbuser | List all credentials |
| GET | /dbuser/{id} | Get credential details |
| POST | /dbuser | Register credentials for a server |
| PUT | /dbuser/{id} | Update credentials |
| DELETE | /dbuser/{id} | Delete credentials |

---

## How monitoring works

1. Register a server with `POST /server`
2. Add its credentials with `POST /dbuser`
3. pgwatch automatically checks every 30 seconds whether the server responds
4. Query the status with `GET /server/{id}` — returns `UP` or `DOWN`