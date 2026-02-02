import streamlit as st
import pandas as pd
from db_connection import get_connection

def reports():
    st.subheader("Health Reports")

    report_type = st.selectbox(
        "Select Report Type",
        ["All Records", "Weekly Report", "Monthly Report", "Yearly Report"]
    )

    conn = get_connection()
    cursor = conn.cursor()

    if report_type == "All Records":
        query = """
            SELECT bmi, bp, created_at
            FROM health_records
            WHERE user_id = %s
            ORDER BY created_at DESC
        """
        cursor.execute(query, (st.session_state["user_id"],))

    elif report_type == "Weekly Report":
        query = """
            SELECT bmi, bp, created_at
            FROM health_records
            WHERE user_id = %s
              AND created_at >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
        """
        cursor.execute(query, (st.session_state["user_id"],))

    elif report_type == "Monthly Report":
        query = """
            SELECT bmi, bp, created_at
            FROM health_records
            WHERE user_id = %s
              AND created_at >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
        """
        cursor.execute(query, (st.session_state["user_id"],))

    else:  # Yearly
        query = """
            SELECT bmi, bp, created_at
            FROM health_records
            WHERE user_id = %s
              AND created_at >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
        """
        cursor.execute(query, (st.session_state["user_id"],))

    data = cursor.fetchall()

    if data:
        df = pd.DataFrame(data, columns=["BMI", "Blood Pressure", "Date"])
        st.table(df)

        st.subheader("BMI Trend")
        st.line_chart(df["BMI"])
    else:
        st.warning("No records found for selected period")

print("reports.py loaded")
