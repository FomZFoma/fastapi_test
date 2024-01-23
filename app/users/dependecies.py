from jose import jwt

from fastapi import Depends, HTTPException, Request
from app.config import settings
from jose import ExpiredSignatureError, JWTError

from app.users.dao import UsersDAO


def get_token(request:Request):
    token = request.cookie.get('You_have_access_token')
    if not token: raise JWTError

    return token

async def get_current_uuser(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token,settings.SECRET_KEY,settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Could not validate credentials") 
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
    user_id:str = payload.get('sub')
    if not user_id: raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user: raise HTTPException(status_code=401, detail="Could not validate credentials")

    return user