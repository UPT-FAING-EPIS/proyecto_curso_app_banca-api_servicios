    
import datetime
from decimal import Decimal

class PaymentStrategy:
    def calculate_payment(self, amount, due_date):
        pass

class DiscountPaymentStrategy(PaymentStrategy):
    def calculate_payment(self, amount, due_date):
        return amount

class InterestPaymentStrategy(PaymentStrategy):
    def calculate_payment(self, amount, due_date):
        if datetime.date.today() > due_date:
            return amount * Decimal('2')  # Aplicar un incremento del 10% como interés
        else:
            return amount