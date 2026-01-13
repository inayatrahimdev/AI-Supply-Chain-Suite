# AI-Supply-Chain-Suite
**Live App:** [https://ai-supply-chain-suite.streamlit.app/](https://ai-supply-chain-suite.streamlit.app/)

A production-ready supply chain intelligence system combining forecasting, risk assessment, and route optimization in a unified Streamlit interface.

---

## Overview

This system tackles real-world supply chain complexity:  

- **Transport:** LSTM predicts delivery deviations  
- **Warehouse:** Prophet forecasts inventory for 30 days  
- **Risk:** Random Forest identifies high-risk operations  
- **Route:** Dijkstra finds cost-efficient paths  

**Business Impact:**

- Streamlines operations and reduces errors  
- Enables proactive risk management  
- Optimizes routes, saving fuel, time, and cost  
- Predicts inventory trends to prevent stockouts/overstock

---

## Dataset

**dynamic_supply_chain_logistics_dataset.csv** (32,065 rows, 26 features)

Covers:

- Transport metrics: GPS, fuel, traffic, weather, driver behavior, fatigue  
- Warehouse metrics: Inventory, loading/unloading, equipment, order status  
- Risk indicators: Port congestion, supplier reliability, customs clearance, delays  
- IoT sensors: Temperature, cargo condition  
- Temporal data: Timestamps for time-series analysis

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
@software{aisupplychainsuite2024,
  title={AI-Supply-Chain-Suite: Multi-Model Predictive Analytics Platform},
  author={inayatrahimdev},
  year={2026},
  url={https://github.com/inayatrahimdev/AI-Supply-Chain-Suite}
}
```

```
