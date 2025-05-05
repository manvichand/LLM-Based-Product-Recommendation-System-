from transformers import pipeline
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product
from typing import List, Dict

class RecommendationEngine:
    """
        Handles product retrieval and recommendation generation using a pre-trained language model.

        Args:
            model_name (str): The name of the pre-trained language model to use.

        Attributes:
            generator: HuggingFace text-generation pipeline object.
            db (Session): SQLAlchemy session instance.
        """   
    def __init__(self, model_name: str = "distilgpt2"):
        self.generator = pipeline("text-generation", model=model_name)
        self.db: Session = SessionLocal()

    def retrieve_products(self, category: str) -> List[Dict]:
        """
        Retrieves a list of products filtered by category from the database.

        Args:
            category (str): The category to filter products by.

        Returns:
            List[Dict]: A list of product dictionaries with essential product details.
        """    
        products = self.db.query(Product).filter(Product.category == category).limit(5).all()
        return [{"id": p.id, "name": p.name, "description": p.description, "category": p.category, "price": p.price, "features": p.features} for p in products]

    def generate_recommendation(self, user_prefs: Dict, products: List[Dict]) -> List[Dict]:
        """
        Generates a personalized product recommendation using the language model.

        Args:
            user_prefs (Dict): Dictionary of user preferences (must include 'preferred_categories').
            products (List[Dict]): (Currently unused) Placeholder for potential fine-grained filtering.

        Returns:
            List[Dict]: A single-item list containing one recommended product.
        """
        category = user_prefs.get("preferred_categories", "Home Decor")
        retrieved_products = self.retrieve_products(category)
        product_info = "\n".join([f"- {p['name']}: {p['description']} (${p['price']})" for p in retrieved_products])
        prompt = f"Based on products for {category}:\n{product_info}\nRecommend one product for the user."
        response = self.generator(
            prompt,
            max_new_tokens=50,
            num_return_sequences=1,
            truncation=True,
            clean_up_tokenization_spaces=True
        )[0]["generated_text"]
        return [next((p for p in retrieved_products if p["name"].lower() in response.lower()), retrieved_products[0])]