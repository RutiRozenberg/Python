from http.client import HTTPException

from fastapi import FastAPI, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import field_validator, ValidationError, BaseModel, constr



user_router = APIRouter()


Users={}



class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z_]+$")
    id: int

    @field_validator('id')
    def check_Des(cls, id):
        if id > 100:
            raise ValueError('error')
        return id


def check_admin_password(name: str):
    return name == "d"



@user_router.get("/")
async def user(is_authenticated: bool = Depends(check_admin_password)):
    if is_authenticated:
        return Users
    raise HTTPException(status_code=404, detail="oops... your task didn't find")




@user_router.post("/")
async def add_user(user: User):
    try:
        Users[user.id]=user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"


@user_router.put("/{id}", response_model=User)
async def update_user(id: int, item: User):
    update_item_encoded = jsonable_encoder(item)
    Users[id] = update_item_encoded
    return update_item_encoded



@user_router.delete("/{id}")
async def delete_user(id: int):
    del Users[id]
    return {"message": "Item deleted"}

