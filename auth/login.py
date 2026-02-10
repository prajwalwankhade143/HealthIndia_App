import streamlit as st
from firebase_db import db

def login():
    st.subheader("Login")

    email = st.text_input("Email")

    if st.button("Login"):
        users = db.collection("users").where("email", "==", email).stream()
        if any(users):
            st.session_state["user"] = email
            st.success("Login successful")
        else:
            st.error("User not found. Please register.")
