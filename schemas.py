from pydantic import BaseModel
from typing import Optional, Dict

class ProductBase(BaseModel):

    """
    Base schema for product attributes.

    Attributes:
        name (str): Product name
        description (str): Product description
        category (str): Product category
        price (float): Product price
        features (dict): Dictionary of product features
    """

    name: str
    description: str
    category: str
    price: float
    features: Dict

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    
    """
    Response schema for returned product details with ID.

    Attributes:
        id (int): Product ID
        Config: Enables ORM mode
    """
    id: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    """
    Schema for user creation request.

    Attributes:
        username (str): Desired username
        password (str): Raw password
        preferences (Optional[Dict]): User preference data
    """
    username: str
    password: str
    preferences: Optional[Dict] = {}

class Token(BaseModel):
    """
    Schema for JWT token response.

    Attributes:
        access_token (str): Token string
        token_type (str): Type of token (usually "bearer")
    """
    access_token: str
    token_type: str

class FeedbackCreate(BaseModel):

    """
    Schema for submitting user feedback.

    Attributes:
        product_id (int): ID of product being rated
        rating (float): Rating value between 1–5
        comment (Optional[str]): Optional user comment
    """
    product_id: int
    rating: float
    comment: Optional[str] = None