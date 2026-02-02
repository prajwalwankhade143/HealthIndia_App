import streamlit as st
from auth.login import login
from auth.register import register
from modules.health_records import health_records
from modules.medicine import medicine
from modules.appointments import appointments



st.title("HealthIndia – Smart Healthcare System")

menu = ["Login", "Register", "Health Records", "Medicine", "Appointments"]
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

# ✅ NEW BLOCK (SAFE)
elif choice == "Medicine":
    if "user_id" in st.session_state:
        medicine()
    else:
        st.warning("Please login first")

elif choice == "Appointments":
    if "user_id" in st.session_state:
        appointments()
    else:
        st.warning("Please login first")
