class InsufficientStockException(Exception):
    """Exception raised when there is not enough stock available."""
    pass

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock

    def remove_from_inventory(self, quantity):
        if quantity > self.quantity_in_stock:
            raise InsufficientStockException("Not enough stock available.")
        self.quantity_in_stock -= quantity

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock > quantity_to_check