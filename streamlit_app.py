# pip install streamlit
# pip install streamlit-authenticator

import streamlit as st
from streamlit_authenticator import authenticate
from streamlit_authenticator import RegisterableAuthenticator

names = ['Alice', 'Bob']
usernames = ['alice', 'bob']
passwords = ['password123', 'password456']

authenticator = RegisterableAuthenticator(
    names,
    usernames,
    passwords,
    'The Landing Page',
    'localhost',  # Replace with your app's URL if deploying
    enable_register=True,  # Enable user registration
)

def main():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    name, authentication_status, username = authenticator.login('Login')

    if authentication_status:
        st.session_state.authenticated = True
        st.title('Welcome, ' + name)
        # Add your landing page content here
    elif authentication_status == False:
        st.error('Username/password incorrect')
    else:
        st.info('Please login or register')

    # Register new users
    if st.button('Register'):
        authenticator.register_user(
            st.text_input('Name'),
            st.text_input('Username'),
            st.text_input('Password')
        )

    # Check if user is authenticated and display content accordingly
    if st.session_state.authenticated:
        # Display authenticated content here
        st.write('You are logged in as:', username)
    else:
        # Display content for non-authenticated users
        st.write('Please log in to access this content.')

if __name__ == '__main__':
    main()
