from fastapi import Response, HTTPException, APIRouter

from app.schemas.auth_schema import register_user
from app.controllers.auth_controller import user_register



router = APIRouter()

@router.post('/register')
async def handle_user_register(data: register_user, response: Response):
    return user_register(data, response)