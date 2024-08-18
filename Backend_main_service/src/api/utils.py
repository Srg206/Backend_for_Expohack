
from sqlalchemy import Table, select
from src.connection_to_pg import get_async_session
from src.authentification.models import AccessToken, Employee
from src.authentification.schemes import Employee_response
from src.Clients.schemes import Client_response

from src.Base import metadata
from src.connection_to_pg import async_engine
def Convert_user_pydentic(user:Employee):
    return Employee_response(id=user.id, email = user.email, name=user.name, surname=user.surname, company=user.company,
                             job_title=user.job_title, birth_date=user.birth_date, phone=user.phone, city=user.city)
    
def Convert_client_pydentic(client):
    return Client_response(client_id=client.id,client_name=client.client_name, client_surname=client.client_sirname, client_middlename=client.client_middle_name,
                  client_birthdate=str(client.client_birthdate), client_mobile_phone=client.client_mobile_phone, 
                  client_email=client.client_email, relevant_score=client.relevant_score, last_company= client.client_company)
    

async def get_table(bearer_token:str):  
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
    return table
    

