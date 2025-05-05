from llm_engine import RecommendationEngine
import json

def test_recommendation():
    
    """
    Tests the LLM-based recommendation generation logic using dummy preferences.

    This function initializes the engine, sends a test preference, and prints the recommendation.
    """
    engine = RecommendationEngine()
    user_prefs = {"preferred_categories": "Home Decor"}
    recommendations = engine.generate_recommendation(user_prefs, [])
    print(json.dumps(recommendations, indent=2))

if __name__ == "__main__":
    test_recommendation()