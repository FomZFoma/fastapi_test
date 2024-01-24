from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Posts(Base):
    """
    Represents a post in the application.

    Attributes:
        id (int): The unique identifier of the post.
        text (str): The content of the post.
        date (datetime): The date and time when the post was created.
        author_id (int): The ID of the user who created the post.
        rating (int): The rating of the post.
        rating_id (int): The ID of the rating associated with the post.
        author (Users): The user who created the post.

    """

    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    date = Column(DateTime())
    author_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer, default=0)
    rating_id = Column(Integer, default=0)

    author = relationship("Users", backref="posts")
