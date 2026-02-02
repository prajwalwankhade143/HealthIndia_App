import streamlit as st
from db_connection import get_connection

def medicine():
    st.subheader("Medicine Details")

    medicine_name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage (e.g. 1 tablet)")
    schedule = st.selectbox("Schedule", ["Morning", "Afternoon", "Night"])

    if st.button("Save Medicine"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO medicine (user_id, medicine_name, dosage, schedule) VALUES (%s,%s,%s,%s)",
            (st.session_state["user_id"], medicine_name, dosage, schedule)
        )
        conn.commit()
        st.success("Medicine saved successfully")

print("medicine.py loaded")
