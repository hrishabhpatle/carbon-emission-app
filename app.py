# Updated Streamlit app with all required features
 import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load model
with open('carbon_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🌍 Carbon Emission Predictor")

# Create input fields for ALL required features
# Numerical features
monthly_grocery = st.number_input("Monthly Grocery Bill", value=1000)
vehicle_distance = st.number_input("Vehicle Monthly Distance (Km)", value=0)
waste_bag = st.number_input("Waste Bag Weekly Count", value=1)
tv_hours = st.number_input("TV/PC Usage (hrs/day)", value=2)
internet_hours = st.number_input("Internet Usage (hrs/day)", value=3)
new_clothes = st.number_input("How Many New Clothes Monthly", value=1)

# Categorical features
diet = st.selectbox("Diet", ["omnivore", "vegetarian", "vegan"])
transport = st.selectbox("Transport", ["public", "walk/bicycle", "private"])
body_type = st.selectbox("Body Type", ["normal", "obese", "overweight", "underweight"])
sex = st.selectbox("Sex", ["male", "female"])
recycling = st.multiselect("Recycling Habits", ["Paper", "Plastic", "Glass", "Metal"])

if st.button("Predict"):
    # Create a dataframe with all expected columns
    input_data = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    
    # Fill numerical features
    input_data["Monthly Grocery Bill"] = monthly_grocery
    input_data["Vehicle Monthly Distance Km"] = vehicle_distance
    input_data["Waste Bag Weekly Count"] = waste_bag
    input_data["How Long TV PC Daily Hour"] = tv_hours
    input_data["How Long Internet Daily Hour"] = internet_hours
    input_data["How Many New Clothes Monthly"] = new_clothes
    
    # Fill categorical features
    input_data[f"Diet_encoded"] = 1 if diet == "vegetarian" else (2 if diet == "vegan" else 0)
    input_data[f"Transport_{transport}"] = 1
    input_data[f"Sex_{sex}"] = 1
    input_data[f"Body Type_{body_type}"] = 1
    
    for item in recycling:
        input_data[f"Recycling_{item}"] = 1
    
    # Make prediction
    prediction = model.predict(input_data)
    st.success(f"Estimated Carbon Emission: {prediction[0]:.2f} kg CO₂/month")
