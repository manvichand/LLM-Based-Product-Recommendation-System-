# LLM-Based Product Recommendation System

## Overview
This project implements a **product recommendation system** using **`distilgpt2`**, **FastAPI**, and **Streamlit**, processing the UCI Online Retail Dataset (~3665 unique products). It leverages `distilgpt2` to generate up to **3 personalized product recommendations** based on user preferences, with a **Streamlit UI** for registration, login, and viewing recommendations, and **FastAPI** for backend API endpoints.

## Features

- **Database**: SQLite (`recommendation.db`) with ~3665 products categorized as *Home Decor* or *Gifts*.
- **Dataset**: `onlineretail.csv` (referenced in `proof_of_work.md`).
- **LLM**: `distilgpt2` generates recommendations by processing product metadata and user `preferred_categories`.
- **Endpoints**:
  - `POST /api/users/`: Register users with username, password, and preferences.
  - `POST /token`: Authenticate users, returning JWT tokens.
  - `POST /api/recommend/`: Generate up to 3 LLM-based recommendations.
- **UI**: Streamlit app (`app.py`) for user interaction and recommendation display.
- **Authentication**: JWT-based with password hashing (`passlib`).
- **Monitoring**: Logs to `logs/recommendation_system.log`.
- **Documentation**: Docstrings in Python files; `proof_of_work.md` with endpoint tests and video demo.

## Setup

1. Create and Activate Virtual Environment:
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Windows

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. Run FastAPI Server:bash
   ```bash
    uvicorn main:app --reload
   
4. **Install Dependencies**:
   ```bash
   streamlit run app.py
   
5. Test endpoints (see proof_of_work.md).
    
## Files

1. main.py: FastAPI application.
2. api.py: User and recommendation endpoints.
3. auth.py: Authentication endpoint.
4. app.py: Streamlit UI for user interaction.
5. database.py: SQLAlchemy setup.
6. models.py: Database models.
7. llm_engine.py: RAG pipeline.
8. test_llm.py: RAG pipeline tests.
9. logs/recommendation_system.log: System logs
10. proof_of_work.md: Documentation with endpoint tests.

## Testing

1. Database: check_db.py confirms ~3665 products (e.g., WHITE HANGING HEART T-LIGHT HOLDER).
2. Endpoints: Tested via curl:
3. User registration.
4. Token generation.
5. Recommendations (curl_recommend.png), returning up to 3 products.
6. Streamlit: UI at http://localhost:8501 shows registration, login, and recommendations.
7. LLM: Terminal logs (LLM Response: ...) verify distilgpt2 output.
8. Video Demo: demo.mp4 showcases setup, UI, API, and LLM usage.
