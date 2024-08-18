from sqlalchemy import MetaData, Table, create_engine
from .settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession    
from sqlalchemy.orm import Session, sessionmaker
from typing import AsyncGenerator

def Postgres_URL():
    return f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"


engine= create_engine(
    url=Postgres_URL()
)


Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

# Определение существующей таблицы