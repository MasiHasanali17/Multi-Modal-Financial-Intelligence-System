import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

data = {
    "month": [1, 2, 3, 4, 5, 6],
    "expense": [12000, 13500, 14000, 15000, 16000, 17000]
}

df = pd.DataFrame(data)

X = df[["month"]]
y = df["expense"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "expense_forecast.pkl")
print("Expense forecast model trained")
