import unittest
from unittest.mock import patch
from accounts.account import NewAccount  # replace 'your_module' with the actual module name


class TestNewAccount(unittest.TestCase):
    @patch('random.randint', return_value=12345)  # Mock the user ID generation for consistent testing
    def setUp(self, mock_randint):
        self.user_name = "test_user"
        self.new_password = "password123"
        self.holder_name = "John Doe"
        self.account_name = "John's Checking"
        self.new_account = NewAccount(self.user_name, self.new_password, self.holder_name, self.account_name)

    def test_initialization(self):
        """Test that a new account is initialized correctly."""
        self.assertEqual(self.new_account.user_name, self.user_name)
        self.assertEqual(self.new_account.holder_name, self.holder_name)
        self.assertEqual(self.new_account._account_name, self.account_name)
        self.assertEqual(self.new_account._user_id, 12345)
        self.assertEqual(self.new_account._user_password, self.new_password)
        self.assertEqual(self.new_account.transactions, [])
        self.assertEqual(self.new_account.current_budget_warnings, 0)

    def test_view_account_details(self):
        """Test the output of the view_account_details method."""
        checking_balance = 500.0
        savings_balance = 1000.0
        expected_output = f"""
********************************
Account ID: 12345
Account Holder: {self.holder_name}
Checking Balance: {checking_balance}
Savings Balance: {savings_balance}
********************************"""
        result = self.new_account.view_account_details(checking_balance, savings_balance)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_get_account_details(self):
        """Test the output of the get_account_details method."""
        checking_balance = 500.0
        savings_balance = 1000.0
        expected_output = {
            'User ID': 12345,
            'Account Holder Name': self.holder_name,
            'User name': self.user_name,
            'User password': self.new_password,
            'Transaction History': [],
            'Checking Balance': checking_balance,
            'Savings Balance': savings_balance,
            'Current Budget Warnings': 0
        }
        result = self.new_account.get_account_details(checking_balance, savings_balance)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
