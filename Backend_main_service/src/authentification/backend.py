from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from .transport import bearer_transport
from .strategy import get_database_strategy

auth_backend = AuthenticationBackend(
    name="bearer",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
