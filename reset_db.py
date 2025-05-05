from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///recommendation.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Database reset complete")
