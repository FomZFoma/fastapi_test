from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from app.posts.router import router as posts_router
from app.users.router import router as users_router
from redis import asyncio as aioredis
from app.config import settings

app = FastAPI(
    title='Habr'
)
app.include_router(users_router)
app.include_router(posts_router)

"""
This is the main module of the FastAPI application.
"""

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
