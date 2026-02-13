import streamlit as st
import requests

st.set_page_config(page_title="Finance AI", layout="wide")

st.title("💰 Smart Personal Finance AI")

tab1, tab2, tab3 = st.tabs(["📸 Bill OCR", "🧾 Expense Category", "📊 Forecast"])

with tab1:
    img = st.file_uploader("Upload Bill Image", type=["jpg","png"])
    if img and st.button("Extract Bill"):
        res = requests.post("http://localhost:8000/bill", files={"file": img.getvalue()}).json()
        st.success(res)

with tab2:
    txt = st.text_input("Enter transaction text")
    if st.button("Classify Expense"):
        res = requests.post("http://localhost:8000/classify", json={"text": txt}).json()
        st.info(res)

with tab3:
    month = st.number_input("Month Number", 1, 12, 7)
    if st.button("Predict Expense"):
        res = requests.post("http://localhost:8000/forecast", json={"month": month}).json()
        st.success(res)
