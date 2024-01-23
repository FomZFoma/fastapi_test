from datetime import datetime
from fastapi import APIRouter, Depends
from app.posts.dao import PostsDAO


from app.users.dependecies import get_current_user


router = APIRouter(
    prefix="/posts",
    tags=["Посты"],
)

@router.post('/')
async def create_post(post_text: str, current_user=Depends(get_current_user)):
    """
    Create a new post.

    Args:
        post_text (str): The text content of the post.
        current_user: The current authenticated user.

    Returns:
        str: A success message if the post is created successfully, or an error message if the user is not logged in.
    """
    if not current_user:
        return "You need to login to the website"
    
    await PostsDAO.add(text=post_text, date=datetime.utcnow(), author_id=current_user.id)
    return "Post created successfully"

async def create_post(post_text: str,current_user = Depends(get_current_user)):
    """
    Create a new post.

    Args:
        post_text (str): The text content of the post.
        current_user: The current authenticated user.

    Returns:
        str: A success message if the post is created successfully, or an error message if the user is not logged in.
    """
    if not current_user: return "You need login at the wepsite"
    await PostsDAO.add(text = post_text,date = datetime.utcnow(),author_id = current_user.id)
    return "Post created successfully"

@router.get('/')
async def read_top_posts():
    """
    Read the top posts.

    Returns:
        List[Post]: A list of top posts.
    """
    return await PostsDAO.find_all()

@router.patch('plus_vote')
async def plus_vote(id_post, current_user = Depends(get_current_user)):
    """
    Increase the rating of a post by 1.

    Args:
        id_post: The ID of the post.
        current_user: The current authenticated user.
    """
    await PostsDAO.update(id = int(id_post),rating = PostsDAO.model.rating + 1,rating_id = int(current_user.id))

@router.patch('minus_vote')
async def minus_vote(id_post, current_user = Depends(get_current_user)):
    """
    Decrease the rating of a post by 1.

    Args:
        id_post: The ID of the post.
        current_user: The current authenticated user.
    """
    await PostsDAO.update(id = int(id_post),rating = PostsDAO.model.rating - 1,rating_id = int(current_user.id))