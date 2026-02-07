import streamlit as st
from db_connection import get_connection

def government_schemes():
    st.subheader("🏛️ Government Health Schemes (India)")

    schemes = [
        {
            "name": "Ayushman Bharat – PMJAY",
            "info": "Provides health insurance coverage up to ₹5 lakh per family per year.",
            "link": "https://pmjay.gov.in/"
        },
        {
            "name": "National Health Mission (NHM)",
            "info": "Improves availability of and access to quality health care.",
            "link": "https://nhm.gov.in/"
        },
        {
            "name": "Janani Suraksha Yojana (JSY)",
            "info": "Safe motherhood intervention for pregnant women.",
            "link": "https://nhm.gov.in/index1.php?lang=1&level=3&sublinkid=841"
        },
        {
            "name": "Pradhan Mantri Jan Arogya Yojana (PMJAY)",
            "info": "Cashless treatment at empanelled hospitals.",
            "link": "https://pmjay.gov.in/"
        },
        {
            "name": "Rashtriya Bal Swasthya Karyakram (RBSK)",
            "info": "Health screening and early intervention for children.",
            "link": "https://nhm.gov.in/index1.php?lang=1&level=2&sublinkid=642"
        },
        {
            "name": "National Mental Health Programme (NMHP)",
            "info": "Mental healthcare services across India.",
            "link": "https://nhm.gov.in/index1.php?lang=1&level=2&sublinkid=1048"
        }
    ]

    for scheme in schemes:
        with st.container():
            st.markdown(f"### 🩺 {scheme['name']}")
            st.write(scheme["info"])

            if st.button(f"🔗 View Scheme – {scheme['name']}"):
                # SAVE TO DATABASE
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO govt_scheme_history (user_id, scheme_name, scheme_link)
                    VALUES (%s, %s, %s)
                    """,
                    (st.session_state["user_id"], scheme["name"], scheme["link"])
                )
                conn.commit()

                st.success("Scheme visit saved")

                st.markdown(
                    f"""
                    <a href="{scheme['link']}" target="_blank">
                    👉 Open Official Government Website
                    </a>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("---")

print("government_schemes.py loaded")
