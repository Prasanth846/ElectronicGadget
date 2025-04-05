import mysql.connector

def add_product():
    """Add a new product to the inventory."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="TechShop"
    )
    cursor = conn.cursor()
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock quantity: "))
    query = "INSERT INTO products (ProductName, Description, Price, stock) VALUES (%s, %s, %s, %s)"
    values = (name, description, price, stock)
    cursor.execute(query, values)
    conn.commit()
    print("Product added successfully!")
    cursor.close()
    conn.close()

def update_stock():
    """Update stock level of an existing product."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="TechShop"
    )
    cursor = conn.cursor()
    product_id = int(input("Enter ProductID to update stock: "))
    new_stock = int(input("Enter new stock quantity: "))
    query = "UPDATE products SET Stock = %s WHERE ProductID = %s"
    cursor.execute(query, (new_stock, product_id))
    conn.commit()
    print("Stock updated successfully!")
    cursor.close()
    conn.close()

def remove_product():
    """Remove a discontinued product from inventory."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="TechShop"
    )
    cursor = conn.cursor()
    product_id = int(input("Enter ProductID to remove: "))
    query = "DELETE FROM products WHERE ProductID = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    print("Product removed successfully!")
    cursor.close()
    conn.close()

def main():
    while True:
        print("\nTechShop Inventory Management")
        print("1. Add New Product")
        print("2. Update Stock Level")
        print("3. Remove Discontinued Product")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
