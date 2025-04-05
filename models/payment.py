from models.exceptions import PaymentFailedException

class Payment:
    def __init__(self, payment_id, order, amount, status="Pending"):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.status = status

    def process_payment(self, success=True):
        if success:
            self.status = "Completed"
        else:
            raise PaymentFailedException("Payment was declined.")