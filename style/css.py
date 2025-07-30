import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #0f1117;
            color: #ffffff;
        }
        .stApp {
            background-color: #0f1117;
        }
        .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
