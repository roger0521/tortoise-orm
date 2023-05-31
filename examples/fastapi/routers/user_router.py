from models.db_models import User_Pydantic, UserIn_Pydantic, Users, Event
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from typing import List

###### Intialize Router ######
router = APIRouter()


class Status(BaseModel):
    message: str


@router.get("/users", response_model=List[User_Pydantic])
async def get_users():
    event = await Event.create(name="Test")
    print(event.id)
    return await User_Pydantic.from_queryset(Users.all())


@router.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@router.put(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@router.delete(
    "/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}}
)
async def delete_user(user_id: int):
    deleted_count = await Users.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
