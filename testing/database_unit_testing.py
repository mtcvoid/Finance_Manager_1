import unittest
import sqlite3
from data_handler.database.data_base_handler import DatabaseUnpacker


class TestDatabaseUnpackerRealDB(unittest.TestCase):

    def setUp(self):
        """ Set up a connection to the real database for each test. """
        self.db_file = 'BankingData.db'  # Path to the actual database file
        self.db_unpacker = DatabaseUnpacker()

        # Ensure the table exists
        self.db_unpacker.create_account_log_table()

    # Remove or comment out the tearDown method so data persists
    # def tearDown(self):
    #     """ Clean up any test data in the database after each test. """
    #     with sqlite3.connect(self.db_file) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("DELETE FROM accountlog WHERE user_name = 'test_user'")
    #         conn.commit()

    def test_create_account_log_table(self):
        """ Test the creation of the accountlog table. """
        self.db_unpacker.create_account_log_table()

        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accountlog'")
            result = cursor.fetchone()

        self.assertIsNotNone(result, "The accountlog table should exist after creation.")

    def test_push_multiple_users_to_database(self):
        """ Test inserting at least four users into the real database. """

        # Define a list of multiple account data entries (at least 4)
        users_data = [
            {
                'User_ID': 1,
                'Account_Holder_Name': 'Test User 1',
                'User_name': 'test_user_1',
                'User_password': 'test_password_1',
                'Transaction_History': 'Sample transaction history 1',
                'Checking_Balance': 1000.0,
                'Savings_Balance': 2000.0,
                'Current_Budget_Warnings': 0
            },
            {
                'User_ID': 2,
                'Account_Holder_Name': 'Test User 2',
                'User_name': 'test_user_2',
                'User_password': 'test_password_2',
                'Transaction_History': 'Sample transaction history 2',
                'Checking_Balance': 3000.0,
                'Savings_Balance': 4000.0,
                'Current_Budget_Warnings': 1
            },
            {
                'User_ID': 3,
                'Account_Holder_Name': 'Test User 3',
                'User_name': 'test_user_3',
                'User_password': 'test_password_3',
                'Transaction_History': 'Sample transaction history 3',
                'Checking_Balance': 5000.0,
                'Savings_Balance': 6000.0,
                'Current_Budget_Warnings': 2
            },
            {
                'User_ID': 4,
                'Account_Holder_Name': 'Test User 4',
                'User_name': 'test_user_4',
                'User_password': 'test_password_4',
                'Transaction_History': 'Sample transaction history 4',
                'Checking_Balance': 7000.0,
                'Savings_Balance': 8000.0,
                'Current_Budget_Warnings': 3
            }
        ]

        class MockAccount:
            def __init__(self, account_data):
                self.account_data = account_data

            def get_account_details(self, checking_balance, savings_balance, transactions):
                return self.account_data

        class MockTransactions:
            def __init__(self, checking_balance, savings_balance, transactions):
                self.balance = {
                    'Checking_balance': checking_balance,
                    'Savings_balance': savings_balance
                }
                self.transactions = transactions

        # Insert the users into the database
        for user_data in users_data:
            mock_account = MockAccount(user_data)
            mock_transactions = MockTransactions(
                user_data['Checking_Balance'],
                user_data['Savings_Balance'],
                user_data['Transaction_History']
            )
            self.db_unpacker.push_to_database(mock_account, mock_transactions)

        # Verify that the users were inserted correctly
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accountlog WHERE user_name LIKE 'test_user_%'")
            result = cursor.fetchall()

        # Assert that we have at least 4 users inserted
        self.assertEqual(len(result), 4, "There should be at least 4 test users in the database.")

        # Check that the user names and balances match the data we inserted
        for i, user_data in enumerate(users_data):
            self.assertEqual(result[i][2], user_data['User_name'],
                             f"The user_name should match {user_data['User_name']}.")
            self.assertEqual(result[i][5], user_data['Checking_Balance'],
                             f"The checking balance should match {user_data['Checking_Balance']}.")
            self.assertEqual(result[i][6], user_data['Savings_Balance'],
                             f"The savings balance should match {user_data['Savings_Balance']}.")


if __name__ == '__main__':
    unittest.main()
