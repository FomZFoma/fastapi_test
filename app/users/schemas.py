from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    """
    Schema for user authentication.
    """

    email: EmailStr
    password: str
