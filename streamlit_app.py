import joblib
import pandas as pd
import streamlit as st


model = joblib.load("decision_tree_model.pkl")

st.set_page_config(page_title="Smart Home Efficiency Predictor", page_icon="🏠")

st.title("🏠 Smart Home Efficiency Prediction")
st.write("Enter the device details below to predict Smart Home Efficiency.")

device = st.selectbox(
    "Device Type",
    ["Camera", "Lights", "Security System", "Smart Speaker", "Thermostat"],
)
usage = st.slider("Usage Hours Per Day", 0.0, 24.0, 8.0)
energy = st.number_input("Energy Consumption", min_value=0.0, value=50.0)
preference = st.selectbox("User Preference", [0, 1])
malfunction = st.slider("Malfunction Incidents", 0, 20, 0)
age = st.slider("Device Age (Months)", 0, 120, 24)

device_flags = {
    "Lights": int(device == "Lights"),
    "Security System": int(device == "Security System"),
    "Smart Speaker": int(device == "Smart Speaker"),
    "Thermostat": int(device == "Thermostat"),
}

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[
            usage,
            energy,
            preference,
            malfunction,
            age,
            device_flags["Lights"],
            device_flags["Security System"],
            device_flags["Smart Speaker"],
            device_flags["Thermostat"],
        ]],
        columns=[
            "UsageHoursPerDay",
            "EnergyConsumption",
            "UserPreferences",
            "MalfunctionIncidents",
            "DeviceAgeMonths",
            "DeviceType_Lights",
            "DeviceType_Security System",
            "DeviceType_Smart Speaker",
            "DeviceType_Thermostat",
        ],
    )

    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ Smart Home is Efficient")
    else:
        st.error("❌ Smart Home is Not Efficient")