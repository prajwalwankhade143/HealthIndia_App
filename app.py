import streamlit as st
from auth.login import login
from auth.register import register
from modules.health_records import health_records

st.title("HealthIndia – Smart Healthcare System")

menu = ["Login", "Register", "Health Records"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    login()
elif choice == "Register":
    register()
elif choice == "Health Records":
    if "user_id" in st.session_state:
        health_records()
    else:
        st.warning("Please login first")
