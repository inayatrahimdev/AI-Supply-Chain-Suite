# AI-Supply-Chain-Suite

**A production-ready supply chain intelligence system combining time-series forecasting, risk assessment, and route optimization in a unified Streamlit interface.**

---

## What This Actually Does

Most supply chain tools treat prediction as a single-model problem. This system acknowledges that supply chains are multi-faceted: delivery times depend on driver behavior and weather patterns, warehouse inventory follows seasonal trends, risk emerges from supplier reliability and port congestion, and routes need real-time optimization. Each domain requires different modeling approaches.

This platform integrates four specialized models:
- **LSTM neural networks** for non-linear delivery time prediction (capturing complex interactions between fuel consumption, traffic, weather, driver fatigue)
- **Facebook Prophet** for warehouse inventory forecasting (handling seasonality and trend decomposition)
- **Random Forest classifiers** for multi-factor risk assessment (combining delay probability, port congestion, supplier reliability, customs clearance)
- **Graph-based route optimization** using Dijkstra's algorithm (finding cost-optimal paths through supply network topologies)

The result: a unified dashboard where operations teams can simulate scenarios, view forecasts, and make data-driven decisions without switching between tools.

---

## Architecture Decisions & Trade-offs

### Why LSTM for Transport?
Delivery time deviation isn't linear. A driver's fatigue score of 0.8 combined with severe weather (0.9) doesn't simply add up—there's a multiplicative effect. LSTM's recurrent structure captures these temporal dependencies and non-linear interactions. Trade-off: requires more data and longer training time than linear regression, but provides superior accuracy for complex patterns.

### Why Prophet for Warehouse?
Warehouse inventory has clear seasonality (holiday spikes, quarterly patterns) and trend components. Prophet excels at decomposing these without manual feature engineering. Alternative ARIMA models require more domain expertise to tune. Trade-off: Prophet is less interpretable than ARIMA but more robust to missing data and outliers.

### Why Random Forest for Risk?
Risk classification involves categorical outcomes (Low/Medium/High) with multiple heterogeneous features. Random Forest handles non-linear boundaries and feature interactions naturally. Alternative: logistic regression would be faster but miss complex risk patterns. Trade-off: RF is less interpretable but provides better accuracy on this dataset.

### Why Dijkstra for Routes?
Route optimization here is deterministic shortest-path. Dijkstra guarantees optimality for non-negative edge weights. Alternative: A* would be faster with heuristics, but our graph is small enough that Dijkstra's O(V²) complexity is acceptable. Trade-off: Dijkstra is simpler to implement and verify correctness.

---

## Dataset

The system uses a 32,065-row time-series dataset with 26 features covering:
- **Transport metrics**: GPS coordinates, fuel consumption, traffic congestion, weather severity, driver behavior, fatigue monitoring
- **Warehouse metrics**: Inventory levels, loading/unloading times, equipment availability, order fulfillment status
- **Risk indicators**: Port congestion, supplier reliability, customs clearance time, disruption likelihood, delay probability
- **IoT sensors**: Temperature monitoring, cargo condition status
- **Temporal data**: Timestamps for time-series analysis

**Data quality**: Missing values are imputed using column means for numeric features. This is a pragmatic choice—production systems would use more sophisticated imputation (KNN, MICE) or handle missingness explicitly in models.

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- 4GB+ RAM (for TensorFlow/LSTM training)
- 2GB+ disk space

### Quick Start

```bash
# Clone repository
git clone https://github.com/inayatrahimdev/AI-Supply-Chain-Suite.git
cd AI-Supply-Chain-Suite

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

The app will launch at `http://localhost:8501`. Models train on first load (cached thereafter).

### Dependency Notes

- **TensorFlow**: Used for LSTM. If you encounter installation issues, use `tensorflow-cpu` instead of `tensorflow` for CPU-only systems.
- **Prophet**: Requires C++ compiler on some systems. On Windows, install Visual C++ Build Tools. On Linux/Mac, install `gcc`/`clang`.
- **NetworkX**: Lightweight graph library for route optimization.

---

## Usage Guide

### Module 1: Dataset Overview
View raw data, column statistics, and data shape. Useful for understanding what features are available before diving into predictions.

### Module 2: Transport Forecast (LSTM)
**Inputs**: Fuel consumption rate, traffic congestion, weather severity, driver behavior score, fatigue score  
**Output**: Predicted delivery time deviation (scaled units)  
**Interpretation**: Higher values indicate greater deviation from scheduled delivery. Use this to proactively adjust routes or schedules.

**Example scenario**: Set fuel consumption to 0.8, traffic to 0.7, weather to 0.9, driver behavior to 0.6, fatigue to 0.8. The model predicts high deviation—consider delaying shipment or switching drivers.

### Module 3: Warehouse Forecast (Prophet)
**Inputs**: None (uses historical warehouse inventory data)  
**Output**: 30-day forecast with uncertainty intervals  
**Interpretation**: Blue line = expected inventory level. Dashed lines = 80% confidence interval. Use lower bound for safety stock planning.

**Example scenario**: If forecast shows inventory dropping below threshold in 15 days, trigger reorder now to account for lead time.

### Module 4: Risk Prediction
**Inputs**: Delay probability, disruption likelihood, port congestion, supplier reliability, customs clearance time  
**Output**: Risk classification (Low/Medium/High)  
**Interpretation**: Model accuracy displayed at top. Adjust sliders to simulate "what-if" scenarios.

**Example scenario**: Supplier reliability drops to 0.3, port congestion rises to 0.9. Model predicts High risk—consider alternative suppliers or ports.

### Module 5: Route Optimization
**Inputs**: Start location, destination  
**Output**: Optimal path and total cost  
**Interpretation**: Uses Dijkstra's algorithm to find shortest path. Cost represents distance/time/fuel.

**Example scenario**: Warehouse → Destination direct costs 30 units. Warehouse → A → B → C → Destination costs 30 units (12+7+6+5). System chooses optimal path based on current graph weights.

---

## Model Performance & Limitations

### LSTM Transport Model
- **Training**: 10 epochs, batch size 32, sequence length 10
- **Limitations**: 
  - Trained on historical data—may not generalize to extreme weather events or new driver patterns
  - Sequence length of 10 may miss longer-term dependencies
  - No explicit handling of missing features during inference
- **Production considerations**: Add model versioning, A/B testing, and retraining pipeline

### Prophet Warehouse Model
- **Forecast horizon**: 30 days
- **Limitations**:
  - Assumes historical patterns continue—may miss sudden demand spikes (e.g., viral product)
  - No external regressors (holidays, promotions) included
  - Uncertainty intervals are symmetric (may underestimate downside risk)
- **Production considerations**: Add external regressors, custom seasonalities, and anomaly detection

### Random Forest Risk Model
- **Accuracy**: Displayed in UI (typically 85-95% depending on data)
- **Limitations**:
  - Trained on historical risk classifications—may not capture novel risk patterns
  - Feature importance not exposed (harder to explain predictions)
  - Binary/multi-class classification—no probability scores for nuanced decisions
- **Production considerations**: Add SHAP values for explainability, probability calibration, and continuous risk scores

### Route Optimization
- **Algorithm**: Dijkstra's shortest path
- **Limitations**:
  - Static graph weights—doesn't account for real-time traffic or road closures
  - No multi-objective optimization (time vs. cost vs. risk)
  - Graph topology is hardcoded—not scalable to large networks
- **Production considerations**: Integrate real-time traffic APIs, add multi-objective optimization (Pareto fronts), and dynamic graph updates

---

## Project Structure

```
AI-Supply-Chain-Suite/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── data/
│   └── supply_chain_dataset.csv  # 32K+ row dataset
└── utils/
    ├── __init__.py
    ├── preprocessing.py        # Data loading and imputation
    ├── lstm_transport.py       # LSTM model for delivery time prediction
    ├── prophet_warehouse.py    # Prophet model for inventory forecasting
    ├── risk_prediction.py      # Random Forest for risk classification
    └── route_optimization.py   # Dijkstra-based route finder
```

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
**Streamlit Cloud**: Push to GitHub, connect repo to Streamlit Cloud.  
**Docker**: Create `Dockerfile`:
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
- Model explainability (SHAP, LIME)
- Real-time data integration
- Multi-objective route optimization
- Anomaly detection for warehouse inventory
- Model retraining pipelines

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
  year={2024},
  url={https://github.com/inayatrahimdev/AI-Supply-Chain-Suite}
}
```

---

## Acknowledgments

Built for Programming for AI LAB (4th Semester). Models implemented using TensorFlow, scikit-learn, Prophet, and NetworkX. UI powered by Streamlit.

---

**Questions?** Open an issue or reach out via email.
