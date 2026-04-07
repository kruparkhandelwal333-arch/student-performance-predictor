import streamlit as st
import pickle
import numpy as np
import os

st.title("🎓 Student Performance Predictor")

# Load model safely
model = None

if os.path.exists("model.pkl"):
    try:
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)
    except Exception as e:
        st.error("Error loading model")
        st.write(e)
else:
    st.error("model.pkl file not found")

# Inputs
study_hours = st.slider("Study Hours", 0, 10)
sleep_hours = st.slider("Sleep Hours", 0, 10)
attendance = st.slider("Attendance (%)", 0, 100)

# Prediction
if st.button("Predict"):
    input_data = np.array([[study_hours, sleep_hours, attendance]])

    if model is not None:
        try:
            prediction = model.predict(input_data)
            st.success(f"Predicted Marks: {round(prediction[0], 2)}")

            # Recommendations
            st.subheader("Suggestions:")
            if study_hours < 3:
                st.write("👉 Increase study hours")
            if sleep_hours < 6:
                st.write("👉 Improve sleep schedule")
            if attendance < 75:
                st.write("👉 Attend more classes")

        except Exception as e:
            st.error("Prediction failed")
            st.write(e)

    else:
        st.error("Model not loaded properly. Please check model.pkl")


import matplotlib.pyplot as plt

hours = [1,2,3,4,5,6,7,8]
preds = [model.predict([[h, sleep_hours]])[0] for h in hours]

fig, ax = plt.subplots()
ax.plot(hours, preds)
ax.set_xlabel("Study Hours")
ax.set_ylabel("Predicted Marks")
st.pyplot(fig)
