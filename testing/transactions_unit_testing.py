"""
New Tests to Add:
Multiple deposits and withdrawals: Test combinations of multiple deposits and withdrawals.
Zero amount transactions: Test deposits and withdrawals of zero amounts.
Negative deposit (invalid input): Test what happens when a negative deposit is attempted.
Small balance edge cases: Test edge cases where the account balance is just enough for a withdrawal.
Invalid account types: Test invalid account types to check how the class handles them.
"""

from accounts.transactions import *
import unittest

class TestTransactions(unittest.TestCase):

    def setUp(self):
        """
        Create a new instance of Transactions before each test.
        """
        self.transactions = Transactions()

    def test_initial_balance(self):
        """
        Test if the initial balances are set correctly.
        """
        self.assertEqual(self.transactions.balance['Checking_balance'], 300)
        self.assertEqual(self.transactions.balance['Savings_balance'], 745)

    def test_deposit_checking(self):
        """
        Test deposit to the checking account.
        """
        self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.DEPOSIT, 100)
        self.assertEqual(self.transactions.balance['Checking_balance'], 400)
        self.assertIn((Transactions.CHECKING, 100), self.transactions.transactions)

    def test_deposit_savings(self):
        """
        Test deposit to the savings account.
        """
        self.transactions.deposit_withdrawal(Transactions.SAVINGS, Transactions.DEPOSIT, 200)
        self.assertEqual(self.transactions.balance['Savings_balance'], 945)
        self.assertIn((Transactions.SAVINGS, 200), self.transactions.transactions)

    def test_withdrawal_checking(self):
        """
        Test withdrawal from the checking account.
        """
        self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.WITHDRAWAL, 50)
        self.assertEqual(self.transactions.balance['Checking_balance'], 250)
        self.assertIn((Transactions.CHECKING, -50), self.transactions.transactions)

    def test_withdrawal_savings(self):
        """
        Test withdrawal from the savings account.
        """
        self.transactions.deposit_withdrawal(Transactions.SAVINGS, Transactions.WITHDRAWAL, 45)
        self.assertEqual(self.transactions.balance['Savings_balance'], 700)
        self.assertIn((Transactions.SAVINGS, -45), self.transactions.transactions)

    def test_overdraft_checking(self):
        """
        Test overdraft prevention for checking account.
        """
        result = self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.WITHDRAWAL, 350)
        self.assertEqual(result, '$350 would cause an overdraft. Please choose another amount')
        self.assertEqual(self.transactions.balance['Checking_balance'], 300)  # No change in balance

    def test_overdraft_savings(self):
        """
        Test overdraft prevention for savings account.
        """
        result = self.transactions.deposit_withdrawal(Transactions.SAVINGS, Transactions.WITHDRAWAL, 800)
        self.assertEqual(result, '$800 would cause an overdraft. Please choose another amount')
        self.assertEqual(self.transactions.balance['Savings_balance'], 745)  # No change in balance

    # Additional Tests

    def test_multiple_deposits_withdrawals(self):
        """
        Test multiple deposits and withdrawals on both accounts.
        """
        self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.DEPOSIT, 50)
        self.transactions.deposit_withdrawal(Transactions.SAVINGS, Transactions.DEPOSIT, 100)
        self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.WITHDRAWAL, 20)
        self.transactions.deposit_withdrawal(Transactions.SAVINGS, Transactions.WITHDRAWAL, 50)

        self.assertEqual(self.transactions.balance['Checking_balance'], 330)  # 300 + 50 - 20
        self.assertEqual(self.transactions.balance['Savings_balance'], 795)   # 745 + 100 - 50
        self.assertIn((Transactions.CHECKING, 50), self.transactions.transactions)
        self.assertIn((Transactions.SAVINGS, 100), self.transactions.transactions)

    def test_zero_amount_deposit(self):
        """
        Test a deposit of 0 to the checking account.
        """
        self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.DEPOSIT, 0)
        self.assertEqual(self.transactions.balance['Checking_balance'], 300)  # No change in balance

    def test_zero_amount_withdrawal(self):
        """
        Test a withdrawal of 0 from the savings account.
        """
        self.transactions.deposit_withdrawal(Transactions.SAVINGS, Transactions.WITHDRAWAL, 0)
        self.assertEqual(self.transactions.balance['Savings_balance'], 745)  # No change in balance

    def test_negative_deposit(self):
        """
        Test a negative deposit (invalid input).
        """
        result = self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.DEPOSIT, -100)
        self.assertEqual(result, 'Cannot deposit a negative amount: -100')  # Expect the proper error message
        self.assertEqual(self.transactions.balance['Checking_balance'], 300)  # Balance should remain unchanged

    def test_small_balance_withdrawal_edge_case(self):
        """
        Test withdrawing an amount that leaves just enough balance.
        """
        result = self.transactions.deposit_withdrawal(Transactions.CHECKING, Transactions.WITHDRAWAL, 300)
        self.assertEqual(result, None)  # Should succeed
        self.assertEqual(self.transactions.balance['Checking_balance'], 0)  # Checking balance should be zero

    def test_invalid_account_type(self):
        """
        Test an invalid account type.
        """
        result = self.transactions.deposit_withdrawal('InvalidAccount', Transactions.DEPOSIT, 100)
        self.assertEqual(result, None)  # Should ignore or fail silently
        self.assertEqual(self.transactions.balance['Checking_balance'], 300)
        self.assertEqual(self.transactions.balance['Savings_balance'], 745)

if __name__ == '__main__':
    unittest.main()
