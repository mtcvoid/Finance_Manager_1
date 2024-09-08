from accounts.account import Account
from context_manager.context_manager import ContextManager
from accounting.transactions import Transactions

"""
WORK IN PROGRESS.

Need to figure out how to get the information from the account objects and move them over
to database.
"""


class DatabaseUnpacker:

    def get_data(self, account, tran):
        account_data = account.get_account_details(tran.balance['Checking_balance'],
                                                   tran.balance['Savings_balance'],
                                                   tran.transactions)
        return account_data

    def create_account_log_table(self):
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS accountlog(userID integer primary key, account_holder_name '
                           'text, user_name text, user_password text, transaction_history text, checking_balance '
                           'integer, savings_balance integer, current_budget_warnings integer)')

    def push_to_database(self, account, tran):
        account_data = self.get_data(account, tran)
        with ContextManager('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        INSERT INTO accountlog (userID, account_holder_name, user_name, user_password, 
                                                transaction_history, checking_balance, savings_balance,
                                                current_budget_warnings)
                        VALUES (:userID, :account_holder_name, :user_name, :user_password, :transaction_history, 
                                            :checking_balance, :savings_balance, :current_budget_warnings)
                    ''', account_data)

