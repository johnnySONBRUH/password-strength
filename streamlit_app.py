import streamlit as st
import joblib
import pandas as pd
from parseInput import parseInput

# Load the model
model = joblib.load('predictor.pkl')

def check_password_strength(password):
    # Parse the password using the existing parseInput function
    # It returns: lower, upper, special, length
    lower, upper, special, length = parseInput(password)
    
    # Create a DataFrame with the features as expected by the model
    # The columns in training were 'Has Lowercase', 'Has Uppercase', 'Has Special Character', 'Length'
    # pandas will treat True/False as 1/0
    input_features = pd.DataFrame([[lower, upper, special, length]], 
    columns=['Has Lowercase', 'Has Uppercase', 'Has Special Character', 'Length'])
    
    # Predict
    pred = model.predict(input_features)
    return pred[0]

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔒 Password Strength Checker")
st.write("Enter a password to assess its strength.")

password = st.text_input("Password", type="password")

if st.button("Check Strength", type="primary"):
    if not password:
        st.warning("Please enter a password.")
    else:
        result = check_password_strength(password)
        if result == "Weak":
            st.error(f"Strength: **{result}**")
        else:
            st.success(f"Strength: **{result}**")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Password Strength AI</p>
</div>
""", unsafe_allow_html=True)

