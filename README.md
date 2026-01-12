# AI-Supply-Chain-Suite

**A production-ready supply chain intelligence system combining time-series forecasting, risk assessment, and route optimization in a unified Streamlit interface.**

---

## What This Actually Does

Most supply chain tools treat prediction as a single-model problem. This system acknowledges that supply chains are multi-faceted: delivery times depend on driver behavior and weather patterns, warehouse inventory follows seasonal trends, risk emerges from supplier reliability and port congestion, and routes need real-time optimization. Each domain requires different modeling approaches.

**Key Capabilities:**
- **Transport Forecasting (LSTM):** Predict delivery deviations for proactive scheduling.
- **Warehouse Forecasting (Prophet):** 30-day inventory predictions with uncertainty intervals.
- **Risk Prediction (Random Forest):** Identify high-risk shipments or operational bottlenecks.
- **Route Optimization (Dijkstra):** Find cost-efficient paths between warehouses and destinations.

<img width="954" height="398" alt="Dashboard Preview" src="https://github.com/user-attachments/assets/0f54e0de-ffe9-423d-a625-a26b19b131a5" />

**Business Value:**
- Streamlines operations and reduces human error  
- Enables proactive risk management and timely decision-making  
- Optimizes routes, saving fuel, time, and operational cost  
- Reduces warehouse stockouts and overstocking through predictive inventory management  

---

## Dataset

The system uses a **32,065-row time-series dataset with 26 features**, covering:

- **Transport metrics:** GPS coordinates, fuel consumption, traffic congestion, weather severity, driver behavior, fatigue monitoring  
- **Warehouse metrics:** Inventory levels, loading/unloading times, equipment availability, order fulfillment status  
- **Risk indicators:** Port congestion, supplier reliability, customs clearance time, disruption likelihood, delay probability  
- **IoT sensors:** Temperature monitoring, cargo condition status  
- **Temporal data:** Timestamps for time-series analysis  

**File:** `dynamic_supply_chain_logistics_dataset.csv`  

This dataset **simulates real-world logistics operations** and allows dynamic, predictive analytics for transport, warehouse, and risk management.

---

## Installation & Setup

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

The platform is **interactive and intuitive**, designed for supply chain managers, logistics teams, and business analysts.

### Step 1: Select Module

Use the **sidebar** to select:

* Dataset Overview
* Transport Forecast (LSTM)
* Warehouse Forecast (Prophet)
* Risk Prediction
* Route Optimization

### Step 2: Input Data

* **Transport Forecast:** Adjust sliders for fuel, traffic, weather, driver score, and fatigue.
* **Warehouse Forecast:** Forecast generated automatically from historical inventory.
* **Risk Prediction:** Adjust delay probability, disruption score, port congestion, supplier reliability, and customs time.
* **Route Optimization:** Select start and end locations.

### Step 3: View Results

* Predicted delivery deviation (Transport)
* 30-day inventory forecast (Warehouse)
* Risk level (Low / Medium / High)
* Optimal route and total cost

### Step 4: Make Decisions

* Adjust schedules and transport routes based on predictions
* Plan procurement to avoid stockouts or overstock
* Take preventive action on medium/high-risk shipments

---

## Extending the System

### Adding New Models

1. Create model file in `utils/` (e.g., `utils/demand_forecasting.py`)
2. Implement training function returning model and metadata
3. Add module to `app.py` sidebar and create UI section
4. Use `@st.cache_resource` for model caching

### Integrating Real-Time Data

Replace CSV loading with API calls:

```python
# In preprocessing.py
def load_data_from_api():
    response = requests.get('https://api.supplychain.com/metrics')
    return pd.DataFrame(response.json())
```

### Adding Authentication

Streamlit supports authentication via `streamlit-authenticator` or custom session state. Add before module selection in `app.py`.

### Deployment

**Streamlit Cloud:** Push to GitHub, connect repo to Streamlit Cloud.
**Docker:** Example `Dockerfile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## Contributing

This is an academic project, but contributions are welcome:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improved-risk-model`)
3. Commit changes (`git commit -m 'Add XGBoost risk model'`)
4. Push to branch (`git push origin feature/improved-risk-model`)
5. Open Pull Request

**Areas for improvement**:

* Model explainability (SHAP, LIME)
* Real-time data integration
* Multi-objective route optimization
* Anomaly detection for warehouse inventory
* Model retraining pipelines

---

## License

MIT License - see LICENSE file for details.

---

## Citation

If you use this code in research or projects:

```bibtex
@software{aisupplychainsuite2024,
  title={AI-Supply-Chain-Suite: Multi-Model Predictive Analytics Platform},
  author={inayatrahimdev},
  year={2026},
  url={https://github.com/inayatrahimdev/AI-Supply-Chain-Suite}
}
```

---

## Acknowledgments

Models implemented using TensorFlow, scikit-learn, Prophet, and NetworkX. UI powered by Streamlit.

---

**Questions?** Open an issue or reach out via email.



