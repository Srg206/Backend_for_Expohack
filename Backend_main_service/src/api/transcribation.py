

from pydantic import BaseModel, Field
from src.Base import metadata
from src.connection_to_pg import sync_engine, sync_session

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import Table, func, select, text,Date


transcribation_router = APIRouter()

class TranscribationModel(BaseModel):
    client_id: int 
    call_date: str
    transcribation: str 


def Conver_pydentic(row):
    print(row[0])
    print(row[1])
    print(row[2])

    return TranscribationModel(
        client_id=int(row[1]),
        call_date=str(row[2]),
        transcribation=str(row[3])
    )


@transcribation_router.get("/get_history/{client_id}")
async def get_client_info(client_id:int, request: Request):
    try:
        #Transcribation = Table('transcribation', metadata, autoload_with=sync_engine)   
        result=sync_session.execute(text(f'SELECT * FROM transcribation \nWHERE user_id = {client_id}\nORDER BY call_date ASC;'))
        keys=['id','client_id','call_date','transcribation' ]
        transcribation_list = []
        for row in result:
            print(row)
            pyd_row=Conver_pydentic(row)
            transcribation_list.append(pyd_row)

        return transcribation_list
    
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")    