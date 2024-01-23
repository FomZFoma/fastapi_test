from app.database import  Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Votes(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    rating = Column(Integer,default=0)


    user = relationship('Users', backref='votes')
    post = relationship('Posts', backref='votes')