import joblib
import os

BASE = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE, "expense_classifier.pkl"))
vectorizer = joblib.load(os.path.join(BASE, "vectorizer.pkl"))

def classify_expense(text):
    X = vectorizer.transform([text.lower()])
    pred = model.predict(X)[0]
    prob = max(model.predict_proba(X)[0])

    return {
        "category": pred,
        "confidence": round(float(prob), 2)
    }
