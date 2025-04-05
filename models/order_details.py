from exceptions.customer_exceptions import InvalidDataException

class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        if quantity <= 0:
            raise InvalidDataException("Quantity must be positive.")
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.quantity * self.product.get_price()  # Assuming get_price() exists in Products

    def update_quantity(self, new_quantity):
        if new_quantity <= 0:
            raise InvalidDataException("Quantity must be positive.")
        self.quantity = new_quantity