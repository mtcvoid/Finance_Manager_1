import unittest
from accounts.new_account import Account  # Assuming this is in `accounts.py`
from accounts.transactions import Transactions  # Assuming this is in `accounts.py`


class TestAccountTransactionInteraction(unittest.TestCase):

    def setUp(self):
        # Create a new account with initial balance (we simulate this since Account class does not hold balances
        # directly)
        self.account = Account(user_name="testuser", new_password="password123", holder_name="John Doe",
                               account_name="John's Account")

        # Create a new transaction manager instance
        self.transaction_manager = Transactions()

        # Set initial balances for checking and savings
        self.transaction_manager.balance['Checking_balance'] = 1000
        self.transaction_manager.balance['Savings_balance'] = 500

    def test_account_creation(self):
        # Test that account is created with the correct details
        self.assertEqual(self.account.user_name, "testuser")
        self.assertEqual(self.account.holder_name, "John Doe")
        self.assertEqual(self.account._account_name, "John's Account")

    def test_deposit_checking(self):
        # Deposit into checking account and check balance
        self.transaction_manager.deposit_withdrawal(Transactions.CHECKING, Transactions.DEPOSIT, 500)
        self.assertEqual(self.transaction_manager.balance['Checking_balance'], 1500)

    def test_deposit_savings(self):
        # Deposit into savings account and check balance
        self.transaction_manager.deposit_withdrawal(Transactions.SAVINGS, Transactions.DEPOSIT, 200)
        self.assertEqual(self.transaction_manager.balance['Savings_balance'], 700)

    def test_withdrawal_checking(self):
        # Withdraw from checking account and check balance
        self.transaction_manager.deposit_withdrawal(Transactions.CHECKING, Transactions.WITHDRAWAL, 300)
        self.assertEqual(self.transaction_manager.balance['Checking_balance'], 700)

    def test_withdrawal_savings(self):
        # Withdraw from savings account and check balance
        self.transaction_manager.deposit_withdrawal(Transactions.SAVINGS, Transactions.WITHDRAWAL, 200)
        self.assertEqual(self.transaction_manager.balance['Savings_balance'], 300)

    def test_insufficient_funds_withdrawal(self):
        # Try to withdraw more than available balance from checking and expect an overdraft warning
        response = self.transaction_manager.deposit_withdrawal(Transactions.CHECKING, Transactions.WITHDRAWAL, 2000)
        self.assertEqual(response, '$2000 would cause an overdraft. Please choose another amount')

    def test_negative_deposit(self):
        # Try to deposit a negative amount and expect an error message
        response = self.transaction_manager.deposit_withdrawal(Transactions.CHECKING, Transactions.DEPOSIT, -100)
        self.assertEqual(response, 'Cannot deposit a negative amount: -100')

    def test_overdraft_checker(self):
        # Test overdraft checker for checking and savings accounts
        self.assertTrue(self.transaction_manager.over_draft_checker(Transactions.CHECKING, 500))  # Should pass
        self.assertFalse(self.transaction_manager.over_draft_checker(Transactions.CHECKING, 2000))  # Should fail


if __name__ == '__main__':
    unittest.main()
