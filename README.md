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

---

## 📊 Operational Impact

| Module             | Operational Impact                | Business Benefit                  |
|-------------------|---------------------------------|----------------------------------|
| Transport Forecast | Anticipates delivery delays      | Minimizes late shipment penalties |
| Warehouse Forecast | Predicts inventory gaps/oversupply | Reduces storage and stockout costs |
| Risk Prediction    | Highlights high-risk shipments   | Prevents operational disruptions |
| Route Optimization | Identifies optimal delivery paths | Reduces fuel and time costs |

**Additional Benefits:**  
- **Streamlined Decision Making:** Centralized dashboard for all supply chain KPIs  
- **Real-Time Awareness:** Predictive alerts empower proactive decisions  
- **Actionable Insights:** Transform raw data into strategic operational actions  

---

## 🎯 Problems Solved

- **Delivery Uncertainty:** LSTM-based transport forecasts identify potential deviations from planned delivery schedules, reducing late shipments and operational penalties.  
- **Warehouse Inefficiencies:** Prophet forecasts inventory levels, preventing stockouts and overstocking. Enables proactive inventory planning.  
- **Supply Chain Risks:** Random Forest risk prediction identifies high-risk shipments, supplier issues, or port congestion before they escalate.  
- **Inefficient Routes:** Dijkstra-based route optimization ensures shipments follow cost-effective and fastest paths, saving time and fuel.  

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

## Future Enhancements

- Multi-modal data integration (IoT sensor feeds, GPS data)  
- Dynamic routing with traffic and weather updates  
- Dashboard alerts for high-risk shipments  
- API endpoints for third-party ERP integration  

---
