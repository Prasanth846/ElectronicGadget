import mysql.connector
import re

def get_db_connection():
    """Establish database connection"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="TechShop"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None


if __name__ == "__main__":
    
    try:
        # Simulating user input
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO CUSTOMERS (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
            values = (first_name, last_name, email, phone, address)
            cursor.execute(query, values)
            conn.commit()
            print("Customer registered successfully!")
            


    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")