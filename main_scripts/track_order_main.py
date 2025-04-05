import mysql.connector

def track_order_status():
    """Retrieve and display the order status for a given customer."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="TechShop"
    )
    cursor = conn.cursor()
    email = input("Enter your email to track orders: ")
    # Check if the customer exists
    cursor.execute("SELECT CustomerID FROM customers WHERE Email = %s", (email,))
    customer = cursor.fetchone()
    if not customer:
        print("No customer found with this email.")
        return

    customer_id = customer[0]
    # Retrieve order details
    cursor.execute("SELECT OrderID, OrderDate, TotalAmount, Status FROM orders WHERE CustomerID = %s", (customer_id,))
    orders = cursor.fetchall()
    if not orders:
        print("No orders found for this customer.")
    else:
        print("\nYour Orders:")
        print("{:<10} {:<15} {:<10} {:<10}".format("OrderID", "OrderDate", "TotalAmount", "Status"))
        print("-" * 50)
        for order in orders:
            print("{:<10} {:<15} {:<10} {:<10}".format(order[0], order[1], order[2], order[3]))
    cursor.close()
    conn.close()

def main():
    while True:
        print("\nTechShop Order Management")
        print("1. Track Order Status")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            track_order_status()
        elif choice == "2":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
