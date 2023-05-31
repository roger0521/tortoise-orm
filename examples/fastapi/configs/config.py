import os

PYTEST_ENV = os.environ.get("TORTOISE_ORM")
DATABASE_URL = "sqlite://:memory:"

TORTOISE_ORM = (
    {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "host": "localhost",
                    "port": "5432",
                    "user": "postgres",
                    "password": "pgsql-aiplatform@24",
                    "database": "fms",
                },
            }
        },
        "apps": {
            "models": {
                "models": ["models.db_models"],
                "default_connection": "default",
            }
        },
        "_create_db": True,
    }
    if PYTEST_ENV is None
    else PYTEST_ENV
)
