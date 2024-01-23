from sqlalchemy import Column, Integer, String
from app.database import Base

class Users(Base):
    """
    The Users class corresponds to the "users" table in our database.

    Each instance of this class represents a row in the table.

    Attributes:
        id (Integer): The primary key for the user. This is unique for each user.
        email (String): The email address of the user. This field is required and must be unique.
        password (String): The password for the user. This field is required.
    """
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)