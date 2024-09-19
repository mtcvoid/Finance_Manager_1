import unittest
from unittest.mock import patch
from account_objects.accounts import Account
from interface.user_interface_general import (
    create_new_account_interface,
    input_with_validation,
    get_user_confirmation,
    get_retry_or_exit_choice
)

class TestAccountCreation(unittest.TestCase):

    @patch('builtins.input', side_effect=['n'])  # Simulate user choosing 'No'
    @patch('builtins.print')  # Mocking print so it doesn't output to console
    def test_create_new_account_interface_exit(self, mock_print, mock_input):
        result = create_new_account_interface()
        self.assertIsNone(result)  # Ensure None is returned when exiting

        # Check that the function prints the correct message
        mock_print.assert_called_with('Exiting account creation...')

    @patch('builtins.input', side_effect=['y', 'john_doe', 'y', 'password123', 'y', 'John Doe', 'y', "John's Investment Account", 'y'])
    @patch('builtins.print')
    def test_create_new_account_interface_success(self, mock_print, mock_input):
        account = create_new_account_interface()

        # Check that the account was created successfully
        self.assertIsInstance(account, Account)
        self.assertEqual(account.user_name, 'john_doe')
        self.assertEqual(account.new_password, 'password123')
        self.assertEqual(account.holder_name, 'John Doe')
        self.assertEqual(account.account_name, "John's Investment Account")

    @patch('builtins.input', side_effect=['john_doe', 'y'])
    def test_input_with_validation_success(self, mock_input):
        result = input_with_validation('Username')
        self.assertEqual(result, 'john_doe')

    @patch('builtins.input', side_effect=['wrong_input', 'n', 'correct_input', 'y'])
    def test_input_with_validation_retry(self, mock_input):
        result = input_with_validation('Username')
        self.assertEqual(result, 'correct_input')

    @patch('builtins.input', side_effect=['y'])
    def test_get_user_confirmation_yes(self, mock_input):
        result = get_user_confirmation('Are you sure? (Y)es, (N)o')
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['n'])
    def test_get_user_confirmation_no(self, mock_input):
        result = get_user_confirmation('Are you sure? (Y)es, (N)o')
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['1'])
    def test_get_retry_or_exit_choice_retry(self, mock_input):
        result = get_retry_or_exit_choice()
        self.assertEqual(result, 'retry')

    @patch('builtins.input', side_effect=['2'])
    def test_get_retry_or_exit_choice_exit(self, mock_input):
        result = get_retry_or_exit_choice()
        self.assertEqual(result, 'exit')


if __name__ == '__main__':
    unittest.main()
