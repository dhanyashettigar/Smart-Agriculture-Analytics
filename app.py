
import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="Smart Agriculture",
    page_icon="🌱",
    layout="wide"
)

# Load model
model = joblib.load("crop_model.pkl")

# Title
st.title("🌱 Smart Agriculture Analytics")
st.subheader("Crop Recommendation System")

st.write(
    "Enter the soil and environmental conditions "
    "to get the most suitable crop recommendation."
)

st.divider()

# Input fields
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", 0.0, 200.0, 90.0)
    P = st.number_input("Phosphorus (P)", 0.0, 200.0, 42.0)
    K = st.number_input("Potassium (K)", 0.0, 250.0, 43.0)
    temperature = st.number_input("Temperature (°C)", 0.0, 60.0, 25.0)

with col2:
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, 100.0)

# Prediction button
if st.button("🌾 Recommend Crop", use_container_width=True):

    input_data = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=[
            "N", "P", "K", "temperature",
            "humidity", "ph", "rainfall"
        ]
    )

    prediction = model.predict(input_data)

    st.success("Recommended Crop")

    st.markdown(
        f"<h2 style='text-align:center;'>🌱 {prediction[0].upper()}</h2>",
        unsafe_allow_html=True
    )

st.divider()

st.caption("Smart Agriculture Analytics | Crop Recommendation System")
