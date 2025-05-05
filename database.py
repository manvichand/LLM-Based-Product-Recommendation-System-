from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///recommendation.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Provides a database session dependency for FastAPI routes.

    Yields:
        Session: SQLAlchemy session instance used to interact with the database.
    """
    db = SessionLocal()
    """
    Sets up the SQLAlchemy database engine and session factory.

    Uses SQLite with compatibility settings and binds it to the ORM.
    """
    try:
        yield db
    finally:
        db.close()

