from app.schemas.auth_schema import register_user
from app.exceptions.auth_exceptions import UserDataNotFoundException, UserAlreadyExistsException
from app.utils.hash_utils import hash_email
from app.models.user_model import User
from app.utils.encription_utils import incrept_email
from app.utils.password_utils import hash_password


async def user_register_service(user:register_user):
    if not user:
        raise UserDataNotFoundException()
    
    email_hash = hash_email(user.email)
    
    is_user_exist = await User.find_one(User.email_hash == email_hash)
    if is_user_exist:
        raise UserAlreadyExistsException(email=user.email)
    
    user_dict = user.model_dump(exclude_none=True)
    user_dict['email_hash'] = email_hash
    user_dict['email'] = incrept_email(user.email)
    user_dict['password'] = hash_password(user.password)
    
    
    
    
    
    