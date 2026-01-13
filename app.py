import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from utils.preprocessing import load_data, fill_missing
from utils.lstm_transport import train_lstm
from utils.prophet_warehouse import train_prophet
from utils.risk_prediction import train_risk
from utils.route_optimization import get_best_route

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI-Powered Supply Chain System",
    layout="wide",
    page_icon="🚚"
)

st.title("🚚 AI-Powered Supply Chain Management System")
st.markdown("""
Explore **real-time AI-powered supply chain analytics**:
- Transport forecast (LSTM)
- Warehouse forecast (Prophet)
- Risk prediction (Random Forest)
- Route optimization (Dijkstra)
""")

# -------------------------
# LOAD DATA (FAST)
# -------------------------
@st.cache_data
def load_and_preprocess():
    df = load_data("data/supply_chain_dataset.csv")
    return fill_missing(df)

df = load_and_preprocess()

# -------------------------
# LOAD MODELS ONCE (CRITICAL FIX)
# -------------------------
@st.cache_resource
def load_models():
    with st.spinner("Loading AI models (one-time)..."):
        lstm_model, scaler, seq_len, features = train_lstm(df)
        prophet_model, prophet_forecast = train_prophet(df)
        risk_model, risk_acc = train_risk(df)

    return {
        "lstm": (lstm_model, scaler, seq_len, features),
        "prophet": (prophet_model, prophet_forecast),
        "risk": (risk_model, risk_acc)
    }

MODELS = load_models()

# -------------------------
# SIDEBAR
# -------------------------
section = st.sidebar.radio(
    "Select Module",
    [
        "Dataset Overview",
        "Transport Forecast (LSTM)",
        "Warehouse Forecast (Prophet)",
        "Risk Prediction",
        "Route Optimization"
    ]
)

# -------------------------
# DATASET OVERVIEW
# -------------------------
if section == "Dataset Overview":
    st.subheader("📊 Dataset Overview")
    st.dataframe(df.head(20))
    st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# -------------------------
# TRANSPORT FORECAST (LSTM)
# -------------------------
elif section == "Transport Forecast (LSTM)":
    st.subheader("🚛 Delivery Time Prediction")

    lstm_model, scaler, seq_len, features = MODELS["lstm"]

    col1, col2 = st.columns(2)
    with col1:
        fuel = st.slider("Fuel Consumption Rate", float(df['fuel_consumption_rate'].min()), float(df['fuel_consumption_rate'].max()))
        traffic = st.slider("Traffic Congestion", float(df['traffic_congestion_level'].min()), float(df['traffic_congestion_level'].max()))
        weather = st.slider("Weather Severity", float(df['weather_condition_severity'].min()), float(df['weather_condition_severity'].max()))
    with col2:
        driver = st.slider("Driver Behavior Score", float(df['driver_behavior_score'].min()), float(df['driver_behavior_score'].max()))
        fatigue = st.slider("Fatigue Score", float(df['fatigue_monitoring_score'].min()), float(df['fatigue_monitoring_score'].max()))

    input_vector = np.array([[fuel, traffic, weather, driver, fatigue]])
    repeated = np.repeat(input_vector, seq_len, axis=0)

    scaled = scaler.transform(
        np.hstack([repeated, np.zeros((seq_len, 1))])
    )[:, :len(features)]

    X_pred = scaled.reshape(1, seq_len, len(features))
    pred = lstm_model.predict(X_pred, verbose=0)[0][0]

    st.success(f"Predicted Delivery Deviation: {pred:.3f}")

# -------------------------
# WAREHOUSE FORECAST (PROPHET)
# -------------------------
elif section == "Warehouse Forecast (Prophet)":
    st.subheader("🏭 Inventory Forecast")

    _, forecast = MODELS["prophet"]

    fig = px.line(forecast, x="ds", y="yhat", title="30-Day Inventory Forecast")
    fig.add_scatter(x=forecast["ds"], y=forecast["yhat_lower"], name="Lower Bound", line=dict(dash="dash"))
    fig.add_scatter(x=forecast["ds"], y=forecast["yhat_upper"], name="Upper Bound", line=dict(dash="dash"))

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# RISK PREDICTION
# -------------------------
elif section == "Risk Prediction":
    st.subheader("⚠️ Risk Prediction")

    risk_model, acc = MODELS["risk"]
    st.metric("Model Accuracy", f"{acc*100:.2f}%")

    col1, col2, col3 = st.columns(3)
    with col1:
        delay = st.slider("Delay Probability", float(df['delay_probability'].min()), float(df['delay_probability'].max()))
        disruption = st.slider("Disruption Likelihood", float(df['disruption_likelihood_score'].min()), float(df['disruption_likelihood_score'].max()))
    with col2:
        port = st.slider("Port Congestion", float(df['port_congestion_level'].min()), float(df['port_congestion_level'].max()))
        supplier = st.slider("Supplier Reliability", float(df['supplier_reliability_score'].min()), float(df['supplier_reliability_score'].max()))
    with col3:
        customs = st.slider("Customs Clearance Time", float(df['customs_clearance_time'].min()), float(df['customs_clearance_time'].max()))

    X = np.array([[delay, disruption, port, supplier, customs]])
    risk = risk_model.predict(X)[0]

    st.success(f"Predicted Risk Level: {risk}")

# -------------------------
# ROUTE OPTIMIZATION
# -------------------------
elif section == "Route Optimization":
    st.subheader("🗺️ Route Optimization")

    locations = ['Warehouse', 'A', 'B', 'C', 'Destination']
    start = st.selectbox("Start Location", locations)
    end = st.selectbox("Destination", locations, index=4)

    if start == end:
        st.warning("Start and destination must differ.")
    else:
        path, cost = get_best_route(start, end)
        st.success(" → ".join(path))
        st.metric("Total Cost", f"{cost}$")
