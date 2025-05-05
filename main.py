from fastapi import FastAPI
from api import router as api_router
from auth import router as auth_router

"""
Entry point of the FastAPI application.

Includes and initializes the API and authentication routers.
Registers the LLM-based product recommendation system.
"""

app = FastAPI(title="LLM Product Recommendation System")
app.include_router(api_router, prefix="/api")
app.include_router(auth_router)

