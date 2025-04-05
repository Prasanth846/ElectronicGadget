import mysql.connector

# Database Connection
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="TechShop"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to Search Products
def search_products():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    search_query = input("Enter product name or keyword to search: ")
    query = """SELECT ProductID, ProductName, Price, Description
 FROM products
 WHERE ProductName LIKE %s OR Description LIKE %s"""
    cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
    results = cursor.fetchall()
    if not results:
        print("No matching products found.")
    else:
        print("\nSearch Results:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ₹{row[2]}, Description: {row[3]}")
        # Fetch recommendations
        recommend_products(search_query, cursor)
    cursor.close()
    conn.close()

# Function to Recommend Products Based on Description
def recommend_products(search_query, cursor):
    query = """SELECT ProductID, ProductName, Price, Description
 FROM products
 WHERE Description LIKE %s
 LIMIT 3"""
    cursor.execute(query, (f"%{search_query}%",))
    recommendations = cursor.fetchall()
    if recommendations:
        print("\nRecommended Products:")
        for row in recommendations:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ₹{row[2]}, Description: {row[3]}")

# Main Menu
def main():
    while True:
        print("\n1. Search Products\n2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            search_products()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
