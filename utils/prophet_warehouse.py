from prophet import Prophet
import pandas as pd

def train_prophet(df):
    df_w = df[['timestamp', 'warehouse_inventory_level']].dropna()
    if df_w.empty:
        raise ValueError("No warehouse inventory data available.")
    
    df_w = df_w.groupby('timestamp').mean().reset_index()
    df_w = df_w.rename(columns={'timestamp': 'ds', 'warehouse_inventory_level': 'y'})

    model = Prophet()
    model.fit(df_w)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return model, forecast