from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_risk(df):
    features = [
        'delay_probability',
        'disruption_likelihood_score',
        'port_congestion_level',
        'supplier_reliability_score',
        'customs_clearance_time'
    ]
    target = 'risk_classification'

    df_model = df[features + [target]].dropna()
    if df_model.empty:
        raise ValueError("No data available for risk prediction.")

    X = df_model[features]
    y = df_model[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return model, acc