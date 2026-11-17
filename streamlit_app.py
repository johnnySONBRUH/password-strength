import streamlit as st
import joblib
import numpy as np
model = joblib.load('predictor.pkl')
STREAMLIT_APPS=['https://sbskkz5w96tlxlsmvkcha7.streamlit.app/']
def predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level):
    yes_no_map = {'No': 0, 'Yes': 1}
    smoking_history_map = {
        'not current': 0, 'former': 1, 'never': 2, 'current': 3, 'No Info': 4, 'ever': 5
    }
    gender_map = {'Male': 0, 'Female': 1, 'Other': 2}
    arr = np.array([
        gender_map[gender],
        age,
        yes_no_map[hypertension],
        yes_no_map[heart_disease],
        smoking_history_map[smoking_history],
        bmi,
        hba1c_level,
        blood_glucose_level
    ])
    arr = arr.reshape(1, -1)
    pred = model.predict(arr)
    return "Diabetes Detected" if pred[0] == 1 else "No Diabetes Detected"
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺")
st.title("🩺 Diabetes Predictor")
st.write("Enter your health data to assess potential diabetes risk.")
col1, col2 = st.columns(2)
with col1:
    st.subheader("👤 Demographic Info")
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    age = st.number_input('Age', min_value=0, max_value=120, value=25)
with col2:
    st.subheader("🏥 Health Indicators")
    hypertension = st.selectbox('Hypertension', ['Yes', 'No'])
    heart_disease = st.selectbox('Heart Disease', ['Yes', 'No'])
    smoking_history = st.selectbox(
        'Smoking History', 
        ['not current', 'former', 'never', 'current', 'No Info', 'ever']
    )
    bmi = st.number_input('BMI', min_value=0.0, value=18.5)
    hba1c_level = st.number_input('HbA1c Level', min_value=0.0, value=6.0)
    blood_glucose_level = st.number_input('Blood Glucose Level', min_value=0, value=100)
if st.button("Predict Risk", type="primary"):
    result = predict_diabetes(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level)
    if "No" in result:
        st.success(result)
    else:
        st.error(result)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Made by bruzz-bruzz</p>
    <div style="display: flex; justify-content: center; gap: 20px;">
        <a href="YOUR_GITHUB_PROFILE_URL" target="_blank">GitHub Profile</a>
        <a href="YOUR_GITHUB_REPO_URL" target="_blank">GitHub Repository</a>
    </div>
</div>
""", unsafe_allow_html=True)

