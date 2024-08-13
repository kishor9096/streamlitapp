import streamlit as st
import streamlit_authenticator as stauth
from google.oauth2 import id_token
from google.auth.transport import requests
import os

def main():
    st.title("Your Streamlit App")
    
    # Google Authentication
    st.subheader("Google Authentication")
    client_id = st.secrets["google_client_id"]  # Replace with your OAuth client ID
    token = st.text_input("Enter your Google ID token", type="password")
    if st.button("Authenticate"):
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            if idinfo['aud'] != client_id:
                raise ValueError("Invalid client ID")
            st.success(f"Authentication successful: {idinfo['name']}")
            # Continue with the rest of your app logic here
        except ValueError as e:
            st.error("Authentication failed")
            st.error(e)

if __name__ == "__main__":
    main()
