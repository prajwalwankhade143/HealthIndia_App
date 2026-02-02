import streamlit as st
from db_connection import get_connection

def exercise():
    st.subheader("Exercise Plan")

    exercise_name = st.text_input("Exercise Name (e.g. Walking, Yoga)")
    duration = st.text_input("Duration (e.g. 30 minutes)")

    if st.button("Save Exercise"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO exercise (user_id, exercise_name, duration) VALUES (%s,%s,%s)",
            (st.session_state["user_id"], exercise_name, duration)
        )
        conn.commit()
        st.success("Exercise saved successfully")

print("exercise.py loaded")
