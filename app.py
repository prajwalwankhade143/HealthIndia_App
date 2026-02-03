import streamlit as st   # ✅ FIRST LINE (MANDATORY)

# ---------- PAGE CONFIG (BLACK FLASH FIX) ----------
st.set_page_config(
    page_title="HealthIndia – Smart Healthcare System",
    layout="wide",
    initial_sidebar_state="expanded"
)

from auth.login import login
from auth.register import register

from modules.health_records import health_records
from modules.medicine import medicine
from modules.appointments import appointments
from modules.diet import diet
from modules.exercise import exercise
from modules.reports import reports
from modules.dashboard import dashboard


# ---------- GLOBAL UI FIX (REMOVE BLACK BACKGROUND) ----------
st.markdown("""
<style>

/* -------- FORCE LIGHT BACKGROUND -------- */
html, body, .stApp {
    background-color: #f9fafb !important;
    color: #1f2937 !important;
}

/* -------- REMOVE DARK FLASH -------- */
[data-testid="stAppViewContainer"] {
    background-color: #f9fafb !important;
}

/* -------- MAIN CONTENT -------- */
.main {
    background-color: #f9fafb !important;
}

/* -------- BLOCK CONTAINER -------- */
.block-container {
    padding-top: 1.5rem;
    background-color: #f9fafb !important;
}

/* -------- SIDEBAR -------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f8f9fc, #eef1f7) !important;
    padding: 10px;
}

/* ---- Sidebar title ---- */
section[data-testid="stSidebar"] h1 {
    color: #1f2937;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* ---- Sidebar buttons ---- */
section[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 12px;
    margin: 8px 0px;
    padding: 12px 14px;
    background: white !important;
    color: #1f2937 !important;
    border: 1px solid #e5e7eb;
    font-weight: 600;
    text-align: left;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    transition: all 0.25s ease;
}

/* ---- Hover effect ---- */
section[data-testid="stSidebar"] button:hover {
    background: linear-gradient(90deg, #4f8bf9, #6a5cff) !important;
    color: white !important;
    transform: translateX(4px);
    box-shadow: 0 6px 16px rgba(79,139,249,0.35);
    border: none;
}

/* ---- Success box ---- */
section[data-testid="stSidebar"] .stAlert {
    border-radius: 10px;
    font-weight: 600;
}

/* ---- Custom card ---- */
.dashboard-card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

/* ---- Dataframe ---- */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
}

/* ---- Charts ---- */
[data-testid="stChart"] {
    background: white;
    border-radius: 12px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------- TITLE ----------
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

# 🔹 AFTER LOGIN
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
