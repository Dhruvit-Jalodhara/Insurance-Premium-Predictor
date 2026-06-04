import streamlit as st
import pickle
import numpy as np

# Load Model and Scaler
linear_model = pickle.load(open('Models/linear.pkl', 'rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl', 'rb'))

# Page Config
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="centered"
)

# Title & Description
st.title("🏥 Insurance Premium Predictor")

st.markdown("""
Predict insurance premium charges based on:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region
""")

st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25,
        step=1
    )

    sex = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )

with col2:
    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    smoker = st.selectbox(
        "Do you Smoke?",
        ["Yes", "No"]
    )

    region = st.selectbox(
        "Region",
        ["southwest", "southeast", "northwest", "northeast"]
    )

# Encoding
encoded_sex = 1 if sex == "Male" else 0

encoded_smoker = 1 if smoker == "Yes" else 0

region_mapping = {
    "southwest": 1,
    "southeast": 2,
    "northwest": 3,
    "northeast": 4
}

encoded_region = region_mapping[region]

# Show User Inputs
with st.expander(" View Input Data"):
    st.write({
        "Age": age,
        "Gender": sex,
        "BMI": bmi,
        "Children": children,
        "Smoker": smoker,
        "Region": region
    })

# Prediction
if st.button(" Predict Insurance Premium"):

    input_data = np.array([ [ age, encoded_sex, bmi, children, encoded_smoker, encoded_region] ])

    scaled_data = standard_scaler.transform(input_data)
    prediction = linear_model.predict(scaled_data)

    st.markdown("---")

    st.metric( label="Predicted Insurance Premium", value=f"${prediction[0]:,.2f}" )

    st.success("Prediction completed successfully!")

