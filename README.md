 # 🌍 Carbon Emission Prediction App

This project is a **Machine Learning web application** built using **Streamlit** that predicts a person's carbon emissions based on their lifestyle and consumption habits. It uses a **Linear Regression** model trained on various features such as diet, transport methods, energy sources, and more.

---

## 📌 Project Overview

- Goal:Predict individual carbon emissions (kg CO₂/month) from lifestyle inputs.
- Dataset: Custom dataset with lifestyle variables and corresponding emissions.
- Model Used: Linear Regression (`scikit-learn`)
- Deployment: Streamlit Cloud

---

## 📊 Features Used

The model uses the following input features:

- Body Type
- Sex
- Diet
- How Often Shower
- Heating Energy Source
- Transport
- Social Activity
- Monthly Grocery Bill
- Frequency of Traveling by Air
- Vehicle Monthly Distance Km
- Waste Bag Size
- Waste Bag Weekly Count
- How Long TV/PC Daily Hour
- How Many New Clothes Monthly
- How Long Internet Daily Hour
- Energy Efficiency
- Recycling
- Cooking With

---

## 🚀 App Demo

Try it live on **Streamlit Cloud**:  
🔗 [Click Here to Launch App](https://your-streamlit-app-link)

---

## 🛠 How to Run Locally

1. **Clone the repository:**
 Create virtual environment (optional but recommended):

 
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run the app:

 
streamlit run app.py
📁 Project Structure
 
carbon-emission-predictor/
│
├── app.py                # Streamlit web app
├── carbon_model.pkl      # Trained ML model
├── Carbon Emission.csv   # Dataset used for training
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
🧠 Model Training Summary
Preprocessing:

Handled missing values

Encoded categorical features (LabelEncoder, OneHotEncoder)

Scaled numeric values using StandardScaler

Model: Linear Regression (scikit-learn)

Metrics:

MSE: 198,913.28

R² Score: 0.8087

Cross-validated R²: ~0.802

📦 Dependencies
pandas

numpy

scikit-learn

streamlit
 

🧑‍💻 Author
Hrishabh Patle
📧hrishabh07patle@gmail.com
🔗 GitHub

📜 License
This project is licensed under the MIT License.
 
---

Let me know if you'd like me to:
- Replace placeholder links (like GitHub repo or Streamlit app) with your actual ones,
- Help generate the `requirements.txt`,
 









