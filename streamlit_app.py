# streamlit_app.py
import streamlit as st
import requests

st.title("📧 Email Classification and PII Masking System")

email_input = st.text_area("Enter your email text:")

if st.button("Classify Email"):
    if email_input.strip() != "":
        # Send to FastAPI
        response = requests.post("http://127.0.0.1:8000/predict", json={"email_body": email_input})

        if response.status_code == 200:
            result = response.json()

            st.subheader("🔎 Masked Email:")
            st.write(result['masked_email'])

            st.subheader("🔐 List of Masked Entities:")
            st.json(result['list_of_masked_entities'])

            st.subheader("📂 Predicted Category:")
            st.success(result['category_of_the_email'])
        else:
            st.error("Error from API.")
    else:
        st.warning("Please enter email text!")
