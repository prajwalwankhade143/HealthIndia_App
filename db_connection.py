import mysql.connector
import os

def get_connection():
    # Streamlit secrets (recommended)
    host = os.getenv("DB_HOST", "YOUR_PLANETSCALE_HOST")
    user = os.getenv("DB_USER", " root@localhost")
    password = os.getenv("DB_PASS", "root123")
    database = os.getenv("DB_NAME", "healthindia")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
