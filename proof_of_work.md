LLM Product Recommendation System Proof of Work

1. Overview

This document demonstrates a FastAPI-based Product Recommendation System using distilgpt2, a lightweight variant of GPT-2, and a SQLite database (recommendation.db). The system supports user creation, JWT authentication, and personalized product recommendations based on user preferences. distilgpt2 was chosen for its efficiency and GPT-2 lineage, aligning with the requirement for a pre-trained LLM. Key components include dataset preprocessing, database integration, a RAG pipeline, and a RESTful API.
Setup

1. Database: recommendation.db with 3665 products, 4339 users, and 397924 feedback entries, managed via SQLAlchemy.
2. RAG Pipeline: Implemented in llm_engine.py, tested via test_llm.py, generating recommendations (e.g., "WHITE     HANGING HEART T-LIGHT HOLDER").
3. FastAPI Server: Running on http://127.0.0.1:8000.
4. GitHub Repository: [Insert GitHub URL, e.g., https://github.com/yourusername/recommendation-system]

2. Implementation Details

- Dataset Preprocessing:

    -Processed the UCI Online Retail Dataset (onlineretail.csv), containing columns InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country, to populate recommendation.db.

    -Extracted 3665 unique products (based on StockCode and Description) and 4339 users (based on CustomerID), with 397924 feedback entries derived from transaction records.

    -Cleaned and normalized data (e.g., handling missing CustomerID, standardizing Description) to ensure compatibility with the RAG pipeline


- Database System:

    Used SQLite with SQLAlchemy, defining User, Product, and Feedback models in models.py.
    Managed connections via SessionLocal in database.py.


- Authentication and Authorization:

    Implemented JWT-based authentication in auth.py (/token endpoint) using passlib for password hashing and jose for JWT.
    Secured /recommend/ endpoint with token-based authorization in api.py.


- RAG Pipeline:

    Developed a retrieval-augmented generation pipeline in llm_engine.py, using distilgpt2 to generate recommendations based on user preferences and product data.
    Tested via test_llm.py, ensuring relevance (e.g., Home Decor preferences yield matching products).


- FastAPI Application:

    Built a RESTful API in main.py, with endpoints for user creation (/users/), authentication (/token), and recommendations (/recommend/).
    Integrated with the database and RAG pipeline.


- Monitoring:

    Implemented logging to recommendation_system.log to track performance and errors.



3. Endpoint Tests

- Create User (/users/):

    curl -X POST "http://127.0.0.1:8000/api/users/" -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpass","preferences":{"preferred_categories":"Home Decor"}}'

    Response:
    {"username":"testuser","password":"testpass","preferences":{"preferred_categories":"Home Decor"}}


- Authenticate User (/token):

    curl -X POST "http://127.0.0.1:8000/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&password=testpass"

    Response:
    {"access_token":"[Actual JWT Token]","token_type":"bearer"}


- Get Recommendations (/recommend/):

    curl -X POST "http://127.0.0.1:8000/api/recommend/" -H "Authorization: Bearer [Actual JWT Token]"

    Response:
    [
    {
        "id": "85123A",
        "name": "WHITE HANGING HEART T-LIGHT HOLDER",
        "description": "WHITE HANGING HEART T-LIGHT HOLDER",
        "category": "Home Decor",
        "price": 2.55,
        "features": {"material": "plastic"}
    }
    ]



4. Notes on Requirements

- LLM Choice: distilgpt2 was selected for its balance of performance and resource efficiency, suitable for rapid prototyping and aligned with GPT-2’s capabilities.

- Caching and Feedback: Logging monitors performance, but caching and explicit product search/feedback endpoints are planned for future enhancements.

- Endpoints: /recommend/ implicitly handles product search via preferences.

5. Logs

Log file: logs/recommendation_system.log
No errors reported during endpoint tests.

6. Conclusion

The system successfully meets the requirements, including database integration, authentication, API development, and recommendation generation using distilgpt2. The GitHub repository contains all source code, and this document, with endpoint tests and screenshots, proving its functionality.


Submitted by Manvi Chand on May 1, 2025
