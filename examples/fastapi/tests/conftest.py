import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    PYTEST_TORTOISE_ORM_ENV = {
        "connections": {"default": "sqlite://:memory:"},
        "apps": {
            "models": {
                "models": ["models.db_models"],
                "default_connection": "default",
            }
        },
    }
    os.environ["TORTOISE_ORM"] = str(PYTEST_TORTOISE_ORM_ENV)
