from asyncio import sleep
import asyncio
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import Table, select
from ..authentification.models import AccessToken, Employee
from ..connection_to_pg import get_async_session
from src.Clients.schemes import Client_response
from src.Base import metadata
from .utils import Convert_client_pydentic, get_table
import asyncpg
from src.connection_to_pg import async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from src.connection_to_pg import get_async_session

from sqlalchemy import func
get_lid_router = APIRouter()

min_score_limit=60
relevant_score_limit=80


@get_lid_router.get("/get_new_lids_info/{amount}")
async def get_manager_info(amount:int, request: Request, response_model=Client_response):
    try:
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]
        
        company_name=""
        async for session in get_async_session():
            async with session.begin():
                token_request = await session.execute(select(AccessToken).filter(AccessToken.token == bearer_token))
                employee_id=token_request.scalars().first().user_id
                
                employee_request= await session.execute(select(Employee).filter(Employee.id == employee_id))
                found_employee=employee_request.scalars().first()
                await session.commit()
                company_name=found_employee.company
        
            async with async_engine.connect() as conn:
                def get_table(connection):
                    return Table("sorted_" + company_name, metadata, autoload_with=connection)

                table = await conn.run_sync(get_table)
            global score_limit
            if amount==-1:
                query = table.select().where(table.c.relevant_score > min_score_limit)
            else:
                query = table.select().where(table.c.relevant_score > min_score_limit).limit(amount)
            result = await session.execute(query)
            rows = result.fetchall()
            response = [row._asdict() for row in rows]
            #response = [Convert_client_pydentic(row) for row in rows]    
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")    
    return response
    
    
    

@get_lid_router.get("/count_new_lids")
async def count_new_lids( request: Request, response_model=Client_response):
    try:
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]
        
        table= await get_table(bearer_token)
        async for session in get_async_session():
            async with session.begin():
                global min_score_limit
                
                query = table.select().where(table.c.relevant_score > min_score_limit)
                result = await session.execute(query)
                rows = result.fetchall()
                count=len(rows)
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")
    return count

@get_lid_router.get("/count_relevant_lids")
async def count_relevant_lids( request: Request, response_model=Client_response):
    try:
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]
        
        table=await  get_table(bearer_token)
        async for session in get_async_session():
            async with session.begin():
                global relevant_score_limit
                
                query = table.select().where(table.c.relevant_score > relevant_score_limit)
                result = await session.execute(query)
                rows = result.fetchall()
                count=len(rows)
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")
    return count




@get_lid_router.get("/get_client_info/{client_id}")
async def get_client_info(client_id:int, request: Request, response_model=Client_response):
    try:
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]
        table=await get_table(bearer_token)
        
        async for session in get_async_session():
            query = table.select().where(table.c.id == client_id)

            result = await session.execute(query)
            row = result.first()
            response = Convert_client_pydentic(row)
            return response
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")    
    
