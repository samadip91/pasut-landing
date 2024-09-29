import streamlit as st
from auth0.v2 import Authentication

# Initialize Auth0 client
auth0 = Authentication(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    domain="YOUR_DOMAIN"
)

# Create a login button
if st.button("Login with Auth0"):
    # Redirect to Auth0 login page
    authorization_url = auth0.authorization_url(
        redirect_uri="http://localhost:8501/"
    )
    st.write(f'<a href="{authorization_url}">Login</a>', unsafe_allow_html=True)

# Handle the callback from Auth0
if "code" in st.session_state:
    # Exchange code for an access token
    token = auth0.get_access_token(
        st.session_state.code,
        redirect_uri="http://localhost:8501/"
    )

    # Use the access token to get user information
    user_info = auth0.get_user_info(token["access_token"])

    # Check if the user is a paid user
    if user_info.get("is_paid"):
        # Grant access to the webpage
        st.write("Welcome, paid user!")
    else:
        st.write("Access denied. You must be a paid user.")
