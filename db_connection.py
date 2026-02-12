import mysql.connector
from urllib.parse import urlparse
import streamlit as st

def get_connection():
    DATABASE_URL = st.secrets["mysql://root:QdnZxesGOAFEnZSFfdyvyRKTlEyAGBHV@metro.proxy.rlwy.net:18933/railway"]

    url = urlparse(DATABASE_URL)

    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],
        port=url.port,
        ssl_disabled=False
    )
