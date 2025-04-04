import mysql.connector

print("Attempting to connect to the database...")

try:
    # Replace these with your actual MySQL Workbench credentials
    connection = mysql.connector.connect(
        host="localhost",
        user="root",           # or your MySQL username
        password="root",       # replace with your actual MySQL password
        database="TechShop"
    )
    print("Database connection successful!")

    cursor = connection.cursor()

    # Sample query: Get all customers
    cursor.execute("SELECT FIRSTNAME, LASTNAME, EMAIL FROM CUSTOMERS")
    results = cursor.fetchall()

    if results:
        print("\nCustomers in TechShop:")
        print("------------------------")
        for row in results:
            print(f"{row[0]} {row[1]} - {row[2]}")
    else:
        print("No customers found.")

    # Additional queries to display more data
    print("\nOrders with Customer Names:")
    print("----------------------------")
    cursor.execute("""
        SELECT ORDERS.ORDERID, ORDERS.ORDERDATE, CUSTOMERS.FIRSTNAME, CUSTOMERS.LASTNAME
        FROM ORDERS
        JOIN CUSTOMERS ON ORDERS.CUSTOMERID = CUSTOMERS.CUSTOMERID
    """)
    orders = cursor.fetchall()
    if orders:
        for order in orders:
            print(f"OrderID: {order[0]}, Date: {order[1]}, Customer: {order[2]} {order[3]}")
    else:
        print("No orders found.")

    print("\nProducts and Total Revenue:")
    print("----------------------------")
    cursor.execute("""
        SELECT PRODUCTS.PRODUCTNAME, SUM(ORDERDETAILS.QUANTITY * PRODUCTS.PRICE) AS TOTALREVENUE
        FROM ORDERDETAILS
        JOIN PRODUCTS ON ORDERDETAILS.PRODUCTID = PRODUCTS.PRODUCTID
        GROUP BY PRODUCTS.PRODUCTNAME
    """)
    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"Product: {product[0]}, Total Revenue: ${product[1]:.2f}")
    else:
        print("No products found.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()

