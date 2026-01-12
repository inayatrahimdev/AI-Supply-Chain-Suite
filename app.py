import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

st.title("🚚 AI-Powered Supply Chain Management System (Fully Interactive)")
st.markdown("""
Welcome! Explore **real-time AI-powered supply chain analytics**:
- Transport forecast (LSTM)
- Warehouse forecast (Prophet)
- Risk prediction (Random Forest)
- Route optimization (Dijkstra)
""")

# -------------------------
# LOAD AND PREPROCESS DATA
# -------------------------
@st.cache_data
def load_and_preprocess():
    df = load_data("data/supply_chain_dataset.csv")
    df = fill_missing(df)
    return df

df = load_and_preprocess()

# -------------------------
# SIDEBAR MODULE SELECTION
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
# MODULE 1: Dataset Overview
# -------------------------
if section == "Dataset Overview":
    st.subheader("📊 Dataset Overview")
    st.write("Preview and explore the dataset:")
    st.dataframe(df.head(20))
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.info("Includes transport, warehouse, risk metrics, timestamps.")

# -------------------------
# MODULE 2: Transport Forecast (LSTM)
# -------------------------
elif section == "Transport Forecast (LSTM)":
    st.subheader("🚛 Delivery Time Prediction (LSTM)")

    @st.cache_resource
    def get_lstm_model():
        return train_lstm(df)

    lstm_model, scaler, seq_len, features = get_lstm_model()

    st.markdown("### Adjust Inputs for Prediction")
    col1, col2 = st.columns(2)
    with col1:
        fuel = st.slider("Fuel Consumption Rate (L/h)", float(df['fuel_consumption_rate'].min()), float(df['fuel_consumption_rate'].max()), step=0.1)
        traffic = st.slider("Traffic Congestion Level", float(df['traffic_congestion_level'].min()), float(df['traffic_congestion_level'].max()), step=0.01)
        weather = st.slider("Weather Severity", float(df['weather_condition_severity'].min()), float(df['weather_condition_severity'].max()), step=0.01)
    with col2:
        driver = st.slider("Driver Behavior Score", float(df['driver_behavior_score'].min()), float(df['driver_behavior_score'].max()), step=0.01)
        fatigue = st.slider("Fatigue Score", float(df['fatigue_monitoring_score'].min()), float(df['fatigue_monitoring_score'].max()), step=0.01)

    # Prepare input for LSTM
    input_vector = np.array([[fuel, traffic, weather, driver, fatigue]])
    repeated = np.repeat(input_vector, seq_len, axis=0)
    scaled_sequence = scaler.transform(np.hstack([repeated, np.zeros((seq_len, 1))]))[:, :len(features)]
    X_pred = scaled_sequence.reshape(1, seq_len, len(features))

    pred_scaled = lstm_model.predict(X_pred, verbose=0)
    pred = pred_scaled[0][0]

    st.success(f"Predicted Delivery Time Deviation: {pred:.3f} (scaled units)")
    st.info("Higher values → greater deviation from scheduled delivery.")

# -------------------------
# MODULE 3: Warehouse Forecast (Prophet)
# -------------------------
elif section == "Warehouse Forecast (Prophet)":
    st.subheader("🏭 Warehouse Inventory Forecast (Prophet)")

    @st.cache_resource
    def get_prophet_model():
        return train_prophet(df)

    model, forecast = get_prophet_model()

    # Plot forecast
    fig = px.line(forecast, x='ds', y='yhat', title="30-Day Warehouse Inventory Forecast")
    fig.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Lower Bound', line=dict(dash='dash'))
    fig.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Upper Bound', line=dict(dash='dash'))
    st.plotly_chart(fig, use_container_width=True)

    st.info("Blue line = forecast, dashed lines = uncertainty interval")

# -------------------------
# MODULE 4: Risk Prediction
# -------------------------
elif section == "Risk Prediction":
    st.subheader("⚠️ Supply Chain Risk Prediction")

    @st.cache_resource
    def get_risk_model():
        return train_risk(df)

    model, acc = get_risk_model()

    st.metric("Model Accuracy", f"{acc*100:.2f}%")
    st.write("Adjust input values to simulate risk prediction:")

    # Input sliders for risk features
    col1, col2, col3 = st.columns(3)
    with col1:
        delay = st.slider("Delay Probability", float(df['delay_probability'].min()), float(df['delay_probability'].max()), step=0.01)
        disruption = st.slider("Disruption Likelihood Score", float(df['disruption_likelihood_score'].min()), float(df['disruption_likelihood_score'].max()), step=0.01)
    with col2:
        port = st.slider("Port Congestion Level", float(df['port_congestion_level'].min()), float(df['port_congestion_level'].max()), step=0.01)
        supplier = st.slider("Supplier Reliability Score", float(df['supplier_reliability_score'].min()), float(df['supplier_reliability_score'].max()), step=0.01)
    with col3:
        customs = st.slider("Customs Clearance Time", float(df['customs_clearance_time'].min()), float(df['customs_clearance_time'].max()), step=0.1)

    # Make single risk prediction
    input_risk = np.array([[delay, disruption, port, supplier, customs]])
    risk_pred = model.predict(input_risk)[0]

    st.success(f"Predicted Risk Level: {risk_pred}")
    st.info("Risk = Low / Medium / High (dataset dependent)")

# -------------------------
# MODULE 5: Route Optimization
# -------------------------
elif section == "Route Optimization":
    st.subheader("🗺️ Optimal Transport Route")

    locations = ['Warehouse', 'A', 'B', 'C', 'Destination']

    start = st.selectbox("Select Start Location", locations)
    end = st.selectbox("Select Destination", locations, index=4)

    if start == end:
        st.warning("Start and Destination cannot be the same.")
    else:
        path, cost = get_best_route(start=start, end=end)

        st.success(" → ".join(path))
        st.metric("Total Route Cost", f"{cost}$ Total Cost")



