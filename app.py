
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("outputs/titanic_model.pkl")
features = joblib.load("outputs/model_features.pkl")

st.title("Titanic Survival Prediction")
st.write("Upload passenger data to predict survival.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    data = data[features]

    predictions = model.predict(data)
    probabilities = model.predict_proba(data)

    results = data.copy()
    results["Prediction"] = [
        "Survived" if p == 1 else "Not Survived"
        for p in predictions
    ]
    results["Survival Probability (%)"] = (
        probabilities[:, 1] * 100
    ).round(2)

    st.subheader("Prediction Results")
    st.dataframe(results)

    st.download_button(
        "Download Predictions",
        results.to_csv(index=False),
        "titanic_predictions.csv",
        "text/csv"
    )
