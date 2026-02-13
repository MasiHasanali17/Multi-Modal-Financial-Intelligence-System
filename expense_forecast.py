import joblib
import os
import numpy as np

BASE = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE, "expense_forecast.pkl"))

def predict_next_month(month):
    pred = model.predict(np.array([[month]]))[0]
    return round(float(pred), 2)
