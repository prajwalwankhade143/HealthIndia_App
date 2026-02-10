import streamlit as st
import urllib.parse
import os

from firebase_db import db   # ✅ FIREBASE

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="HealthIndia – Smart Healthcare System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- IMAGE HELPER ----------
def show_page_image(image_path, title=None):
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if title:
            st.markdown(
                f"<h2 style='text-align:center'>{title}</h2>",
                unsafe_allow_html=True
            )

        if os.path.exists(image_path):
            try:
                st.image(image_path, use_container_width=True)
            except Exception:
                st.info("🖼️ Image format issue, skipping image.")
        else:
            st.info("🖼️ Image not found, skipping image.")

# ---------- IMPORTS ----------
from auth.login import login
from auth.register import register

from modules.health_records import health_records
from modules.medicine import medicine
from modules.appointments import appointments
from modules.diet import diet
from modules.exercise import exercise
from modules.reports import reports
from modules.feedback import feedback_page
from modules.dashboard import dashboard
from modules.government_schemes import government_schemes
from modules.insurance import insurance_page

# ---------- GLOBAL UI ----------
st.markdown("""
<style>
html, body, .stApp {
    background-color: #eef2f7 !important;
    color: #1f2937;
}
.block-container {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin: 1.5rem auto;
    max-width: 1200px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e6ecf5, #dde6f2) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("HealthIndia – Smart Healthcare System")

# ---------- SESSION ----------
if "page" not in st.session_state:
    st.session_state["page"] = "Register"

is_logged_in = "user" in st.session_state

# ---------- SIDEBAR ----------
st.sidebar.title("Menu")

if not is_logged_in:
    if st.sidebar.button("📝 Register"):
        st.session_state["page"] = "Register"
    if st.sidebar.button("🔐 Login"):
        st.session_state["page"] = "Login"

else:
    st.sidebar.success(f"Welcome {st.session_state['user']}")

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
    if st.sidebar.button("🏛️ Government Schemes"):
        st.session_state["page"] = "Government Schemes"
    if st.sidebar.button("🛡️ Insurance"):
        st.session_state["page"] = "Insurance"
    if st.sidebar.button("⭐ Feedback & Rating"):
        st.session_state["page"] = "Feedback"

    # ---- MAP SEARCH ----
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

page = st.session_state.get("page", "Register")

# ---------- PAGE IMAGE ----------
if page == "Register":
    show_page_image("assets/images/register_healthindia.png",
                    "HealthIndia – Smart Healthcare System")
elif page == "Login":
    show_page_image("assets/images/register_healthindia.png",
                    "HealthIndia – Smart Healthcare System")
elif page == "Dashboard":
    show_page_image("assets/images/welcome_healthindia.png",
                    "Welcome to HealthIndia")
elif page == "Health Records":
    show_page_image("assets/images/Health Records.png", "Health Records")
elif page == "Appointments":
    show_page_image("assets/images/appointments.png", "Doctor Appointments")
elif page == "Medicine":
    show_page_image("assets/images/medicine.png", "Medicine Management")
elif page == "Diet":
    show_page_image("assets/images/diet.png", "Healthy Diet Plan")
elif page == "Exercise":
    show_page_image("assets/images/exercise.png", "Exercise & Fitness")
elif page == "Reports":
    show_page_image("assets/images/reports.png", "Health Reports")
elif page == "Government Schemes":
    show_page_image("assets/images/govt_schemes.png",
                    "Indian Government Health Schemes")
elif page == "Insurance":
    show_page_image("assets/images/insurance.png",
                    "Health Insurance & Policies")

# ---------- PAGE RENDER ----------
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
elif page == "Government Schemes":
    government_schemes()
elif page == "Insurance":
    insurance_page()
elif page == "Feedback":
    feedback_page()

# ---------- GOOGLE MAP DISPLAY + FIREBASE SAVE ----------
if is_logged_in and search_map and hospital_place:
    db.collection("map_search_history").add({
        "user": st.session_state["user"],
        "location": hospital_place
    })

    query = urllib.parse.quote(hospital_place)
    map_url = f"https://www.google.com/maps?q={query}&output=embed"

    st.markdown("### 📍 Hospital Location")
    st.components.v1.html(
        f"<iframe src='{map_url}' width='100%' height='450'></iframe>",
        height=470
    )
    st.success("📌 Location search saved (Firebase)")
