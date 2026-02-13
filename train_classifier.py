import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

data = {
    "text": [
        "zomato food order", "pizza restaurant",
        "uber ride travel", "bus ticket",
        "amazon shopping", "flipkart purchase",
        "electricity bill payment", "water bill"
    ],
    "label": [
        "Food", "Food",
        "Travel", "Travel",
        "Shopping", "Shopping",
        "Utilities", "Utilities"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "expense_classifier.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Expense classifier trained")
