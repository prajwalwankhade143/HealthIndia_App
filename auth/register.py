import streamlit as st
from firebase_db import db

def register():
    st.subheader("User Registration")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if name and email and password:
            db.collection("users").add({
                "name": name,
                "email": email
            })
            st.success("Registered Successfully! Now Login.")
        else:
            st.warning("All fields required")
