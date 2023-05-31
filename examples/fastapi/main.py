# pylint: disable=E0611,E0401
from configs.config import TORTOISE_ORM
from fastapi import FastAPI
from routers.user_router import router as UserRouter
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title="FMS Backend APIs")

######## Include the routers ########
app.include_router(UserRouter, tags=["User"])

######################################

######## Connect to Dababase  ########
print("Connect")
print(TORTOISE_ORM)
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True)
######################################
