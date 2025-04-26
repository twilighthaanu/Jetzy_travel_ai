import streamlit as st
from openai_connector import ask_openai
import os

st.set_page_config(page_title="Jetzy Personalized Travel AI ✈️🌍", page_icon="🌎", layout="centered")

# --- Custom Fancy CSS for UI ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    h1 {
        color: #00c6ff;
        text-align: center;
        margin-bottom: 30px;
        font-size: 50px;
        text-shadow: 2px 2px 5px #0072ff;
    }
    div.stButton > button {
        background: linear-gradient(to right, #ff758c, #ff7eb3);
        border: none;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0px 0px 10px 2px #ff7eb3;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(to right, #43cea2, #185a9d);
        box-shadow: 0px 0px 15px 5px #43cea2;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Jetzy Personalized Travel AI ✈️")

# --- Country ➔ State Mapping ---
country_states = {
    "USA": ["California", "New York", "Florida", "Texas", "Washington DC"],
    "India": ["Delhi", "Mumbai", "Kerala", "Rajasthan", "Goa"],
    "Europe": ["Paris", "Rome", "Berlin", "Barcelona", "Amsterdam"],
    "Australia": ["Sydney", "Melbourne", "Perth", "Brisbane"],
    "Japan": ["Tokyo", "Kyoto", "Osaka", "Hokkaido"],
    "Other": ["Please specify your destination"]
}

# --- User Inputs ---
gender = st.selectbox("👤 Select Your Gender:", ["Male", "Female", "Other"], key="gender")
age_group = st.selectbox("🎂 Select Your Age Group:", ["Child", "Teen", "Adult", "Senior"], key="age")
interests = st.multiselect("🎯 Choose Your Interests:", ["Beaches", "Adventure", "Culture", "Shopping", "Nature", "Luxury"], key="interests")
country = st.selectbox("🌎 Select Your Country:", list(country_states.keys()), key="country")
state = st.selectbox(f"🏙️ Select a Place in {country}:", country_states[country], key="state")
transport_mode = st.selectbox("🚗 Preferred Transport Mode:", ["Flight", "Car", "Walk", "Ship"], key="transport")
duration_days = st.slider("📅 Travel Duration (Days):", 1, 30, step=1, key="duration")
budget = st.slider("💵 Select Your Budget ($):", 100, 10000, step=100, key="budget")
custom_query = st.text_input("📝 Anything Specific You Want? (Optional)", key="custom_query")

# --- Plan My Trip Button ---
if st.button("🚀 Plan My Trip"):

    if gender and age_group and interests and country and state and duration_days and budget:

        interests_string = ", ".join(interests)
        final_prompt = (
            f"Suggest a {duration_days}-day travel itinerary for a {age_group.lower()} {gender.lower()} traveler "
            f"visiting {state}, {country} who loves {interests_string}. "
            f"The budget is ${budget}. "
            f"The traveler prefers to travel mostly by {transport_mode.lower()}. "
            f"Include cheap transport options or booking links if possible. "
            f"Please provide a detailed day-by-day itinerary. "
            f"{custom_query if custom_query else ''}"
        )

        with st.spinner("🤔 Planning your perfect trip..."):
            response = ask_openai(final_prompt)
            st.success(response)

            # --- Add Google Search Travel Link ---
            google_link = f"https://www.google.com/search?q=cheap+{transport_mode.lower()}+travel+to+{state}+{country}"
            st.markdown(f"🔗 [Find Cheap {transport_mode} Options for {state}]({google_link})", unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please fill all details properly to generate your personalized plan.")
