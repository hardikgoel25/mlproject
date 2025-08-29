import streamlit as st
import requests
import os

# Load API URL from environment (fallback to localhost if not set)
API_URL = os.getenv("API_URL", "http://127.0.0.1:5000/predict")

st.title("🎓 Student Exam Performance Prediction")

# Input fields
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level = st.selectbox(
    "Parental Level of Education", 
    [
        "some high school", "high school", "some college",
        "associate's degree", "bachelor's degree", "master's degree"
    ]
)
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)
writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=70)

# Predict button
if st.button("Predict"):
    payload = {
        "gender": gender,
        "race_ethnicity": ethnicity,
        "parental_level_of_education": parental_level,
        "lunch": lunch,
        "test_preparation_course": test_prep,
        "reading_score": reading_score,
        "writing_score": writing_score
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"📊 Predicted Score: **{result['prediction']}**")
        else:
            st.error(f"❌ API Error {response.status_code}: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Could not connect to API. Is Flask running?")
