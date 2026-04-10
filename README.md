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

## Requirements

- Python 3.12+
- PostgreSQL

## Installation

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

## Configuration

Create a `.env` file in the root of the project:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/pgwatch
ENCRYPT_KEY=your_generated_key
```

To generate the encryption key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## Migrations

```bash
# Apply database migrations
alembic upgrade head
```

## Run

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive documentation at `http://localhost:8000/docs`.

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

## How monitoring works

1. Register a server with `POST /server`
2. Add its credentials with `POST /dbuser`
3. pgwatch automatically checks every 30 seconds whether the server responds
4. Query the status with `GET /server/{id}` — returns `UP` or `DOWN`

API REST para monitorizar servidores PostgreSQL en tiempo real. Registra tus servidores, configura sus credenciales y pgwatch comprueba automáticamente cada 30 segundos si están disponibles.

## ¿Qué hace?

- Registra servidores PostgreSQL con su host, puerto y motor
- Gestiona credenciales de forma segura con cifrado reversible
- Comprueba automáticamente cada 30 segundos si cada servidor está UP o DOWN
- Expone una API REST para consultar el estado de los servidores en tiempo real

## Stack

- **Python 3.12**
- **FastAPI** — framework web async
- **SQLAlchemy 2.0** — ORM async
- **Alembic** — migraciones de base de datos
- **APScheduler** — scheduler de tareas en background
- **asyncpg** — driver async para PostgreSQL
- **Cryptography** — cifrado de contraseñas

## Requisitos

- Python 3.12+
- PostgreSQL

## Instalación

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/pgwatch.git
cd pgwatch

# Crea el entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instala las dependencias
pip install -r requirements.txt
```

## Configuración

Crea un fichero `.env` en la raíz del proyecto:

```
DATABASE_URL=postgresql+asyncpg://usuario:password@localhost:5432/pgwatch
ENCRYPT_KEY=tu_clave_generada
```

Para generar la clave de encriptación:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## Migraciones

```bash
# Crea la base de datos y aplica las migraciones
alembic upgrade head
```

## Arrancar

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`.
La documentación interactiva en `http://localhost:8000/docs`.

## Endpoints

### Servidores
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /server | Lista todos los servidores y su estado |
| GET | /server/{id} | Detalle de un servidor |
| POST | /server | Registra un servidor nuevo |
| PUT | /server/{id} | Actualiza un servidor |
| DELETE | /server/{id} | Elimina un servidor |

### Credenciales
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /dbuser | Lista todas las credenciales |
| GET | /dbuser/{id} | Detalle de unas credenciales |
| POST | /dbuser | Registra credenciales para un servidor |
| PUT | /dbuser/{id} | Actualiza credenciales |
| DELETE | /dbuser/{id} | Elimina credenciales |

## Cómo funciona el monitoreo

1. Registra un servidor con `POST /server`
2. Añade sus credenciales con `POST /dbuser`
3. pgwatch comprueba automáticamente cada 30 segundos si el servidor responde
4. Consulta el estado con `GET /server/{id}` — devuelve `UP` o `DOWN`
