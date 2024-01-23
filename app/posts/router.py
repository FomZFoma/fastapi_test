from datetime import datetime
from fastapi import APIRouter, Depends
from app.posts.dao import PostsDAO


from app.users.dependecies import get_current_user


router = APIRouter(
    prefix="/posts",
    tags=["Посты"],
)

@router.post('/')
async def create_post(post_text: str,current_user = Depends(get_current_user)):
    if not current_user: return "You need login at the wepsite"
    await PostsDAO.add(text = post_text,date = datetime.utcnow(),author_id = current_user.id)
    return "Post created successfully"

@router.get('/')
async def read_top_posts():
    return await PostsDAO.find_all()

@router.patch('plus_vote')
async def plus_vote(id_post, current_user = Depends(get_current_user)):
    await PostsDAO.update(id = int(id_post),rating = PostsDAO.model.rating + 1,rating_id = int(current_user.id))

@router.patch('minus_vote')
async def minus_vote(id_post, current_user = Depends(get_current_user)):
    await PostsDAO.update(id = int(id_post),rating = PostsDAO.model.rating - 1,rating_id = int(current_user.id))