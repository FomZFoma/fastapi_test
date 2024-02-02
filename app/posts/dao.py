from sqlalchemy import desc, join, select, update

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.posts.models import Posts
from app.users.models import Users


class PostsDAO(BaseDAO):
    """
    Data Access Object for Posts model.
    """

    model = Posts

    @classmethod
    async def find_all(cls):
        """
        Find all posts.

        Returns:
            A list of the most liked and fresh posts.
        """
        async with async_session_maker() as session:
            query = (
                select(Posts)
                .order_by(
                    desc(Posts.rating), desc(Posts.date)
                )  # update, now we find the most high rating, and after that the most new
                .limit(10)
            )
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def update(cls, id, **data):
        """
        Update the model with the given data.

        Args:
            **data: The data to update the model with.

        Returns:
            None
        """
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()
    

    @classmethod

    async def merge(cls):
        async with async_session_maker() as session:
            query_join = join(Posts, Users, Posts.author_id == Users.id) 
            query = select(Posts,Users).select_from(query_join)
            result = await session.execute(query)
            response = result.mappings().all()

            return response[len(response)-1]