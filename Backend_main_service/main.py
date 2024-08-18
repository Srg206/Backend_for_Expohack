from fastapi import FastAPI
import uvicorn
from src.connection_to_pg import get_async_session
from src.authentification.models import Employee
from src.settings import settings
from src.api.authentification import all_auth_router
from fastapi.middleware.cors import CORSMiddleware
from src.api.get_lid_info import get_lid_router
from src.api.transcribation import *
from src.api.transcribation import transcribation_router
from src.api.assistant import assistant

from src.api.send_email import email_router

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(all_auth_router)
app.include_router(get_lid_router)
app.include_router(assistant)
app.include_router(transcribation_router)
app.include_router(email_router)




# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")