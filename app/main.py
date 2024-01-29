from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from app.posts.router import router as posts_router
from app.users.router import router as users_router
from redis import asyncio as aioredis
from app.config import settings

app = FastAPI()
app.include_router(users_router)
app.include_router(posts_router)

"""
This is the main module of the FastAPI application.
"""

@app.on_event("startup")
def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
