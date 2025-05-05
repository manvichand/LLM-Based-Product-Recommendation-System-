from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Product
from llm_engine import RecommendationEngine
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import random

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
SECRET_KEY = "3adc8d606bbe4541dcd69940e7c0788ccc45d63baaf583bc342e7e0778f6620d"
ALGORITHM = "HS256"

class UserCreate(BaseModel):
    username: str
    password: str
    preferences: dict

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Decodes JWT token and returns the current logged-in user from DB.

    Args:
        token (str): OAuth2 bearer token

    Returns:
        User: SQLAlchemy User object if token is valid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user account with hashed password and saved preferences.

    Args:
        user (UserCreate): Incoming request body containing username, password, preferences
        db (Session): SQLAlchemy database session

    Returns:
        UserCreate: Confirmation of user creation with original payload
    """
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        preferences=user.preferences
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

@router.post("/recommend/")
async def recommend_products(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Generates and returns a recommended product based on the logged-in user's preferences.

    Args:
        current_user (User): The authenticated user object

    Returns:
        List[Dict]: Recommended product(s)
    """
    preferences = current_user.preferences or {"preferred_categories": "Gifts"}
    category = preferences.get("preferred_categories", "Gifts")
    products = db.query(Product).filter(Product.category == category).all()
    if not products:
        raise HTTPException(status_code=404, detail=f"No products found for category: {category}")
    selected = random.sample(products, min(3, len(products)))
    return [{"id": p.id, "name": p.name, "category": p.category, "price": p.price, "features": p.features} for p in selected]