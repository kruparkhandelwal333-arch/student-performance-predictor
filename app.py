import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Performance Predictor")

study_hours = st.slider("Study Hours", 0, 10)
sleep_hours = st.slider("Sleep Hours", 0, 10)
attendance = st.slider("Attendance (%)", 0, 100)

if st.button("Predict"):
    input_data = np.array([[study_hours, sleep_hours, attendance]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Marks: {round(prediction[0],2)}")

    if study_hours < 3:
        st.write("👉 Increase study hours")
    if sleep_hours < 6:
        st.write("👉 Improve sleep schedule")
    if attendance < 75:
        st.write("👉 Attend more classes")
        