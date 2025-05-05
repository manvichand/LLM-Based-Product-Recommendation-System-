# LLM-Based-Product-Recommendation-System-1.0

## Overview
This project implements a FastAPI-based product recommendation system using `distilgpt2`, a lightweight GPT-2 variant, and a SQLite database (`recommendation.db`). It supports user creation, JWT authentication, and personalized product recommendations via a RAG pipeline.

## Features

- **Database**: SQLite with 3665 products, 4339 users, 397924 feedback entries.
- **Dataset**: Online_retail.csv(referenced in proof of work)
- **Endpoints**: `/users/` (create user), `/token` (authenticate), `/recommend/` (generate recommendations).
- **RAG Pipeline**: Adapts `distilgpt2` for recommendations, tested via `test_llm.py`.
- **Authentication**: JWT-based with password hashing.
- **Monitoring**: Logs to `recommendation_system.log`.
- **Documentation**: Docstrings in all Python files; `proof_of_work.md` with endpoint tests.

## Setup

1. Clone the repository:
   ```bash
   git clone (repo link)
   cd recommendation-system
2. Create and activate a virtual environment:
     ```bash
   git clone (repo link)
    Windows: venv\Scripts\activate
4. Install dependencies:
  pip install -r requirements.txt
5. Run the FastAPI server:
    uvicorn main:app --reload
6. Test endpoints (see proof_of_work.md).
   
## Files

1. main.py: FastAPI application.
2. api.py: User and recommendation endpoints.
3. auth.py: Authentication endpoint.
4. database.py: SQLAlchemy setup.
5. models.py: Database models.
6. llm_engine.py: RAG pipeline.
7. test_llm.py: RAG pipeline tests.
8. proof_of_work.md: Documentation with endpoint tests.

## Notes

1. Uses distilgpt2 for efficiency, aligned with GPT-2.
2. RAG pipeline ensures effective recommendations.
3. Caching and feedback endpoints planned for future work.
   
# MANVI CHAND
