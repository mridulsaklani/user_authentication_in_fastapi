from fastapi import Response
from app.schemas.auth_schema import register_user
from app.services.user_services import user_register_service


async def user_register(data:register_user, response: Response):
    result = user_register_service(data)
    