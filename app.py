import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('carbon_model.pkl', 'rb'))

st.title("🌍 Carbon Emission Predictor")

# Collect user input
sex = st.selectbox("Sex", ["male", "female"])
diet = st.selectbox("Diet", ["vegetarian", "non-vegetarian", "vegan"])
monthly_grocery = st.number_input("Monthly Grocery Bill", value=1000)
tv_hours = st.number_input("TV/PC Usage (hrs/day)", value=2)
internet_hours = st.number_input("Internet Usage (hrs/day)", value=3)

# Construct feature vector (simplified example)
# Add all features as required in your model
features = np.array([[monthly_grocery, tv_hours, internet_hours]])  # Adjust this line!

if st.button("Predict"):
    prediction = model.predict(features)
    st.success(f"Estimated Carbon Emission: {prediction[0]:.2f} kg CO₂/month")
