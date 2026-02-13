import sys
import os

# 🔧 FIX: add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from ml_models.ocr_model import extract_bill_text
from ml_models.expense_classifier import classify_expense
from ml_models.expense_forecast import predict_next_month

app = FastAPI(title="Smart Personal Finance AI")

class TextInput(BaseModel):
    text: str

class MonthInput(BaseModel):
    month: int

@app.get("/")
def home():
    return {"status": "Finance AI Running Successfully"}

@app.post("/bill")
async def analyze_bill(file: UploadFile = File(...)):
    content = await file.read()
    return extract_bill_text(content)

@app.post("/classify")
def classify(data: TextInput):
    return classify_expense(data.text)

@app.post("/forecast")
def forecast(data: MonthInput):
    return {
        "predicted_expense": predict_next_month(data.month)
    }
