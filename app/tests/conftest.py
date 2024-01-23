import asyncio
from datetime import datetime
import json
import pytest
from sqlalchemy import insert
from app.database import Base,async_session_maker,engine
from app.config import settings
from app.users.models import Users
from app.posts.models import Posts
from fastapi.testclient import TestClient
from httpx import AsyncClient
from app.main import app as fastapi_app

@pytest.fixture(scope="session", autouse=True)
async def prepare_database():

    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    users = open_mock_json("users")
    posts = open_mock_json("posts")
    for post in posts:
        post['date'] = datetime.strptime(post['date'], '%Y-%m-%dT%H:%M:%S.%f')

    async with async_session_maker() as session:
        add_users = insert(Users).values(users)
        add_post = insert(Posts).values(posts)

        await session.execute(add_users)
        await session.execute(add_post)

        await session.commit()



@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session
