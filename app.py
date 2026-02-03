import streamlit as st   # ✅ FIRST LINE (MANDATORY)
from db_connection import get_connection
import urllib.parse

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

/* FULL APP BACKGROUND */
html, body, .stApp {
    background-color: #eef2f7 !important;
    color: #1f2937;
}

/* MAIN CONTENT */
[data-testid="stAppViewContainer"] {
    background-color: #eef2f7 !important;
}

/* CENTER CARD */
.block-container {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin: 1.5rem auto;
    max-width: 1200px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e6ecf5, #dde6f2) !important;
    padding: 16px;
    border-right: 1px solid #d0d7e2;
}

section[data-testid="stSidebar"] h1 {
    color: #1e293b;
    font-weight: 700;
}

section[data-testid="stSidebar"] button {
    width: 100%;
    background-color: #ffffff !important;
    color: #1f2937 !important;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    margin: 8px 0;
    padding: 12px 14px;
    font-weight: 600;
    text-align: left;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    transition: all 0.25s ease;
}

section[data-testid="stSidebar"] button:hover {
    background: linear-gradient(90deg, #4f8bf9, #6a5cff) !important;
    color: white !important;
    transform: translateX(4px);
    box-shadow: 0 6px 16px rgba(79,139,249,0.35);
    border: none;
}

section[data-testid="stSidebar"] .stAlert {
    border-radius: 10px;
    font-weight: 600;
}

input, textarea, select {
    background-color: #f1f5f9 !important;
    border-radius: 10px !important;
}

[data-testid="stDataFrame"],
[data-testid="stChart"] {
    background-color: #ffffff;
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

    # ---------- GOOGLE MAP SEARCH (SIDEBAR) ----------
    st.sidebar.markdown("---")
    st.sidebar.subheader("📍 Hospital Map")

    hospital_place = st.sidebar.text_input(
        "Search Hospital / Location",
        placeholder="e.g. AIIMS Nagpur"
    )

    search_map = st.sidebar.button("🔍 Search on Map")

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


# -------- GOOGLE MAP DISPLAY (MAIN PAGE + DB SAVE) --------
if is_logged_in and 'search_map' in locals() and search_map and hospital_place:

    conn = get_connection()
    cursor = conn.cursor()

    # SAVE SEARCH TO DATABASE
    cursor.execute(
        """
        INSERT INTO map_search_history (user_id, location_name)
        VALUES (%s, %s)
        """,
        (st.session_state["user_id"], hospital_place)
    )
    conn.commit()

    query = urllib.parse.quote(hospital_place)
    map_url = f"https://www.google.com/maps?q={query}&output=embed"

    st.markdown("### 📍 Hospital Location")
    st.components.v1.html(
        f"""
        <iframe
            src="{map_url}"
            width="100%"
            height="450"
            style="border:0; border-radius:14px;"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
        """,
        height=470
    )

    st.success("📌 Location search saved successfully")
