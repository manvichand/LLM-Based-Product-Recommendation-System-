import streamlit as st
import requests
import json

# FastAPI backend URL (update to your deployed URL later)
BASE_URL = "http://127.0.0.1:8000"

st.title("LLM Product Recommendation System")

# Session state to store token
if "token" not in st.session_state:
    st.session_state.token = None

# Login/Register UI
st.header("User Authentication")
auth_option = st.selectbox("Choose an option", ["Register", "Login"])

if auth_option == "Register":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    category = st.selectbox("Preferred Category", ["Home Decor", "Gifts"])
    if st.button("Register"):
        response = requests.post(
            f"{BASE_URL}/api/users/",
            json={"username": username, "password": password, "preferences": {"preferred_categories": category}}
        )
        if response.status_code == 200:
            st.success("Registered successfully! Please log in.")
        else:
            st.error(f"Registration failed: {response.json().get('detail', 'Unknown error')}")

elif auth_option == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(
            f"{BASE_URL}/token",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        if response.status_code == 200:
            st.session_state.token = response.json()["access_token"]
            st.success("Logged in successfully!")
        else:
            st.error(f"Login failed: {response.json().get('detail', 'Unknown error')}")

# Recommendations UI
if st.session_state.token:
    st.header("Get Recommendations")
    if st.button("Fetch Recommendations"):
        response = requests.post(
            f"{BASE_URL}/api/recommend/",
            headers={"Authorization": f"Bearer {st.session_state.token}"}
        )
        if response.status_code == 200:
            products = response.json()
            for product in products:
                st.write(f"**{product['name']}**")
                st.write(f"Category: {product['category']}")
                st.write(f"Price: ${product['price']}")
                st.write(f"Features: {json.dumps(product['features'], indent=2)}")
                st.write("---")
        else:
            st.error(f"Failed to fetch recommendations: {response.json().get('detail', 'Unknown error')}")
