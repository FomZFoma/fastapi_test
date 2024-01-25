from sqlalchemy import desc, insert, select, update

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.posts.models import Posts


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
            data = cls.model
            query = (
                select(data)
                .order_by(
                    desc(data.rating), desc(data.date)
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
    async def add(cls, id, **data):
        """
        Add a new record to the database.

        Args:
            **data: Keyword arguments representing the data to be added.

        Returns:
            None
        """
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).where(id=id)
            await session.execute(query)
            await session.commit()
