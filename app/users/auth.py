from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """Verify if the plain password matches the hashed password."""

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Generate a hash for the given password."""
    return pwd_context.hash(password)


async def authenticate_user(email: EmailStr, password: str):
    """Authenticate a user based on their email and password."""
    user = await UsersDAO.find_one_or_none(email=email)
    if not (user and verify_password(password, user.password)):
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create_access_token(data: dict) -> str:
    """Take a dict and create a JWT token with it."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt
