from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}
# Create an instance of SQLAlchemy's AsyncEngine that will interface with the database.
# The engine is created with the database URL from the application settings.
engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

# Create an instance of SQLAlchemy's AsyncSessionmaker.
# This will be used to create new Session objects which are the handle to the database.
# The sessionmaker is configured with the engine and set to not expire objects when commit is called.
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """
    The Base class is the base class for all SQLAlchemy models in this application.
    It's an instance of DeclarativeBase, which is a base class provided by SQLAlchemy for declarative models.
    """

    pass
