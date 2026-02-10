# auth/register.py
import streamlit as st
from db_connection import get_connection

def register():
    st.subheader("User Registration")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        try:
            conn = get_connection()
            print("DB CONNECTED")

            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
                (name, email, password)
            )
            conn.commit()

            st.success("Registration successful. Please login.")
            st.session_state["page"] = "Login"

        except Exception as e:
            st.error("Database error")
            print("REAL ERROR 👉", e)
