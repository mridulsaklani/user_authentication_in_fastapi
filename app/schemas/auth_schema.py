from pydantic import BaseModel, Field

class register_user(BaseModel):
    name: str = Field(..., min_length=8)
    username: str = Field(..., min_length=8, max_length=34)
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" )
    phone: str = Field( ..., min_length=10,  max_length=15, regex=r"^\d+$")
    password: str = Field(..., min_length=8,  regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$")
