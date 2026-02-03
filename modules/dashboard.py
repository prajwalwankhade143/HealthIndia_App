import streamlit as st
import pandas as pd
from db_connection import get_connection

def dashboard():
    st.subheader("🏥 Health Dashboard")

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

    # -------- CARD 1: TABLE --------
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("### 🩺 Health Records")
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # -------- CARD 2: BMI --------
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("### 📈 BMI Trend Over Time")
    st.caption("Shows BMI variation based on recorded dates")
    st.line_chart(df["BMI"], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # -------- CARD 3: BP --------
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("### ❤️ Blood Pressure Overview")
    st.caption("Recorded blood pressure values")
    st.bar_chart(df["BP"], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

print("dashboard.py loaded")
