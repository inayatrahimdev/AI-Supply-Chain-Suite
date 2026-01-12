import pandas as pd

def load_data(path="data/supply_chain_dataset.csv"):
    df = pd.read_csv(path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def fill_missing(df):
    # Fill numeric columns with mean, non-numeric remain unchanged
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    return df