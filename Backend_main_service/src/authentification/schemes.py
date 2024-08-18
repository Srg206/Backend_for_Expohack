
from fastapi_users import schemas
from pydantic import BaseModel


class Employee_response(BaseModel):
    id:int
    email:str
    name:str
    surname:str
    company:str
    job_title:str
    birth_date:str
    phone:str
    city:str
    
class Employee_request(BaseModel):
    email:str
    name:str
    surname:str
    company:str
    job_title:str
    birth_date:str
    phone:str
    city:str

class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    name:str
    surname:str
    company:str
    name:str
    surname:str
    company:str
    job_title:str
    birth_date:str
    phone:str
    city:str


class UserUpdate(schemas.BaseUserUpdate):
    pass