from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    The Settings class holds the configuration settings for the application.

    Each attribute of this class represents a configuration setting.

    Attributes:
        DB_HOST (str): The database host address.
        DB_PORT (int): The port number on which the database is listening.
        DB_USER (str): The username to connect to the database.
        DB_PASS (str): The password to connect to the database.
        DB_NAME (str): The name of the database.
        SECRET_KEY (str): The secret key used for JWT encoding and decoding.
        ALGORITHM (str): The algorithm used for JWT encoding and decoding.

    Properties:
        DATABASE_URL (str): The complete database URL constructed using the DB_HOST, DB_PORT, DB_USER, DB_PASS, and DB_NAME.
    """

    MODE: Literal["DEV", "PROD", "TEST"]
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"

    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
