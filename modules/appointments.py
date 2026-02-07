import streamlit as st
from db_connection import get_connection
import urllib.parse

def appointments():
    st.subheader("👨‍⚕️ Doctor Appointment & Profile Search")

    # ---------- DOCTOR GOOGLE SEARCH ----------
    st.markdown("### 🔍 Search Doctor Profile (Google)")

    doctor_name = st.text_input(
        "Enter Doctor Name",
        placeholder="e.g. Dr. Amit Sharma Cardiologist Nagpur"
    )

    search_doctor = st.button("🔎 Search Doctor on Google")

    if search_doctor and doctor_name:

        # SAVE SEARCH TO DATABASE
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO doctor_search_history (user_id, doctor_name)
            VALUES (%s, %s)
            """,
            (st.session_state["user_id"], doctor_name)
        )
        conn.commit()

        # GOOGLE SEARCH EMBED
        query = urllib.parse.quote(doctor_name)
        google_url = f"https://www.google.com/search?q={query}"

        st.success("Doctor search saved successfully")

        st.markdown(
            f"""
            <a href="{google_url}" target="_blank">
            👉 Click here to view Doctor Profile on Google
            </a>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # ---------- APPOINTMENT BOOKING ----------
    st.markdown("### 📅 Book Appointment")

    book_doctor_name = st.text_input(
        "Doctor Name for Appointment",
        placeholder="Same or different doctor name"
    )
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")

    if st.button("Book Appointment"):
        conn2 = get_connection()
        cursor2 = conn2.cursor()

        cursor2.execute(
            """
            INSERT INTO appointments
            (user_id, doctor_name, appointment_date, appointment_time, status)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                st.session_state["user_id"],
                book_doctor_name,
                appointment_date,
                appointment_time,
                "Booked"
            )
        )
        conn2.commit()

        st.success("✅ Appointment booked successfully")

print("appointments.py loaded")
