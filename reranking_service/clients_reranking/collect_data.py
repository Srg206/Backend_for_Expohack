from .connection_to_db import get_async_session, async_engine, metadata
from sqlalchemy import  MetaData, Table, select, table
from .settings import settings

async def collect_data(table_name: str):
    async with async_engine.connect() as conn:
        def get_table(connection):
            return Table(table_name, metadata, autoload_with=connection)

        table = await conn.run_sync(get_table)
    
    async for session in get_async_session():
        async with session.begin():
            query = table.select() 
            result = await session.execute(query)
            
            
            columns = table.columns.keys()

            # Преобразование данных в список словарей
            data = [dict(zip(columns, row)) for row in result]
    return data
            