# pylint: disable=E0611,E0401
import imp
from typing import List
from configs.config import TORTOISE_ORM
from fastapi import FastAPI, HTTPException
from models.db_models import User_Pydantic, UserIn_Pydantic, Users, Event
from pydantic import BaseModel
from routers.user_router import router as UserRouter
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title="FMS Backend APIs")

######## Include the routers ########
app.include_router(UserRouter, tags=["User"])

######################################

######## Connect to Dababase  ########
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)
######################################
