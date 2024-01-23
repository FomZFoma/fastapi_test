from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    date = Column(DateTime())
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('Users', backref='posts')