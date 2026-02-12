import streamlit as st
from db_connection import get_connection

def login():
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cursor.fetchone()

        if user:
            st.session_state["user_id"] = user[0]
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")
