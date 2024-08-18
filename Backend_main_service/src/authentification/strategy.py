from .models import *
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from ..settings import settings

def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.ACCESS_TOKEN_LIFETIME)