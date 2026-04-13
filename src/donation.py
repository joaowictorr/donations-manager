from datetime import datetime, date

class Donation:
    def __init__(self, item_name, quantity, expiration_date):
        self.item_name = item_name
        self.quantity = self._validate_quantity(quantity)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

    def _validate_quantity(self, qty):
        if int(qty) <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        return int(qty)

    def is_near_expiration(self):
        days_remaining = (self.expiration_date - date.today()).days
        # Retorna True se vencer em até 7 dias
        return 0 <= days_remaining <= 7

    def to_dict(self):
        return {
            "item_name": self.item_name,
            "quantity": self.quantity,
            "expiration_date": str(self.expiration_date)
        }