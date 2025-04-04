print("main.py is running ✅")
from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail
from models.inventory import Inventory
from datetime import datetime

# Step 1: Create a customer
customer1 = Customer(1, "Alice", "Smith", "alice@example.com", "1234567890", "123 Main St")

# Step 2: Create products
product1 = Product(101, "Laptop", "Gaming laptop", 1200)
product2 = Product(102, "Mouse", "Wireless Mouse", 25)

# Step 3: Add inventory for products
inventory1 = Inventory(201, product1, 10, datetime.now())
inventory2 = Inventory(202, product2, 20, datetime.now())

# Step 4: Create an order
order1 = Order(301, customer1, datetime.now())

# Step 5: Add order details (line items)
order_detail1 = OrderDetail(401, order1, product1, 1)
order_detail2 = OrderDetail(402, order1, product2, 2)

# Step 6: Calculate total order amount
total = order1.calculate_total_amount([order_detail1, order_detail2])

# Step 7: Print everything
print("===== Customer Info =====")
print(customer1.get_customer_details())

print("\n===== Order Info =====")
print(order1.get_order_details())

print("\n===== Order Detail 1 =====")
print(order_detail1.get_order_detail_info())

print("\n===== Order Detail 2 =====")
print(order_detail2.get_order_detail_info())

print("\n===== Inventory Check =====")
print("Laptop Available:", inventory1.is_product_available())
print("Mouse Available:", inventory2.is_product_available())
