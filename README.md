# Auth Service

The Auth Service for the Candy-Star project is a microservice for managing user authentication and authorization.

## Contents

- [Technologies](#technologies)
- [Installation and Setup](#installation-and-setup)
- [Running](#running)
- [Running with Docker](#running-with-docker)
- [Database Migrations](#database-migrations)
- [Usage](#usage)
- [Sentry Configuration](#sentry-configuration)
- [Contact](#contact)

## Technologies

- Python 3.10
- FastAPI
- SQLAlchemy (Async)
- Alembic
- JWT
- Docker
- PostgreSQL
- Redis
- RabbitMQ
- Sentry

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Eastwesser/auth-service.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows: .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add the following environment variables:

    ```env
    DATABASE_URL=postgresql+asyncpg://your_db_username:password@localhost:5432/auth_db
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    RABBITMQ_URL=amqp://guest:guest@localhost/
    REDIS_URL=redis://localhost
    SENTRY_DSN=your_sentry_dsn  # Optional, if you use Sentry
    TEST_DATABASE_URL=postgresql+asyncpg://your_db_username:password@localhost:5432/test_auth_db
    ```

## Running

1. Run the service with Uvicorn:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## Running with Docker

1. Build the Docker image:

    ```bash
    docker build -t auth-service .
    ```

2. Run the container:

    ```bash
    docker run -d --name auth-service -p 8000:8000 --env-file .env auth-service
    ```

## Database Migrations

1. Initialize Alembic (already done if you see the `migrations` directory):

    ```bash
    alembic init migrations
    ```

2. Create and apply a migration:

    ```bash
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```

## Usage

The Auth Service provides the following endpoints:

- `POST /auth/token` - obtain a JWT token
- `POST /auth/register` - register a new user

## Sentry Configuration

To integrate with Sentry, add your DSN to the `.env` file:

```env
SENTRY_DSN=your_sentry_dsn
```
Sentry is used for error tracking and performance monitoring.

### Additional Steps to Complete Setup

1. **Make sure Alembic is installed:**

    ```bash
    pip install alembic
    ```

2. **Add your `SENTRY_DSN` to the `.env` file (if using Sentry).**

3. **Run Alembic migrations to create tables in the database:**

    ```bash
    alembic upgrade head
    ```

4. **Ensure all services (PostgreSQL, Redis, RabbitMQ) are running and accessible.**

### Example File Structure

For convenience, here is the file structure of your project:

```plaintext
auth-service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── dependencies/
│   │   ├── __init__.py
│   │   └── dependencies.py
│   ├── crud/
│   │   ├── __init__.py
│   │   └── crud.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── jwt/
│   │   ├── __init__.py
│   │   └── jwt_token_logic.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── redis/
│   │   ├── __init__.py
│   │   └── redis.py
│   ├── rabbit/
│   │   ├── __init__.py
│   │   └── rabbit.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── alembic.ini
├── Dockerfile
├── requirements.txt
├── .env
├── README.md
└── tests/
    ├── test_main.py
    ├── test_error_handling.py
    └── test_auth.py
```

## Example Contents of requirements.txt

```
fastapi
uvicorn
sqlalchemy[asyncpg]
alembic
python-dotenv
python-jose[cryptography]
sentry-sdk
passlib[bcrypt]
aioredis
aio-pika
pydantic
```

### Contact

For questions and suggestions:

Me - eastwesser@gmail.com

GitHub - https://github.com/Eastwesser

© 2024 Candy-Star. All rights reserved.
