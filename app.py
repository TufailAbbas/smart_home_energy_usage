from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


MODEL_PATH = Path(__file__).with_name("decision_tree_model.pkl")
model = joblib.load(MODEL_PATH)
app = FastAPI(title="Smart Home Efficiency API")


class PredictionInput(BaseModel):
    usage_hours_per_day: float
    energy_consumption: float
    user_preferences: int
    malfunction_incidents: int
    device_age_months: int
    device_type: str


@app.get("/")
def health_check():
    return {"status": "ok", "service": "smart home efficiency API"}


@app.post("/predict")
def predict(data: PredictionInput):
    device_flags = {
        "Lights": int(data.device_type == "Lights"),
        "Security System": int(data.device_type == "Security System"),
        "Smart Speaker": int(data.device_type == "Smart Speaker"),
        "Thermostat": int(data.device_type == "Thermostat"),
    }
    input_data = pd.DataFrame(
        [[
            data.usage_hours_per_day,
            data.energy_consumption,
            data.user_preferences,
            data.malfunction_incidents,
            data.device_age_months,
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
    prediction = int(model.predict(input_data)[0])
    return {"prediction": prediction, "efficient": prediction == 1}