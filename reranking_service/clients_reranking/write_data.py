from sqlalchemy import Table
from .connection_to_db import get_async_session, metadata, async_engine


async def write_to_table(table_name, data):
    
    print(f"\nI am going to write {table_name}\n")
    
    
    async with async_engine.connect() as conn:
        def get_table(connection):
            return Table(table_name, metadata, autoload_with=connection)
        
        table = await conn.run_sync(get_table)
        
    async for session in get_async_session():
        async with session.begin():
    
            #print(data[0])
            for client in data:
                for key, value in client.items():
                    if key=="client_passport_no_previous":
                        client[key] = bool(client[key])
                    if value == '':
                        client[key] = None
                insert_stmt = table.insert().values(client)
                await session.execute(insert_stmt)
                



    print(f"\nI`ve written {table_name} \n")
    