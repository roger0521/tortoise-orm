import os


DATABASE_URL = "sqlite://:memory:"

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models.db_models"],
            "default_connection": "default",
        }
    },
}
