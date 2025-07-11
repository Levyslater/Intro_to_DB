# creates a database if it does not exists

import mysql.connector
from mysql.connector import Error, errorcode

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='lawre',
        password='Uyi76d'
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Step 2: Create a cursor and execute SQL
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully.")

except Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong Username and or password!")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f" Error: {e}")

finally:
    # only close variables if they were successfully created to avoid NameError
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
