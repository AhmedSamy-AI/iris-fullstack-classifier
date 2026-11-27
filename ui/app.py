import os

import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://api:8000")

st.set_page_config(page_title="Iris Classifier", page_icon="🌸")
st.title("🌸 Iris Flower Classifier")
st.write("Enter the four measurements (in centimetres) and press **Predict**.")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal length (cm)", 0.1, 10.0, 5.1, 0.1)
    petal_length = st.number_input("Petal length (cm)", 0.1, 10.0, 1.4, 0.1)
with col2:
    sepal_width = st.number_input("Sepal width (cm)", 0.1, 10.0, 3.5, 0.1)
    petal_width = st.number_input("Petal width (cm)", 0.1, 10.0, 0.2, 0.1)

if st.button("Predict", type="primary"):
    # The API expects: {"feature_array": [sepal_len, sepal_wid, petal_len, petal_wid]}
    payload = {"feature_array": [sepal_length, sepal_width, petal_length, petal_width]}
    try:
        resp = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        resp.raise_for_status()
        species = resp.json()["prediction"]["class_name"]
        st.success(f"Predicted species: **{species}**")
    except requests.RequestException as exc:
        st.error(f"Could not reach the API: {exc}")
