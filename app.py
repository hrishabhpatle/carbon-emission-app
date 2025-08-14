import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
with open('carbon_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🌍 Carbon Emission Predictor")

# Numerical Inputs
monthly_grocery = st.number_input("Monthly Grocery Bill", value=1000.0)
vehicle_distance = st.number_input("Vehicle Monthly Distance (Km)", value=0.0)
waste_bag = st.number_input("Waste Bag Weekly Count", value=1.0)
tv_hours = st.number_input("TV/PC Usage (hrs/day)", value=2.0)
internet_hours = st.number_input("Internet Usage (hrs/day)", value=3.0)
new_clothes = st.number_input("How Many New Clothes Monthly", value=1.0)

# Categorical Inputs
diet = st.selectbox("Diet", ["omnivore", "vegetarian", "vegan"])
transport = st.selectbox("Transport", ["public", "walk_bicycle", "private"])  # replace slash with underscore
sex = st.selectbox("Sex", ["male", "female"])

if st.button("Predict"):
    # Create dataframe with all model features set to 0
    input_data = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)

    # Fill numerical features
    input_data["Monthly Grocery Bill"] = monthly_grocery
    input_data["Vehicle Monthly Distance Km"] = vehicle_distance
    input_data["Waste Bag Weekly Count"] = waste_bag
    input_data["How Long TV PC Daily Hour"] = tv_hours
    input_data["How Long Internet Daily Hour"] = internet_hours
    input_data["How Many New Clothes Monthly"] = new_clothes

    # One-hot encode categorical features if they exist in model's features
    diet_col = f"Diet_{diet}"
    transport_col = f"Transport_{transport}"
    sex_col = f"Sex_{sex}"

    for col in [diet_col, transport_col, sex_col]:
        if col in input_data.columns:
            input_data[col] = 1

    # Prediction
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Carbon Emission: {prediction:.2f} kg CO₂/month")
