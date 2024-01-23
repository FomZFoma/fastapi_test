from datetime import datetime, timedelta
from fastapi import HTTPException
from passlib.context import CryptContext
from pydantic import EmailStr
from app.config import settings
from app.users.dao import UsersDAO
from jose import jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)
 
def get_password_hash(password):
   return pwd_context.hash(password)

async def authenticate_user(email: EmailStr, password: str):
   user = await UsersDAO.find_one_or_none(email=email)
   if not(user and verify_password(password,user.password)):
      return HTTPException(status_code=404,detail="User not found") 
   return user

async def create_access_token(data:dict)->str:
   to_encode = data.copy()
   expire = datetime.utcnow() + timedelta(minutes=30)
   to_encode.update({'exp':expire})
   encoded_jwt = jwt.encode(
      to_encode,settings.SECRET_KEY,settings.ALGORITHM
   )
   return encoded_jwt