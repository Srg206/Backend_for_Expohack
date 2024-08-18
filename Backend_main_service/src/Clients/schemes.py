from pydantic import BaseModel



class Client_response(BaseModel):
    client_id:int
    client_name:str
    client_surname:str
    client_middlename:str
    client_birthdate:str
    client_mobile_phone:str
    client_email:str
    relevant_score:int
    last_company:str
    