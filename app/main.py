from fastapi import FastAPI

from app.posts.router import router as posts_router
from app.users.router import router as users_router

app = FastAPI()
app.include_router(users_router)
app.include_router(posts_router)

"""
This is the main module of the FastAPI application.
It sets up the FastAPI app and includes the users router.
"""
