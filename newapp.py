import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load Files
model = joblib.load("rf_model.joblib")
df = pd.read_csv("cleaned_df.csv")

# Sidebar
with st.sidebar:
    st.title("🏠 House Price Prediction")

    st.image("house.png", width=250)

    st.markdown("---")

    st.success("Machine Learning Project")

    st.markdown("---")

    st.subheader("About")

    st.write(
        "This project predicts Bengaluru house prices using Machine Learning and Streamlit."
    )

# Main Page
st.title("🏡 Bengaluru House Price Prediction")

st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:

    location = st.selectbox(
        "📍 Location",
        sorted(df["location"].unique())
    )

    sqft = st.number_input(
        "📐 Total Sq.ft",
        min_value=300,
        max_value=10000,
        value=1000
    )

with col2:

    bath = st.selectbox(
        "🚿 Bathrooms",
        sorted(df["bath"].unique())
    )

    bhk = st.selectbox(
        "🏠 BHK",
        sorted(df["bhk"].unique())
    )

# Predict Button
if st.button("🔮 Predict Price"):

    try:

        encoded_location = df.loc[
            df["location"] == location,
            "encoded_location"
        ].iloc[0]

        if "encoded_availability" in df.columns:
            encoded_availability = df["encoded_availability"].iloc[0]
        else:
            encoded_availability = 0

        input_data = pd.DataFrame({
            "encoded_availability": [encoded_availability],
            "total_sqft": [sqft],
            "bath": [bath],
            "bhk": [bhk],
            "encoded_location": [encoded_location]
        })

        prediction = model.predict(input_data)

        st.success(
            f"🏡 Predicted Price: ₹ {prediction[0]:,.2f} Lakhs"
        )

        st.balloons()

        st.subheader("Property Details")

        st.write("📍 Location:", location)
        st.write("📐 Total Sq.ft:", sqft)
        st.write("🚿 Bathrooms:", bath)
        st.write("🏠 BHK:", bhk)

    except Exception as e:

        st.error(f"Error: {e}")

# Footer
st.markdown("---")

st.caption("Built with Python | Scikit-Learn | Streamlit")

st.write("Created by Shikha Gupta ❤️")