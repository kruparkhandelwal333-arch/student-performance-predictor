import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Predictor")

# Inputs
study_hours = st.slider("Study Hours", 0, 10, 5)
sleep_hours = st.slider("Sleep Hours", 0, 10, 6)

# Prediction
if st.button("Predict"):
    prediction = model.predict([[study_hours, sleep_hours]])[0]

    st.subheader(f"📊 Predicted Marks: {prediction:.2f}")

    # Performance category
    if prediction < 40:
        st.error("Poor Performance 😟")
    elif prediction < 70:
        st.warning("Average Performance 😐")
    else:
        st.success("Excellent Performance 🔥")

    # Recommendations
    st.subheader("📌 Recommendations")
    if study_hours < 4:
        st.info("👉 Increase study hours for better results")
    if sleep_hours < 6:
        st.info("👉 Get more sleep for improved focus")
    if study_hours >= 6 and sleep_hours >= 7:
        st.success("Great balance! Keep it up 💯")

    # Graph
    st.subheader("📈 Study Hours vs Predicted Marks")

    hours = list(range(1, 11))
    preds = [model.predict([[h, sleep_hours]])[0] for h in hours]

    fig, ax = plt.subplots()
    ax.plot(hours, preds)
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Predicted Marks")
    st.pyplot(fig)
