from datetime import datetime

class Orders:
    def __init__(self, order_id, customer, order_date, total_price):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.total_price = total_price

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Date: {self.order_date}, Total: {self.total_price}"