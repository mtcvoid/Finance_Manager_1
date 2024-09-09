from context_manager.context_manager import ContextManager


class DatabaseUnpacker:
    """
    A class responsible for interacting with a SQLite database to store and retrieve account
    information. This class provides methods for creating the necessary table, inserting or updating
    account data, and pulling account information from the database based on the user ID.
    """

    def get_data(self, account, tran):
        """
         Retrieves account details and transaction information to prepare it for database insertion.

         Parameters:
             account (Account): An object containing account details such as user name, balance, and password.
             tran (Transactions): An object that holds transaction history and current balances.

         Returns:
             dict: A dictionary containing the account details and transaction information, structured for insertion
                   into the database.
         """
        account_data = account.get_account_details(tran.balance['Checking_balance'],
                                                   tran.balance['Savings_balance'],
                                                   tran.transactions)
        return account_data

    def create_account_log_table(self):
        """
        Creates the 'accountlog' table in the 'BankingData.db' SQLite database if it does not already exist.
        This table is used to store account-related information such as userID, account holder name, and balances.

        The table includes the following fields:
        - userID: The primary key (unique identifier for the user).
        - account_holder_name: The name of the account holder.
        - user_name: The username for the account.
        - user_password: The password for the account.
        - transaction_history: A log of account transactions.
        - checking_balance: The balance in the checking account.
        - savings_balance: The balance in the savings account.
        - current_budget_warnings: A count of any budget warnings associated with the account.
        """
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS accountlog(userID integer primary key, account_holder_name '
                           'text, user_name text, user_password text, transaction_history text, checking_balance '
                           'integer, savings_balance integer, current_budget_warnings integer)')

    def push_to_database(self, account, tran):
        """
        Inserts or updates account information in the 'accountlog' table of the 'BankingData.db' database.
        If an account with the same userID already exists, it will update the existing record. Otherwise,
        it will insert a new record.

        Parameters:
            account (Account): An object containing account details such as user name, balance, and password.
            tran (Transactions): An object that holds transaction history and current balances.
        """
        account_data = self.get_data(account, tran)
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO accountlog (userID, account_holder_name, user_name, user_password, 
                                        transaction_history, checking_balance, savings_balance, current_budget_warnings)
                VALUES (:User_ID, :Account_Holder_Name, :User_name, :User_password, 
                        :Transaction_History, :Checking_Balance, :Savings_Balance, :Current_Budget_Warnings)
                ON CONFLICT(userID) DO UPDATE SET 
                    account_holder_name = excluded.account_holder_name,
                    user_name = excluded.user_name,
                    user_password = excluded.user_password,
                    transaction_history = excluded.transaction_history,
                    checking_balance = excluded.checking_balance,
                    savings_balance = excluded.savings_balance,
                    current_budget_warnings = excluded.current_budget_warnings
            ''', account_data)

    def pull_from_database(self, user_id):
        """
        Retrieves the account information for a specific user from the 'accountlog' table in the 'BankingData.db'
        database. The information is printed to the console.

        Parameters:
            user_id (int): The user ID of the account you want to retrieve from the database.

        Returns:
            None: The account information is printed to the console. If no account is found, a message is printed.
        """
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            # Use a WHERE clause to filter by userID
            cursor.execute('SELECT * FROM accountlog WHERE userID = ?', (user_id,))
            row = cursor.fetchone()  # Fetch only one row corresponding to the specific userID

            if row:
                # Map the fetched row into a dictionary
                account_info = {
                    'user_id': row[0],
                    'Account_Holder_Name': row[1],
                    'user_name': row[2],
                    'user_password': row[3],
                    'transaction_history': row[4],
                    'checking_balance': row[5],
                    'savings_balance': row[6],
                    'current_budget_warnings': row[7]
                }

                # Print the account info
                for key, value in account_info.items():
                    print(f'{key}: {value}')
            else:
                print(f'No account found for userID: {user_id}')
