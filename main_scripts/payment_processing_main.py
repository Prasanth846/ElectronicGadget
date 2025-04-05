import mysql.connector

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

def process_payment(cursor, conn):
    """Process a payment for an order"""
    order_id = input("Enter Order ID: ")
    # Check if order exists
    cursor.execute("SELECT TotalAmount, Status FROM orders WHERE OrderID = %s",(order_id,))
    order = cursor.fetchone()
    if not order:
        print("Order not found.")
        return

    total_amount, status = order
    if status == "Paid":
        print("This order is already paid.")
        return

    print(f"Total Amount: {total_amount}")
    print("\nPayment Methods:")
    print("1.  Credit Card")
    print("2.  Debit Card")
    print("3.  PayPal")
    print("4.  UPI")
    method_choice = input("Choose payment method (1-4): ")
    payment_methods = {"1": "Credit Card", "2": "Debit Card", "3": "PayPal", "4": "UPI"}
    if method_choice not in payment_methods:
        print("Invalid payment method.")
        return

    payment_method = payment_methods[method_choice]
    amount_paid = float(input("Enter payment amount: "))
    if amount_paid != float(total_amount):
        print(f"Payment amount must match TotalAmount: {total_amount}")
        return

    # Update orders table with payment details
    cursor.execute("UPDATE orders SET PaymentMethod = %s, AmountPaid = %s, Status = \
'Paid' WHERE OrderID = %s",
                   (payment_method, amount_paid, order_id))
    conn.commit()
    print("Payment processed successfully!")

def main():
    """Main function for payment processing"""
    conn = get_db_connection()
    if not conn:
        return
    cursor = conn.cursor()
    while True:
        print("\nPAYMENT PROCESSING")
        print("1.  Process a Payment")
        print("2.  Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            process_payment(cursor, conn)
        elif choice == "2":
            print("Exiting Payment Processing...")
            break
        else:
            print("Invalid choice. Try again.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
