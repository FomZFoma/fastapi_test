from jose import jwt

from fastapi import Depends, HTTPException, Request
from app.config import settings
from jose import ExpiredSignatureError, JWTError

from app.users.dao import UsersDAO


def get_token(request: Request):
    """
    Retrieves the access token from the request cookies.

    Args:
        request (Request): The FastAPI request object.

    Returns:
        str: The access token.

    Raises:
        JWTError: If the access token is not found in the request cookies.
    """
    token = request.cookies.get('You_have_access_token')
    if not token:
        raise JWTError

    return token


async def get_current_user(token: str = Depends(get_token)):
    """
    Retrieves the current user based on the provided access token.

    Args:
        token (str): The access token.

    Returns:
        User: The current user.

    Raises:
        HTTPException: If the access token is expired or invalid, or if the user cannot be found.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user_id: str = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    return user