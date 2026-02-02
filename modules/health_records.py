import streamlit as st
from db_connection import get_connection

def health_records():
    st.subheader("Health Records")

    bmi = st.number_input("BMI")
    bp = st.text_input("Blood Pressure")

    if st.button("Save Record"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO health_records (user_id, bmi, bp) VALUES (%s, %s, %s)",
            (st.session_state["user_id"], bmi, bp)
        )
        conn.commit()
        st.success("Health record saved successfully")
        print("health_records module loaded")

