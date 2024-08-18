from fastapi import APIRouter, Depends, HTTPException, Request

import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from sqlalchemy import select

from ..authentification.schemes import Employee_request, Employee_response, UserCreate, UserRead, UserUpdate

from ..authentification.UserManager import get_user_manager
from ..authentification.backend import auth_backend

from src.connection_to_pg import get_async_session
from src.authentification.models import Employee, AccessToken

from .utils import Convert_user_pydentic

fastapi_users = FastAPIUsers[Employee, int](
    get_user_manager,
    [auth_backend],
)

all_auth_router = APIRouter()

all_auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/bearer",
    tags=["auth"],
)
all_auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@all_auth_router.get("/get_manager_info")
async def get_manager_info(request: Request, response_model=Employee_response):
    try: 
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]
        
        
        print("=========================================")
        print(auth_header)
        print(bearer_token)
        print("=========================================")
        async for session in get_async_session():
            async with session.begin():
                token_request = await session.execute(select(AccessToken).filter(AccessToken.token == bearer_token))
                employee_id=token_request.scalars().first().user_id
                
                employee_request= await session.execute(select(Employee).filter(Employee.id == employee_id))
                found_employee=employee_request.scalars().first()
                await session.commit()
        
        if auth_header is None:
            raise HTTPException(status_code=401, detail="Authorization header missing")
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")
    return Convert_user_pydentic(found_employee)
    
def change_inf(old_emp:Employee, new_emp:Employee_response):
    old_emp.email=new_emp.email
    old_emp.name=new_emp.name
    old_emp.surname=new_emp.surname
    old_emp.company=new_emp.company
    old_emp.job_title=new_emp.job_title
    old_emp.birth_date=new_emp.birth_date
    old_emp.phone=new_emp.phone
    old_emp.city=new_emp.city
    return old_emp

@all_auth_router.post("/change_manager_info")
async def change_manager_info(request: Request,new_info:Employee_request):
    try: 
        
        auth_header = request.headers.get("Authorization")
        bearer_token=auth_header.split(" ")[1]
        
        
        print("=========================================")
        print(auth_header)
        print(bearer_token)
        print("=========================================")
        async for session in get_async_session():
            async with session.begin():
                token_request = await session.execute(select(AccessToken).filter(AccessToken.token == bearer_token))
                employee_id=token_request.scalars().first().user_id
                
                employee_request= await session.execute(select(Employee).filter(Employee.id == employee_id))
                found_employee=employee_request.scalars().first()
                res= change_inf(found_employee, new_info)
                await session.commit()
                
        if auth_header is None:
            raise HTTPException(status_code=401, detail="Authorization header missing")
    except Exception as e:
       print(f"Unexpected error: {e}")
       raise HTTPException(status_code=500, detail="Internal server error")
    return Convert_user_pydentic(res)
    
  






































# all_auth_router.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
# all_auth_router.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
# all_auth_router.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )


# current_active_user = fastapi_users.current_user(active=True)
# @all_auth_router.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}