import streamlit as st
from db_connection import get_connection

def diet():
    st.subheader("Diet Plan")

    meal_time = st.selectbox("Meal Time", ["Breakfast", "Lunch", "Dinner"])
    food = st.text_area("Food Description")

    if st.button("Save Diet"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO diet (user_id, meal_time, food) VALUES (%s,%s,%s)",
            (st.session_state["user_id"], meal_time, food)
        )
        conn.commit()
        st.success("Diet saved successfully")

print("diet.py loaded")
