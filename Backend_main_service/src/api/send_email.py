

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import select

from src.authentification.models import AccessToken, Employee
from src.connection_to_pg import get_async_session
from src.settings import settings

from src.api.get_lid_info import get_client_info

import json
import time
import smtplib
from email.message import EmailMessage

from src.settings import settings
email_router = APIRouter()

async def get_company(bearer_token:str):  
    company_name=""
    async for session in get_async_session():
        async with session.begin():
            token_request = await session.execute(select(AccessToken).filter(AccessToken.token == bearer_token))
            employee_id=token_request.scalars().first().user_id
            
            employee_request= await session.execute(select(Employee).filter(Employee.id == employee_id))
            found_employee=employee_request.scalars().first()
            await session.commit()
            company_name=found_employee.company
    return company_name
templates={
    "d2":"""Здравствуйте username, если вы давно хотели получить страховку, предлагаем вам ознакомиться с перечнем наших услуг https://www.d2insur.ru/""",
    "expobank":  """Здравствуйте username, хотели бы предложить вам воспользоваться Услугой нашего банка https://expobank.ru/""",
    "expocar": """Здравствуйте username, если вы давно хотели приобрести машину, предлагаем вам воспользоваться нашим автосалоном https://expocar.ru/""",
    "hvoya": """Здравствуйте username, если вы решили отдохнуть, предлагаем вам посетить наш парк-отель "Хвоя". Вы получите новые впечатления и незабываемый отпуск https://hvoya-park.ru/""",
    "leasing": """Здравствуйте username, если вы не хотите покупать авто, то можете воспользоваться лизингом, предоставляемый нашей компанией""",
    "autoexpress": """Здравствуйте username, если вы работаете в сфере связанной с автомобильным рынком, то советуем ознакомться с перечнем услуг компании автоэкспресс"""
}


def email_on_background(client_email,client_name,client_username,company_name):
    try:
        
        email = EmailMessage()
        email['Subject'] = templates[company_name].replace("username"," "+client_name+" "+client_username,1)
        email['From'] = settings.SMTP_SENDER
        email['To'] = client_email
        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_SENDER, settings.SMTP_PASS)
            server.send_message(email)
    except Exception as e:
        print(e)    
    

@email_router.get("/send_email/{client_id}")
async def send_email(client_id:int,request: Request):
    try:
        inf=await get_client_info(client_id,request)
        print(inf)
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]

        company_name=await get_company(bearer_token)
        print(company_name)
        #email_on_background(inf.client_email, inf.client_name,inf.client_surname, company_name)
        email_on_background("czukanov_s@list.ru", inf.client_name,inf.client_surname, company_name)
        
        
        #print(company_name)
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")
    
