import mysql.connector
from datetime import datetime

# Database connection
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Change if needed
            password="root",  # Change if needed
            database="TechShop"  # Change if needed
        )
        return conn
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        return None

# Display available products
def show_products(cursor):
    cursor.execute("SELECT ProductID, ProductName, Price FROM products")
    products = cursor.fetchall()
    print("\nAvailable Products:")
    for product in products:
        print(f"{product[0]}. {product[1]} - ₹{product[2]}")
    return products

# Get customer ID from email
def get_customer_id(cursor, email):
    cursor.execute("SELECT CustomerID FROM customers WHERE Email = %s", (email,))
    result = cursor.fetchone()
    return result[0] if result else None

# Place an order
def place_order(cursor, conn, customer_id, product_id, quantity):
    # Check stock availability
    cursor.execute("SELECT ProductName, Price, stock FROM products WHERE ProductID = %s", (product_id,))
    product = cursor.fetchone()
    if not product:
        print("Invalid product selection.")
        return
    product_name, price, stock = product
    if stock < quantity:
        print("Insufficient stock available!")
        return
    # Calculate total amount
    total_amount = price * quantity
    # Insert order
    order_date = datetime.now().date()
    cursor.execute("INSERT INTO orders (CustomerID, OrderDate, TotalAmount, Status) VALUES (%s, %s, %s, %s)",
                   (customer_id, order_date, total_amount, "Pending"))
    order_id = cursor.lastrowid
    # Update stock
    new_stock = stock - quantity
    cursor.execute("UPDATE products SET stock = %s WHERE ProductID = %s", (new_stock, product_id))
    conn.commit()
    print(f"\nOrder placed successfully! Order ID: {order_id}")
    print(f"{quantity} {product_name}(s) ordered for ₹{total_amount}")

# Main function
def main():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    # Display products
    products = show_products(cursor)
    # Get customer email
    email = input("\nEnter your registered email: ")
    customer_id = get_customer_id(cursor, email)
    if not customer_id:
        print("Customer not found! Please register first.")
        return
    # Select product
    product_id = int(input("Enter Product ID to order: "))
    quantity = int(input("Enter quantity: "))
    # Place order
    place_order(cursor, conn, customer_id, product_id, quantity)
    # Close connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
