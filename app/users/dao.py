from app.dao.base import BaseDAO
from app.users.models import Users
from app.database import async_session_maker

class UsersDAO(BaseDAO):
    model = Users

