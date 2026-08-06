# 🏠 Smart Home Device Usage Prediction

A Machine Learning project that predicts whether a smart home device is operating **efficiently** or **not efficiently** based on its usage patterns, energy consumption, device age, malfunction history, and user preferences.

---

## 📌 Project Overview

As smart homes become more common, monitoring the efficiency of connected devices is important for reducing energy consumption and improving device performance.

This project uses a **Decision Tree Classifier** to analyze smart home device data and predict whether a device operates efficiently.

The trained model is deployed using **Streamlit**, providing an interactive web interface where users can enter device information and receive instant predictions.

---

## 🎯 Objectives

- Predict smart home device efficiency.
- Analyze factors affecting device performance.
- Provide an easy-to-use web interface.
- Demonstrate the deployment of a Machine Learning model.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📂 Dataset

The dataset contains information about smart home devices, including:

| Feature | Description |
|---------|-------------|
| UsageHoursPerDay | Average device usage per day |
| EnergyConsumption | Energy consumed by the device |
| UserPreferences | User preference setting (0/1) |
| MalfunctionIncidents | Number of device malfunctions |
| DeviceAgeMonths | Age of the device in months |
| DeviceType | Type of smart home device |

### Target Variable

**SmartHomeEfficiency**

- **1** → Efficient
- **0** → Not Efficient

---

## 🤖 Machine Learning Model

Algorithm Used:

- Decision Tree Classifier

The model learns decision rules from historical data and predicts the efficiency of new smart home devices.

---

## 📊 Workflow

```
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Train-Test Split
   │
   ▼
Decision Tree Training
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
Streamlit Web Application
```

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Smart_Home_Device_Usage.git
```

---

### Navigate to Project

```bash
cd Smart_Home_Device_Usage
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Application

```bash
streamlit run app.py
```

---

## 💻 Application Features

- Interactive Streamlit Interface
- Device Type Selection
- User Input Form
- Real-time Prediction
- Decision Tree Machine Learning Model
- Easy-to-use Dashboard

---

## 📁 Project Structure

```
Smart_Home_Device_Usage/
│
├── app.py
├── decision_tree_model.pkl
├── requirements.txt
├── README.md
├── dataset.csv
└── notebook.ipynb
```

---

## 📈 Future Improvements

- Connect with real IoT devices
- Real-time sensor data
- Cloud database integration
- REST API using FastAPI
- Multiple ML model comparison
- Power consumption analytics
- Energy-saving recommendations

---

## 🌐 Real-World Architecture

```
Smart Devices
      │
      ▼
IoT Sensors
      │
      ▼
Backend API
      │
      ▼
Database
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction
      │
      ▼
Dashboard / Mobile App
```

---

## 📸 Screenshots

Add screenshots of your Streamlit application here.

---

## 👨‍💻 Author

**Tufail Abbas**

Computer Science Student

University of Peshawar

---

## 📄 License

This project is developed for educational purposes.