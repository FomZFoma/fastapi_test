from app.dao.base import BaseDAO
from app.votes.models import Votes

class VotesDAO(BaseDAO):
    model = Votes