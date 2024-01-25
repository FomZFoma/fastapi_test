from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.posts.dao import PostsDAO
from app.users.dependecies import get_current_user
from app.votes.dao import VotesDAO

router = APIRouter(
    prefix="/posts",
    tags=["Посты"],
)

@router.post("/create_post")
async def create_post(post_text: str, current_user=Depends(get_current_user)) -> dict:
    """
    Create a new post.

    Args:
        post_text (str): The text content of the post.
        current_user: The current authenticated user.

    Returns:
        str: A success message if the post is created successfully, or an error message if the user is not logged in.
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="You need to login to the website")
    await PostsDAO.add(
        text=post_text, date=datetime.utcnow(), author_id=int(current_user.id)
    )
    return {"message": "Post created successfully"}


@router.get("/")
async def read_top_posts():
    """
    Read the top posts.

    Returns:
        List[Post]: A list of top posts.
    """
    return await PostsDAO.find_all()


@router.patch("plus_vote")
async def plus_vote(id_post, current_user=Depends(get_current_user)) -> dict:
    """
    Increase the rating of a post by 1.

    Args:
        id_post: The ID of the post.
        current_user: The current authenticated user.
    """
    response_true = await VotesDAO.find_one_or_none(
        post_id=int(id_post), user_id=int(current_user.id), like=True
    )
    if response_true:
        raise HTTPException(status_code=404, detail="You already voted to like")
    response_false = await VotesDAO.find_one_or_none(
        post_id=int(id_post), user_id=int(current_user.id), like=False
    )
    if response_false:
        await PostsDAO.update(id=int(id_post), rating=PostsDAO.model.rating + 2)
        await VotesDAO.add(
            post_id=int(id_post), user_id=int(current_user.id), like=True
        )
        await VotesDAO.delete(
            post_id=int(id_post), user_id=int(current_user.id), like=False
        )
    else:
        await PostsDAO.update(
            id=int(id_post),
            rating=PostsDAO.model.rating + 1,
        )
        await VotesDAO.add(
            post_id=int(id_post), user_id=int(current_user.id), like=True
        )
        await VotesDAO.delete(
            post_id=int(id_post), user_id=int(current_user.id), like=False
        )
    return {"message": "Post rating increased by 1"}


@router.patch("minus_vote")
async def minus_vote(id_post, current_user=Depends(get_current_user)) -> dict:
    """
    Decrease the rating of a post by 1.

    Args:
        id_post: The ID of the post.
        current_user: The current authenticated user.
    """
    response_false = await VotesDAO.find_one_or_none(
        post_id=int(id_post), user_id=int(current_user.id), like=False
    )
    if response_false:
        raise HTTPException(status_code=404, detail="You already voted to dislike")
    response_true = await VotesDAO.find_one_or_none(
        post_id=int(id_post), user_id=int(current_user.id), like=True
    )
    if response_true:
        await PostsDAO.update(id=int(id_post), rating=PostsDAO.model.rating - 2)
        await VotesDAO.add(
            post_id=int(id_post), user_id=int(current_user.id), like=False
        )
        await VotesDAO.delete(
            post_id=int(id_post), user_id=int(current_user.id), like=True
        )
    else:
        await PostsDAO.update(
            id=int(id_post),
            rating=PostsDAO.model.rating - 1,
        )
        await VotesDAO.add(
            post_id=int(id_post), user_id=int(current_user.id), like=False
        )
        await VotesDAO.delete(
            post_id=int(id_post), user_id=int(current_user.id), like=True
        )
    return {"message": "Post rating decreased by 1"}
