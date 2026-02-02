import streamlit as st
from db_connection import get_connection

def appointments():
    st.subheader("Doctor Appointment")

    doctor_name = st.text_input("Doctor Name")
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")

    if st.button("Book Appointment"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO appointments (user_id, doctor_name, appointment_date, appointment_time, status) VALUES (%s,%s,%s,%s,%s)",
            (st.session_state["user_id"], doctor_name, appointment_date, appointment_time, "Booked")
        )
        conn.commit()
        st.success("Appointment booked successfully")

print("appointments.py loaded")
