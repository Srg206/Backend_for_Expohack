from sqlalchemy import create_engine
from .settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession    
from sqlalchemy.orm import Session, sessionmaker
from typing import AsyncGenerator

def Postgres_asyncpg_URL():
    return f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"


def Postgres_psycopg_URL():
    return f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

sync_engine= create_engine(
    url=Postgres_psycopg_URL()
)

Session = sessionmaker(bind=sync_engine)
sync_session = Session()
        
async_engine=create_async_engine(
    url=Postgres_asyncpg_URL()  
)

async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

        

from sqlalchemy import create_engine
from .settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession    
from sqlalchemy.orm import Session, sessionmaker
from typing import AsyncGenerator

def Postgres_asyncpg_URL():
    return f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"


def Postgres_psycopg_URL():
    return f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

sync_engine= create_engine(
    url=Postgres_psycopg_URL()
)

Session = sessionmaker(bind=sync_engine)
sync_session = Session()
        
async_engine=create_async_engine(
    url=Postgres_asyncpg_URL()  
)

async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

        

