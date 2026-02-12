import mysql.connector
from urllib.parse import urlparse
import os

# Railway URL yaha paste karo
DATABASE_URL = "mysql://root:QdnZxesGOAFEnZSFfdyvyRKTlEyAGBHV@metro.proxy.rlwy.net:18933/railway"

def get_connection():
    url = urlparse(DATABASE_URL)
    
    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],   # removes leading '/'
        port=url.port
    )
