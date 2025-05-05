from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product

engine = create_engine("sqlite:///recommendation.db")
Session = sessionmaker(bind=engine)
session = Session()

products = session.query(Product).all()
print(f"Total products: {len(products)}")
for p in products[:10]:
    print(f"ID: {p.id}, Name: {p.name}, Category: {p.category}")
