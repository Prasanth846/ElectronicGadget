import mysql.connector

class Products:
    def __init__(self, product_id, product_name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def get_product_details(self):
        return f"Product ID: {self.product_id}, Name: {self.product_name}, Price: {self.price}"

    @staticmethod
    def add_product(db, product_name, description, price):
        """Insert a new product into the database"""
        try:
            cursor = db.connection.cursor()
            query = "INSERT INTO products (ProductName, Description, Price) VALUES (%s, %s, %s)"
            cursor.execute(query, (product_name, description, price))
            db.connection.commit()
            print("Product added successfully!")
        except mysql.connector.Error as e:
            print(f"Error adding product: {e}")
        finally:
            cursor.close()

    @staticmethod
    def update_product(db, product_id, new_price=None, new_description=None):
        """Update product details in the database"""
        try:
            cursor = db.connection.cursor()
            update_fields = []
            values = []
            if new_price is not None:
                if new_price < 0:
                    raise ValueError("Price cannot be negative.")
                update_fields.append("Price = %s")
                values.append(new_price)
            if new_description:
                update_fields.append("Description = %s")
                values.append(new_description)
            values.append(product_id)
            if update_fields:
                query = f"UPDATE products SET {', '.join(update_fields)} WHERE ProductID = %s"
                cursor.execute(query, values)
                db.connection.commit()
                print("Product updated successfully!")
            else:
                print("No changes made.")
        except mysql.connector.Error as e:
            print(f"Error updating product: {e}")
        finally:
            cursor.close()