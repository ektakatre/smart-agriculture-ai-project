
# =========================
# SMART AGRICULTURE AI APP
# =========================

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
import tensorflow as tf

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Smart Agriculture AI",
    layout="wide"
)

st.title("🌾 Smart Agriculture AI System")

# -------------------------
# SIDEBAR MENU
# -------------------------

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "🏠 Home",
        "🚜 Tractor Availability",
        "🌿 Disease Detection",
        "🌦️ Weather Information",
        "🌱 Crop Recommendation",
        "🤖 Kisan Chatbot"
    ]
)

# =========================
# HOME PAGE
# =========================

if menu == "🏠 Home":

    st.header("Welcome Farmer 👨‍🌾")

    st.write("""
    This Smart Agriculture AI System provides:

    ✅ Tractor Availability  
    ✅ Plant Disease Detection  
    ✅ Weather Information  
    ✅ Crop Recommendation  
    ✅ Kisan Chatbot
    """)

    st.image(
        "https://images.unsplash.com/photo-1500937386664-56d1dfef3854",
        use_container_width=True
    )

# =========================
# TRACTOR AVAILABILITY
# =========================

elif menu == "🚜 Tractor Availability":

    st.header("🚜 Tractor Availability System")

    try:

        df = pd.read_csv("TractorData - Sheet1 (1).csv")

        place = st.text_input("Enter City Name")

        if st.button("Search Tractor"):

            result = df[df["City"].str.lower() == place.lower()]

            if not result.empty:

                st.success("Tractors Available 🚜")

                st.dataframe(result)

            else:

                st.error("No Tractor Available")

    except Exception as e:

        st.warning(e)

# =========================
# DISEASE DETECTION
# =========================

elif menu == "🌿 Disease Detection":

    st.header("🌿 Plant Disease Detection")

    uploaded_file = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg", "png", "jpeg"]
    )

    disease_classes = [
        "Healthy",
        "Bacterial Spot",
        "Early Blight",
        "Late Blight",
        "Leaf Mold"
    ]

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", width=300)

        st.success("Image Uploaded Successfully")

        # Dummy AI Prediction
        prediction = np.random.choice(disease_classes)

        st.subheader(f"Prediction: {prediction}")

        # Solutions

        if prediction == "Healthy":
            st.success("Plant is Healthy ✅")

        elif prediction == "Bacterial Spot":
            st.warning("""
            Solution:
            - Use copper fungicide
            - Avoid overhead watering
            """)

        elif prediction == "Early Blight":
            st.warning("""
            Solution:
            - Remove infected leaves
            - Use fungicide spray
            """)

        elif prediction == "Late Blight":
            st.warning("""
            Solution:
            - Improve air circulation
            - Avoid excess moisture
            """)

        elif prediction == "Leaf Mold":
            st.warning("""
            Solution:
            - Maintain proper spacing
            - Reduce humidity
            """)

# =========================
# WEATHER INFORMATION
# =========================

elif menu == "🌦️ Weather Information":

    st.header("🌦️ Weather Information")

    city = st.text_input("Enter City")

    api_key = "734c6b2b87abbc4abe8aae7721bd46b1"

    if st.button("Get Weather"):

        try:

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            data = requests.get(url).json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            st.success(f"Weather in {city}")

            st.write(f"🌡️ Temperature: {temp} °C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"☁️ Condition: {weather}")

        except:

            st.error("Invalid City or API Error")

# =========================
# CROP RECOMMENDATION
# =========================

elif menu == "🌱 Crop Recommendation":

    st.header("🌱 Crop Recommendation System")

    nitrogen = st.number_input("Nitrogen")

    phosphorus = st.number_input("Phosphorus")

    potassium = st.number_input("Potassium")

    temperature = st.number_input("Temperature")

    humidity = st.number_input("Humidity")

    ph = st.number_input("pH Value")

    rainfall = st.number_input("Rainfall")

    if st.button("Recommend Crop"):

        # Dummy Logic

        if rainfall > 200:
            crop = "Rice"

        elif temperature > 30:
            crop = "Cotton"

        elif ph < 6:
            crop = "Tea"

        else:
            crop = "Wheat"

        st.success(f"Recommended Crop: {crop}")

# =========================
# KISAN CHATBOT
# =========================

elif menu == "🤖 Kisan Chatbot":

    st.header("🤖 Kisan Chatbot")

    question = st.text_input("Apna sawal poochho")

    if st.button("Send"):

        if question != "":

            st.success("Aapka sawal: " + question)

            if "pani" in question.lower():
                st.write("🌱 Fasal ko subah ya shaam pani dena best hota hai.")

            elif "gehu" in question.lower():
                st.write("🌾 Gehu ke liye thandi climate achhi hoti hai.")

            elif "khaad" in question.lower():
                st.write("🧪 Organic khaad mitti ke liye achhi hoti hai.")

            else:
                st.write("🤖 Is sawal ka answer abhi available nahi hai.")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.write("Made with ❤️ for Farmers")
