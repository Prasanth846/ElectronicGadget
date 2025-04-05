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

def total_sales_report(cursor):
    """Fetch total sales amount"""
    cursor.execute("SELECT SUM(TotalAmount) FROM orders")
    total_sales = cursor.fetchone()[0]
    print(f"\nTotal Sales Amount: ₹{total_sales if total_sales else 0}")

def sales_by_date_range(cursor):
    """Fetch sales data between a specific date range"""
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    cursor.execute(
        "SELECT OrderID, CustomerID, OrderDate, TotalAmount FROM orders WHERE \
OrderDate BETWEEN %s AND %s",
        (start_date, end_date)
    )
    orders = cursor.fetchall()
    print("\nSales Report (Date Range):")
    for order in orders:
        print(f"Order ID: {order[0]}, Customer ID: {order[1]}, Date: {order[2]}, Amount: ₹{order[3]}")

def sales_by_customer(cursor):
    """Fetch total sales made by a specific customer"""
    customer_id = input("Enter Customer ID: ")
    cursor.execute(
        "SELECT SUM(TotalAmount) FROM orders WHERE CustomerID = %s",
        (customer_id,)
    )
    total_sales = cursor.fetchone()[0]
    print(f"\nCustomer {customer_id} Total Purchases: ₹{total_sales if total_sales else 0}")

def main():
    """Main function to run the sales report system"""
    conn = get_db_connection()
    if not conn:
        return
    cursor = conn.cursor()
    while True:
        print("\nSALES REPORT MENU")
        print("1.  View Total Sales")
        print("2.  View Sales by Date Range")
        print("3.  View Sales by Customer")
        print("4.  Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            total_sales_report(cursor)
        elif choice == "2":
            sales_by_date_range(cursor)
        elif choice == "3":
            sales_by_customer(cursor)
        elif choice == "4":
            print("Exiting Sales Report...")
            break
        else:
            print("Invalid choice. Please try again.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
