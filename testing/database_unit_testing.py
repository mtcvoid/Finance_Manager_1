import unittest
import sqlite3
from database.data_base_handler import DatabaseUnpacker

class TestDatabaseUnpackerRealDB(unittest.TestCase):

    def setUp(self):
        """ Set up a connection to the real database for each test. """
        self.db_file = 'BankingData.db'  # Path to the actual database file
        self.db_unpacker = DatabaseUnpacker()

        # Ensure the table exists
        self.db_unpacker.create_account_log_table()

    def tearDown(self):
        """ Clean up any test data in the database after each test. """
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM accountlog WHERE user_name = 'test_user'")
            conn.commit()

    def test_create_account_log_table(self):
        """ Test the creation of the accountlog table. """
        # This test will run the actual method to create the table in the database
        self.db_unpacker.create_account_log_table()

        # Now let's check if the table exists
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accountlog'")
            result = cursor.fetchone()

        self.assertIsNotNone(result, "The accountlog table should exist after creation.")

    def test_push_to_database(self):
        """ Test inserting or updating account information into the real database. """
        account_data = {
            'User_ID': 1,
            'Account_Holder_Name': 'Test User',
            'User_name': 'test_user',
            'User_password': 'test_password',
            'Transaction_History': 'Sample transaction history',
            'Checking_Balance': 5000.0,
            'Savings_Balance': 3000.0,
            'Current_Budget_Warnings': 0
        }

        class MockAccount:
            def get_account_details(self, checking_balance, savings_balance, transactions):
                return account_data

        class MockTransactions:
            balance = {'Checking_balance': 5000.0, 'Savings_balance': 3000.0}
            transactions = 'Sample transaction history'

        # Use the actual push_to_database method to insert the data
        self.db_unpacker.push_to_database(MockAccount(), MockTransactions())

        # Verify that the data was inserted correctly
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accountlog WHERE user_name = 'test_user'")
            result = cursor.fetchone()

        # Assert that the data matches what we inserted
        self.assertIsNotNone(result, "The test user should be inserted into the database.")
        self.assertEqual(result[2], 'test_user', "The user_name should match 'test_user'.")
        self.assertEqual(result[5], 5000.0, "The checking balance should match 5000.0.")
        self.assertEqual(result[6], 3000.0, "The savings balance should match 3000.0.")

    def test_pull_from_database(self):
        """ Test pulling account information from the real database. """
        account_data = {
            'User_ID': 1,
            'Account_Holder_Name': 'Test User',
            'User_name': 'test_user',
            'User_password': 'test_password',
            'Transaction_History': 'Sample transaction history',
            'Checking_Balance': 5000.0,
            'Savings_Balance': 3000.0,
            'Current_Budget_Warnings': 0
        }

        class MockAccount:
            def get_account_details(self, checking_balance, savings_balance, transactions):
                return account_data

        class MockTransactions:
            balance = {'Checking_balance': 5000.0, 'Savings_balance': 3000.0}
            transactions = 'Sample transaction history'

        # Insert the data into the database
        self.db_unpacker.push_to_database(MockAccount(), MockTransactions())

        # Now we pull the data from the database and verify the output
        self.db_unpacker.pull_from_database(1)  # Assuming userID is 1

        # Check the database for verification
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accountlog WHERE userID = 1")
            result = cursor.fetchone()

        # Assert that the data is present
        self.assertIsNotNone(result, "The account should exist for userID 1.")

if __name__ == '__main__':
    unittest.main()
