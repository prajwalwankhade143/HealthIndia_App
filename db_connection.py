import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # agar alag user hai to change karo
        password="root123",   # apna MySQL password
        database="healthindia",
        port=3306
    )
