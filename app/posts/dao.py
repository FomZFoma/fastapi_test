from app.dao.base import BaseDAO
from app.posts.models import Posts
from app.database import async_session_maker
from sqlalchemy import  select,desc, update



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
            A list of all posts.
        """
        async with async_session_maker() as session:
            query = (select(cls.model)
                
                    .order_by((cls.model.date), (cls.model.rating))
                    .limit(10))
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def update(cls, **data):
        """
        Update the model with the given data.

        Args:
            **data: The data to update the model with.

        Returns:
            None
        """
        async with async_session_maker() as session:
            query = update(cls.model).values(**data)
            await session.execute(query)
            await session.commit()


        