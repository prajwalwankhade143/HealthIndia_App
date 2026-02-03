st.markdown("""
<style>
/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #f5f7fb;
}

/* Sidebar title */
section[data-testid="stSidebar"] h1 {
    color: #2c3e50;
}

/* Sidebar buttons style */
section[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 8px;
    margin: 6px 0px;
    padding: 10px;
    background-color: white;
    color: #2c3e50;
    border: 1px solid #dcdcdc;
    font-weight: 600;
}

/* Hover effect */
section[data-testid="stSidebar"] button:hover {
    background-color: #4f8bf9;
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

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

# -------- SESSION DEFAULTS --------
if "page" not in st.session_state:
    st.session_state["page"] = "Register"

is_logged_in = "user_id" in st.session_state

# -------- SIDEBAR --------
st.sidebar.title("Menu")

# 🔹 BEFORE LOGIN
if not is_logged_in:
    if st.sidebar.button("📝 Register"):
        st.session_state["page"] = "Register"

    if st.sidebar.button("🔐 Login"):
        st.session_state["page"] = "Login"

# 🔹 AFTER LOGIN → ALL FEATURES AS BOXES
else:
    st.sidebar.success("Logged In")

    if st.sidebar.button("📊 Dashboard"):
        st.session_state["page"] = "Dashboard"

    if st.sidebar.button("🩺 Health Records"):
        st.session_state["page"] = "Health Records"

    if st.sidebar.button("💊 Medicine"):
        st.session_state["page"] = "Medicine"

    if st.sidebar.button("👨‍⚕️ Appointments"):
        st.session_state["page"] = "Appointments"

    if st.sidebar.button("🥗 Diet"):
        st.session_state["page"] = "Diet"

    if st.sidebar.button("🏃 Exercise"):
        st.session_state["page"] = "Exercise"

    if st.sidebar.button("📄 Reports"):
        st.session_state["page"] = "Reports"

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# -------- PAGE RENDER --------
page = st.session_state["page"]

if page == "Register":
    register()

elif page == "Login":
    login()

elif page == "Dashboard":
    dashboard()

elif page == "Health Records":
    health_records()

elif page == "Medicine":
    medicine()

elif page == "Appointments":
    appointments()

elif page == "Diet":
    diet()

elif page == "Exercise":
    exercise()

elif page == "Reports":
    reports()
