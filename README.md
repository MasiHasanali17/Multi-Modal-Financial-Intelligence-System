# 💰 Smart Personal Finance & Expense Multi-Modal AI System

An **AI-powered personal finance assistant** that helps users **extract expenses from bills**, **categorize spending**, and **forecast future expenses** using **Machine Learning** and **Multi-Modal AI** techniques.

This project demonstrates **real-world use of AI/ML**, not rule-based scripting.

---

## 🚀 Project Highlights

✅ Multi-Modal AI (Image + Text + Numerical Data)  
✅ Uses **trained ML models** (`.pkl` files)  
✅ OCR + NLP + Machine Learning Forecasting  
✅ Practical, real-life finance use case  
✅ Academic + Resume + Recruiter friendly  

---

## 🧠 Where AI / ML is Used (IMPORTANT)

| Feature | AI / ML Technique |
|------|----------------|
| 🧾 Bill OCR | Computer Vision (EasyOCR) |
| 📊 Expense Category | NLP + ML Classifier |
| 📈 Expense Forecast | Predictive ML Model |
| 🔁 Model Reuse | Saved trained models (`.pkl`) |

✔ This is a **real AI/ML project**, not hard-coded logic.

---

## 🛠️ Technologies Used

- 🐍 Python 3
- ⚡ FastAPI – Backend REST API
- 🎨 Streamlit – Frontend UI
- 👁️ EasyOCR – Bill Text Extraction
- 📚 Scikit-Learn – Machine Learning
- 📦 Joblib – Model Persistence

---





## 📂 Project Structure

```

Smart_Personal_Finance_AI/
│
├── backend/
│   ├── main.py               
│   ├── requirements.txt      
│   └── init.py
│
├── frontend/
│   └── app.py              
│
├── ml_models/
│   ├── ocr_model.py        
│   ├── expense_classifier.py 
│   ├── expense_forecast.py
│   ├── train_classifier.py 
│   ├── train_forecast.py  
│   ├── expense_classifier.pkl
│   ├── vectorizer.pkl   
│   ├── expense_forecast.pkl 
│   └── init.py
│
└── README.md

````

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r backend/requirements.txt
````

---

### 2️⃣ (Optional) Train ML Models

> Already trained models are included.
> Train again only if you want to modify data.

```bash
cd ml_models
python train_classifier.py
python train_forecast.py
```

---

### 3️⃣ Start Backend (FastAPI)

```bash
cd backend
python -m uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

---

### 4️⃣ Start Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

Frontend URL:

```
http://localhost:8501
```

---

## 🧪 Sample Inputs

### 🧾 Bill OCR

Upload:

* Grocery bill
* Restaurant receipt
* Shopping invoice

Example extracted data:

```
Milk 100
Bread 40
Eggs 75
Total: 540.75
```

---

### 📊 Expense Categorization

Input text:

```
Paid 1200 for groceries
Uber ride cost 350
Electricity bill 1800
```

Output:

```
Category: Groceries / Transport / Utilities
```

---

### 📈 Expense Forecast

Uses past spending patterns to predict:

```
Next Month Estimated Expense: ₹18,500
```

---

## 🎓 Academic Explanation (For Viva)

> “This project uses **multi-modal AI**.
> OCR extracts text from bills, an **ML classifier** categorizes expenses using NLP features, and a **forecasting ML model** predicts future spending based on historical data.
> All models are trained and reused from `.pkl` files.”

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**
and should not be used for financial or legal decisions.

---

## ⭐ Project Value

✔ Real AI / ML implementation
✔ Practical real-world application
✔ Strong final-year / portfolio project
✔ Easy to extend with database or cloud





