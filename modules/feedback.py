import streamlit as st
from db_connection import get_connection

def feedback_page():
    st.subheader("⭐ Doctor & Hospital Feedback")

    doctor_name = st.text_input("Doctor Name")
    hospital_name = st.text_input("Hospital Name")
    rating = st.slider("Rating (1 = Worst, 5 = Best)", 1, 5,3)
    feedback_text = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        if doctor_name and hospital_name:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO feedback (user_id, doctor_name, hospital_name, rating, feedback)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    st.session_state["user_id"],
                    doctor_name,
                    hospital_name,
                    rating,
                    feedback_text
                )
            )
            conn.commit()

            st.success("✅ Feedback submitted successfully")
        else:
            st.warning("Please fill Doctor and Hospital name")
