import streamlit as st

from auth.login import login
from auth.register import register

from modules.health_records import health_records
from modules.medicine import medicine
from modules.appointments import appointments
from modules.diet import diet
from modules.exercise import exercise
from modules.reports import reports
from modules.dashboard import dashboard

st.title("HealthIndia – Smart Healthcare System")

is_logged_in = "user_id" in st.session_state

# 🔹 BEFORE LOGIN → Register + Login ALWAYS visible
if not is_logged_in:
    menu = ["Register", "Login"]
else:
    menu = [
        "Health Records",
        "Medicine",
        "Appointments",
        "Diet",
        "Exercise",
        "Reports",
        "Dashboard"
    ]

choice = st.sidebar.selectbox("Menu", menu)

# 🟢 BEFORE LOGIN FLOW
if not is_logged_in:
    if choice == "Register":
        register()
    elif choice == "Login":
        login()

# 🟢 AFTER LOGIN FLOW
else:
    if choice == "Health Records":
        health_records()
    elif choice == "Medicine":
        medicine()
    elif choice == "Appointments":
        appointments()
    elif choice == "Diet":
        diet()
    elif choice == "Exercise":
        exercise()
    elif choice == "Reports":
        reports()
    elif choice == "Dashboard":
        dashboard()
