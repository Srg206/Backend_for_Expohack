
import asyncio
from time import sleep
from typing import List,Dict
from fastapi import APIRouter
from pydantic import BaseModel
from src.connection_to_pg import sync_session
from sqlalchemy import text
assistant = APIRouter()


id=0
prompt_database: List[Dict] = []

    
@assistant.post("/send_prompt")
def send_prompt(user_prompt:str, company_name:str):
    global id
    cur_id=id+1
    id+=1
    new_record={'id':cur_id,"prompt":user_prompt, 'result':None}
    prompt_database.append(new_record)
    response=None
    while not response:
        sleep(1)
        print(prompt_database)
        print(id,"   ", cur_id)
        for i in range(0, len(prompt_database)):
            if prompt_database[i]['id'] == cur_id:           
                print("id")
                if prompt_database[i]['result']!=None:
                    print("result")
                    response=prompt_database[i]['result']
                    del prompt_database[i]
                    
    response=response.replace("hackaton_client_data", "sorted_"+company_name, 1)
    result=sync_session.execute(text(response))              
    rows=result.fetchall()
    result_list = [row._asdict() for row in rows]

    print("result is ", result_list)
    return result_list

@assistant.post("/get_queries")
def get_queries():
    return prompt_database


@assistant.post("/write_result")
def write_result(model_result: List[Dict]):
    print(model_result)
    prompt_database.clear()  # Очищаем prompt_database перед добавлением новых данных
    prompt_database.extend(model_result)  # Добавляем новый список словарей

    return prompt_database 
    
    



    
    