from fastapi import Depends
from sqlalchemy import Column, Integer, String
from ..Base import Base
from ..connection_to_pg import *
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable,  SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)

class Employee(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, index=True)
    name =Column(String, nullable=False)
    surname =Column(String, nullable=False)
    company=Column(String, nullable=False)
    job_title=Column(String, nullable=False)
    birth_date=Column(String, nullable=False)
    phone=Column(String, nullable=False)
    city=Column(String, nullable=False)
    
    


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):  
    user_id = Column(Integer, primary_key=True, index=True)

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Employee)
    
async def get_access_token_db(session: AsyncSession = Depends(get_async_session)):  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)