import unittest
import account


class TestAccount(unittest.TestCase):
    def test_check_balance(self):
        pin = "1234"
        my_account = account.Account("1234", 0.00)
        self.assertEqual(0, my_account.check_balance(pin))

    def test_deposit(self):
        my_account = account.Account("1234", balance=0.00)
        self.assertEqual(0, my_account.deposit(0))
