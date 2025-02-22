import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from review_flow.db.models import Base


DATABASE_URL = os.getenv("DATABASE_URL")


class Database:
    """
    Database class to manage the database connection
    """

    def __init__(self, database_url: str = DATABASE_URL):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

        # Ensure tables are created at startup
        Base.metadata.create_all(self.engine)

    def get_db(self) -> Session:
        """
        Get a database session

        Returns:
            Session: A database session
        """
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


def get_database_session():
    return next(Database().get_db())
