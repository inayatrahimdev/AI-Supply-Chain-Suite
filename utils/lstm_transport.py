import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def train_lstm(df):
    features = [
        'fuel_consumption_rate',
        'traffic_congestion_level',
        'weather_condition_severity',
        'driver_behavior_score',
        'fatigue_monitoring_score'
    ]
    target = 'delivery_time_deviation'

    df_model = df[features + [target]].dropna()
    if df_model.empty:
        raise ValueError("No data available for LSTM training after dropping NaNs.")

    # Scale data
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(df_model)

    # Prepare sequences
    seq_len = 10
    X, y = [], []
    for i in range(seq_len, len(data_scaled)):
        X.append(data_scaled[i - seq_len:i, :-1])  # All features
        y.append(data_scaled[i, -1])               # Target
    X, y = np.array(X), np.array(y)

    if len(X) == 0:
        raise ValueError("Not enough data to create sequences for LSTM.")

    # Build and train model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(seq_len, len(features))))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10, batch_size=32, verbose=0)

    return model, scaler, seq_len, features