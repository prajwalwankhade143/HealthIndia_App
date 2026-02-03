import streamlit as st
import pandas as pd
from db_connection import get_connection

def dashboard():
    st.subheader("Health Dashboard")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT bmi, bp, created_at
        FROM health_records
        WHERE user_id = %s
        ORDER BY created_at
    """
    cursor.execute(query, (st.session_state["user_id"],))
    data = cursor.fetchall()

    if not data:
        st.warning("No health data available")
        return

    df = pd.DataFrame(data, columns=["BMI", "BP", "Date"])

    st.markdown("### Health Records Table")
    st.dataframe(df)

    st.markdown("### BMI Trend Over Time")
    st.line_chart(df["BMI"])

    st.markdown("### Blood Pressure Overview")
    st.bar_chart(df["BP"])

print("dashboard.py loaded")
