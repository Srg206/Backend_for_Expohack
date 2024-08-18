import uuid
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from typing import Optional

from .models import Employee
from .models import get_user_db
from ..settings import settings


class UserManager(UUIDIDMixin, BaseUserManager[Employee, int]):
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET
    
    async def on_after_register(self, user: Employee, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: Employee, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: Employee, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        
async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)