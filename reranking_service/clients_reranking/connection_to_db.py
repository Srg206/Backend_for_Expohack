from .settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession    
from sqlalchemy.orm import Session, sessionmaker
from typing import AsyncGenerator
from sqlalchemy import MetaData


def Postgres_asyncpg_URL():
    return f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"


async_engine=create_async_engine(
    url=Postgres_asyncpg_URL()  
)

SessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
async def get_async_session():
    async with SessionLocal() as session:
        yield session


# async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
metadata=MetaData()