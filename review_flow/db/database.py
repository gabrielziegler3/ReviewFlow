import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


DATABASE_URL = os.getenv("DATABASE_URL")


class Database:
    """
    Database class to manage the database connection
    """
    def __init__(self, database_url: str = DATABASE_URL):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

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


database = Database()

def get_database_session():
    return database.get_db()

