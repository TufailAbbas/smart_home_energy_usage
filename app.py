from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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


@app.get("/", response_class=HTMLResponse)
def home_page():
        return """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Smart Home Efficiency</title>
    <style>
        :root { color-scheme: light; font-family: Georgia, serif; }
        body { margin: 0; min-height: 100vh; background: #eef4f1; color: #17332d; }
        main { width: min(680px, calc(100% - 32px)); margin: 48px auto; }
        .panel { padding: 32px; background: white; border: 1px solid #c8d8d1; border-radius: 12px; box-shadow: 0 16px 40px #17332d18; }
        h1 { margin: 0 0 8px; font-size: clamp(2rem, 6vw, 3.5rem); line-height: 1; }
        p { color: #507168; }
        form { display: grid; gap: 16px; margin-top: 28px; }
        label { display: grid; gap: 6px; font: 600 0.9rem Arial, sans-serif; }
        input, select, button { box-sizing: border-box; width: 100%; padding: 12px; border: 1px solid #a9c0b7; border-radius: 6px; font: 1rem Arial, sans-serif; }
        button { cursor: pointer; background: #17332d; color: white; border-color: #17332d; font-weight: 700; }
        button:hover { background: #2c5b4f; }
        #result { min-height: 24px; margin: 20px 0 0; font: 700 1.1rem Arial, sans-serif; }
        .success { color: #18734a; }
        .failure { color: #a33b32; }
    </style>
</head>
<body>
    <main>
        <section class="panel">
            <h1>Smart Home Efficiency</h1>
            <p>Enter device details to estimate whether the device is operating efficiently.</p>
            <form id="prediction-form">
                <label>Device type
                    <select name="device_type">
                        <option>Camera</option><option>Lights</option><option>Security System</option>
                        <option>Smart Speaker</option><option>Thermostat</option>
                    </select>
                </label>
                <label>Usage hours per day
                    <input name="usage_hours_per_day" type="number" min="0" max="24" step="0.1" value="8" required>
                </label>
                <label>Energy consumption
                    <input name="energy_consumption" type="number" min="0" step="0.1" value="50" required>
                </label>
                <label>User preference
                    <select name="user_preferences"><option value="0">0</option><option value="1">1</option></select>
                </label>
                <label>Malfunction incidents
                    <input name="malfunction_incidents" type="number" min="0" max="20" step="1" value="0" required>
                </label>
                <label>Device age in months
                    <input name="device_age_months" type="number" min="0" max="120" step="1" value="24" required>
                </label>
                <button type="submit">Predict efficiency</button>
            </form>
            <div id="result" role="status"></div>
        </section>
    </main>
    <script>
        const form = document.querySelector("#prediction-form");
        const result = document.querySelector("#result");
        form.addEventListener("submit", async (event) => {
            event.preventDefault();
            const values = Object.fromEntries(new FormData(form));
            ["usage_hours_per_day", "energy_consumption"].forEach((key) => values[key] = Number(values[key]));
            ["user_preferences", "malfunction_incidents", "device_age_months"].forEach((key) => values[key] = Number(values[key]));
            result.className = "";
            result.textContent = "Calculating...";
            try {
                const response = await fetch("/predict", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(values) });
                if (!response.ok) throw new Error("Prediction request failed");
                const data = await response.json();
                result.className = data.efficient ? "success" : "failure";
                result.textContent = data.efficient ? "Efficient device" : "Device is not efficient";
            } catch (error) {
                result.className = "failure";
                result.textContent = "Unable to make a prediction.";
            }
        });
    </script>
</body>
</html>
"""


@app.get("/health")
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