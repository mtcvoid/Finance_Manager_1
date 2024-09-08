from accounts.account import Account
from accounting.transactions import Transactions
from context_manager.context_manager import ContextManager

matt = Account('OnlineBanker', 'tester12345',
               'Matthew Thomas', 'Online investments')

m_t = Transactions()

m_t.deposit_withdrawal('Checking', 'Deposit', 1234)
m_t.deposit_withdrawal('Checking', 'Withdrawal', 480)
m_t.deposit_withdrawal('Savings', 'Deposit', 620)
m_t.deposit_withdrawal('Checking', 'Deposit', 68)


def get_data(account, tran):
    account_data = account.get_account_details(tran.balance['Checking_balance'],
                                               tran.balance['Savings_balance'],
                                               tran.transactions)
    return account_data


def create_account_log_table():
    with ContextManager('BankingData.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS accountlog(userID integer primary key, account_holder_name '
                       'text, user_name text, user_password text, transaction_history text, checking_balance '
                       'integer, savings_balance integer, current_budget_warnings integer)')


def push_to_database(account, tran):
    account_data = get_data(account, tran)
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


def pull_from_database():
    pass

print(matt._user_id)
push_to_database(matt, m_t)
