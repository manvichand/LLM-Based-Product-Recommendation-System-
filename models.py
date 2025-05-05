from sqlalchemy import Column, String, Float, JSON, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    """
    SQLAlchemy model for product information.

    Columns:
        id (String): Product identifier (e.g., '85123A')
        name (String): Product name
        description (String): Product description
        category (String): Product category (e.g., 'Home Decor', 'Gifts')
        price (Float): Product price
        features (JSON): Additional metadata
    """
    __tablename__ = "products"
    id = Column(String, primary_key=True)  # Alphanumeric StockCode
    name = Column(String)
    description = Column(String)
    category = Column(String)
    price = Column(Float)
    features = Column(JSON)

class User(Base):
    """
    SQLAlchemy model for users.

    Columns:
        username (String): Unique username (primary key)
        hashed_password (String): Hashed user password
        preferences (JSON): User's preference profile
    """
    __tablename__ = "users"
    username = Column(String, primary_key=True)  # Matches auth.py, api.py
    hashed_password = Column(String)
    preferences = Column(JSON)

class Feedback(Base):
    """
    SQLAlchemy model for storing user feedback on products.

    Columns:
        id (Integer): Unique feedback ID
        user_id (String): Username of the user giving feedback
        product_id (String): ID of the product being reviewed
        rating (Float): Feedback rating (1 to 5)
        comment (String): Optional textual feedback
    """
    __tablename__ = "feedback"
    id = Column(String, primary_key=True)  # Unique ID for feedback
    user_id = Column(String)  # Matches User.username
    product_id = Column(String)  # Matches Product.id
    rating = Column(Float)
    comment = Column(String)