import streamlit as st
import streamlit_authenticator as stauth
from google.oauth2 import id_token
from google.auth.transport import requests
import os


# Handle OAuth2 callback route
AUTHORIZATION_CODE = "code"
REDIRECT_URI = "https://khatabook.streamlit.app/"  # Replace with your redirect URI

if st._is_running_with_streamlit:
    ctx = ReportThread.get_report_ctx()
    session_id = ctx.session_id
    session_info = Server.get_current()._session_info_by_id[session_id]

    if session_info.ws.request_info.request_line == "GET /":
        auth_code = session_info.ws.request_info.query_params[AUTHORIZATION_CODE]
        get_google_id_token(auth_code, st.secrets["google_client_id"])  # Replace with your actual client ID
        # Continue with the rest of your app's logic
        st.write("Holla!!! You are In.....")
st.title("Khatabook - By Techunar")
st.write("Welcome to Techunar Khatabook!")

def get_google_id_token(auth_code, client_id):
    try:
        token = id_token.fetch_id_token(requests.Request(), auth_code, client_id)
        return token
    except ValueError as e:
        st.error(f"Error retrieving ID token: {e}")

if st.button("Sign in with Google"):
# Redirect the user to the Google Sign-In page
    auth_url = "https://accounts.google.com/o/oauth2/auth"
    client_id = "YOUR_CLIENT_ID"  # Replace with your actual client ID
    redirect_uri = "http://localhost:8501/"  # Replace with your redirect URI
    scope = "openid"  # Replace with the desired scopes
    state = "state123"  # Replace with a unique state value
    auth_endpoint = f"{auth_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}"
    st.markdown(f'<a href="{auth_endpoint}">Click here to sign in with Google</a>', unsafe_allow_html=True)
        
    # # Google Authentication
    # st.subheader("Google Authentication")
    # client_id = st.secrets["google_client_id"]  # Replace with your OAuth client ID
    # token = st.text_input("Enter your Google ID token", type="password")
    # if st.button("Authenticate"):
    #     try:
    #         idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
    #         if idinfo['aud'] != client_id:
    #             raise ValueError("Invalid client ID")
    #         st.success(f"Authentication successful: {idinfo['name']}")
    #         # Continue with the rest of your app logic here
    #     except ValueError as e:
    #         st.error("Authentication failed")
    #         st.error(e)
