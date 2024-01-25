from sqlalchemy import Boolean, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Votes(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    like = Column(Boolean)

    user = relationship("Users", backref="votes")
    post = relationship("Posts", backref="votes")
