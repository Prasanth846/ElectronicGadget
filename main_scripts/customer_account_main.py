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

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def validate_phone(phone):
    """Validate phone number (only digits, length 10-15)"""
    return phone.isdigit() and 10 <= len(phone) <= 15

def update_customer_profile(cursor, conn):
    """Update customer details"""
    customer_id = input("Enter your Customer ID: ")
    # Check if customer exists
    cursor.execute("SELECT * FROM customers WHERE CustomerID = %s",(customer_id,))
    customer = cursor.fetchone()
    if not customer:
        print("Customer not found.")
        return

    print("\nUpdate Options:")
    print("1.  Update Email")
    print("2.  Update Phone")
    print("3.  Update Address")
    choice = input("Enter choice: ")

    if choice == "1":
        new_email = input("Enter new Email: ")
        if not validate_email(new_email):
            print("Invalid email format.")
            return
        cursor.execute("UPDATE customers SET Email = %s WHERE CustomerID = %s",
                       (new_email, customer_id))
    elif choice == "2":
        new_phone = input("Enter new Phone Number: ")
        if not validate_phone(new_phone):
            print("Invalid phone number. Must be 10-15 digits.")
            return
        cursor.execute("UPDATE customers SET Phone = %s WHERE CustomerID = %s",
                       (new_phone, customer_id))
    elif choice == "3":
        new_address = input("Enter new Address: ")
        cursor.execute("UPDATE customers SET Address = %s WHERE CustomerID = %s",
                       (new_address, customer_id))
    else:
        print("Invalid choice.")
        return

    conn.commit()
    print("Customer details updated successfully.")

def main():
    """Main function to manage customer updates"""
    conn = get_db_connection()
    if not conn:
        return
    cursor = conn.cursor()
    while True:
        print("\nCUSTOMER ACCOUNT MANAGEMENT")
        print("1.  Update Account Information")
        print("2.  Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            update_customer_profile(cursor, conn)
        elif choice == "2":
            print("Exiting Customer Account Management...")
            break
        else:
            print("Invalid choice. Please try again.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
