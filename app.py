import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("decision_tree_model.pkl")

st.set_page_config(page_title="Smart Home Efficiency Predictor", page_icon="🏠")

st.title("🏠 Smart Home Efficiency Prediction")
st.write("Enter the device details below to predict Smart Home Efficiency.")

# -----------------------------
# Inputs
# -----------------------------

device = st.selectbox(
    "Device Type",
    [
        "Camera",
        "Lights",
        "Security System",
        "Smart Speaker",
        "Thermostat"
    ]
)

usage = st.slider(
    "Usage Hours Per Day",
    0.0,
    24.0,
    8.0
)

energy = st.number_input(
    "Energy Consumption",
    min_value=0.0,
    value=50.0
)

preference = st.selectbox(
    "User Preference",
    [0,1]
)

malfunction = st.slider(
    "Malfunction Incidents",
    0,
    20,
    0
)

age = st.slider(
    "Device Age (Months)",
    0,
    120,
    24
)

# -----------------------------
# One-Hot Encoding
# -----------------------------

lights = 0
security = 0
speaker = 0
thermostat = 0

if device == "Lights":
    lights = 1

elif device == "Security System":
    security = 1

elif device == "Smart Speaker":
    speaker = 1

elif device == "Thermostat":
    thermostat = 1

# Camera remains all zeros

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    input_data = pd.DataFrame([[
        usage,
        energy,
        preference,
        malfunction,
        age,
        lights,
        security,
        speaker,
        thermostat
    ]],
    columns=[
        'UsageHoursPerDay',
        'EnergyConsumption',
        'UserPreferences',
        'MalfunctionIncidents',
        'DeviceAgeMonths',
        'DeviceType_Lights',
        'DeviceType_Security System',
        'DeviceType_Smart Speaker',
        'DeviceType_Thermostat'
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Smart Home is Efficient")
    else:
        st.error("❌ Smart Home is Not Efficient")