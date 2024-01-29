from app.posts.dao import PostsDAO
from app.votes.dao import VotesDAO


async def get_response(post_id: int, user_id: int, like: bool):
    return await VotesDAO.find_one_or_none(
        post_id=int(post_id), user_id=int(user_id), like=bool(like)
    )


async def change_rating(id_post: int, rating: int, current_user_id: int, like: bool):
    if like:
        await PostsDAO.update(
            id=int(id_post), rating=PostsDAO.model.rating + int(rating)
        )
    else:
        await PostsDAO.update(
            id=int(id_post), rating=PostsDAO.model.rating - int(rating)
        )

    await VotesDAO.add(
        post_id=int(id_post), user_id=int(current_user_id), like=bool(like)
    )
    await VotesDAO.delete(
        post_id=int(id_post), user_id=int(current_user_id), like=bool(not like)
    )


async def create_vote(id_psot: int, reating: int, current_user_id: int, like: bool):
    if like:
        await PostsDAO.update(
            id=int(id_psot), rating=PostsDAO.model.rating + int(reating)
        )
    else:
        await PostsDAO.update(
            id=int(id_psot), rating=PostsDAO.model.rating - int(reating)
        )

    await VotesDAO.add(
        post_id=int(id_psot), user_id=int(current_user_id), like=bool(like)
    )
