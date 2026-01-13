# AI-Supply-Chain-Suite
**Live App:** [https://ai-supply-chain-suite.streamlit.app/](https://ai-supply-chain-suite.streamlit.app/)

A production-ready supply chain intelligence system combining forecasting, risk assessment, and route optimization in a unified Streamlit interface.
Real-time analytics for transport, warehouse, risk, and route optimization using advanced AI models.
---

## Overview

Modern supply chains face dynamic challenges: unpredictable delivery times, warehouse stockouts, operational risks, and inefficient routing. Decisions made reactively often increase costs, delays, and operational bottlenecks.
This system tackles real-world supply chain complexity:  

- **Transport:** LSTM predicts delivery deviations  
- **Warehouse:** Prophet forecasts inventory for 30 days  
- **Risk:** Random Forest identifies high-risk operations  
- **Route:** Dijkstra finds cost-efficient paths
This platform enables organizations to streamline operations, reduce wastage, and make data-driven decisions in real time, ensuring smooth operations and timely responses to emerging issues.

**Business Impact:**

- Streamlines operations and reduces errors  
- Enables proactive risk management  
- Optimizes routes, saving fuel, time, and cost  
- Predicts inventory trends to prevent stockouts/overstock
## 📊 Operational Impact
Module	Operational Impact	Business Benefit
Transport Forecast	Anticipates delivery delays	Minimizes late shipment penalties
Warehouse Forecast	Predicts inventory gaps/oversupply	Reduces storage and stockout costs
Risk Prediction	Highlights high-risk shipments	Prevents operational disruptions
Route Optimization	Identifies optimal delivery paths	Reduces fuel and time costs

Streamlined Decision Making: Centralized dashboard for all supply chain KPIs.

Real-Time Awareness: Predictive alerts empower proactive decisions.

Actionable Insights: Transform raw data into strategic operational actions.

## 🎯 Problems Solved

Delivery Uncertainty:
LSTM-based transport forecasts identify potential deviations from planned delivery schedules, reducing late shipments and operational penalties.

Warehouse Inefficiencies:
Prophet forecasts inventory levels, preventing stockouts and overstocking. Enables proactive inventory planning.

Supply Chain Risks:
Random Forest risk prediction identifies high-risk shipments, supplier issues, or port congestion before they escalate.

Inefficient Routes:
Dijkstra-based route optimization ensures shipments follow cost-effective and fastest paths, saving time and fuel.

---

## Dataset

**dynamic_supply_chain_logistics_dataset.csv** (32,065 rows, 26 features)

Covers:

- Transport metrics: GPS, fuel, traffic, weather, driver behavior, fatigue  
- Warehouse metrics: Inventory, loading/unloading, equipment, order status  
- Risk indicators: Port congestion, supplier reliability, customs clearance, delays  
- IoT sensors: Temperature, cargo condition  
- Temporal data: Timestamps for time-series analysis

## Future Enhancements

Multi-modal data integration (IoT sensor feeds, GPS data)

Dynamic routing with traffic and weather updates

Dashboard alerts for high-risk shipments

API endpoints for third-party ERP integration
---

## Installation

```bash
# Clone repository
git clone https://github.com/your-username/AI-Supply-Chain-Suite.git
cd AI-Supply-Chain-Suite

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Launch dashboard
streamlit run app.py
````

---

## User Guide

1. **Select Module** (sidebar):

   * Dataset Overview
   * Transport Forecast (LSTM)
   * Warehouse Forecast (Prophet)
   * Risk Prediction
   * Route Optimization

2. **Input Data** via sliders or selections

3. **View Results:** Predictions, forecasts, risk levels, or optimized routes

4. **Take Action:** Adjust schedules, routes, and inventory decisions based on insights

---

## Docker Deployment

For future containerized deployment:

```dockerfile
# AI-Supply-Chain-Suite Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Notes:**

* Current deployment: Streamlit Cloud
* Docker ensures portability and cloud readiness
* No Docker Desktop required locally; CI/CD pipelines can build and run this image

---

## Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/new-model`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feature/new-model`)
5. Open a Pull Request

**Suggested improvements:** Model explainability, real-time data integration, multi-objective routing, anomaly detection, automated retraining.

---

## License

MIT License

---

## Citation

```bibtex
@software{aisupplychainsuite2026,
  title={AI-Supply-Chain-Suite: Multi-Model Predictive Analytics Platform},
  author={inayatrahimdev},
  year={2026},
  url={https://github.com/inayatrahimdev/AI-Supply-Chain-Suite}
}

