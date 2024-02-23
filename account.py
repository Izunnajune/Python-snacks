from decimal import Decimal

class Account:
    def __init__(self, pin: str, balance: Decimal):
        self._pin = pin
        self._balance = 0.0

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        return amount

    def check_balance(self, pin):
        if not self._validate_pin(pin):
            raise ValueError("Invalid PIN")
        return self._balance

    def _validate_pin(self, pin_entered):
        return pin_entered == self._pin

    def deposit(self, amount):
        self._validate_amount()
        self._balance += amount

    def withdraw(self, amount):
        self._validate_amount()
        self._balance -= amount

    def validate(self, amount, pin):
        self._validate_pin(pin)
        self._validate_amount()

