from fastapi_users.authentication import BearerTransport

from ..settings import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.BEARER_URL,
)

