from sqlalchemy import delete, insert, select

from app.database import async_session_maker


class BaseDAO:
    """Base Data Access Object class for interacting with the database."""
    
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Find a single record based on the given filter criteria."""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        """Add a new record to the database."""
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by):
        """Delete records from the database based on the given filter criteria."""
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
