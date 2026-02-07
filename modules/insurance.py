import streamlit as st
import urllib.parse
from db_connection import get_connection

def insurance_page():
    st.subheader("🛡️ Health Insurance Search")

    insurance_name = st.text_input(
        "Search Insurance Company",
        placeholder="e.g. LIC Health, Star Health, HDFC Ergo"
    )

    if st.button("🔍 Search Insurance") and insurance_name:

        # SAVE SEARCH TO DATABASE
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO insurance_search_history (user_id, insurance_name)
            VALUES (%s, %s)
            """,
            (st.session_state["user_id"], insurance_name)
        )
        conn.commit()

        query = urllib.parse.quote(insurance_name)
        google_url = f"https://www.google.com/search?q={query}+health+insurance"

        st.success("✅ Insurance search saved successfully")

        # 👉 REAL WORKING GOOGLE OPEN
        st.markdown(
            f"""
            ### 🌐 Open Insurance Results  
            👉 [Click here to view on Google]({google_url})
            """,
            unsafe_allow_html=True
        )
