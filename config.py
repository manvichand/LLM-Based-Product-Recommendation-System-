import logging
import os
"""
Configuration settings for the recommendation system.

Constants:
    ACCESS_TOKEN_EXPIRE_MINUTES (int): JWT token expiry duration
    MODEL_NAME (str): Name of the LLM model to use
    DATABASE_URL (str): SQLite database connection string
    SECRET_KEY (str): Secret key used for JWT
    ALGORITHM (str): JWT algorithm used

Logging:
    Sets up a rotating log file inside the logs directory for tracking events and errors.
"""
ACCESS_TOKEN_EXPIRE_MINUTES = 30
MODEL_NAME = "distilgpt2"
DATABASE_URL = "sqlite:///recommendation.db"
SECRET_KEY = "-"  # Replace with a secure key in production
ALGORITHM = "HS256"
LOG_DIR = "logs"


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "recommendation_system.log"),
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)