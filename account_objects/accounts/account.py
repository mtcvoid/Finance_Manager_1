import json
from account_objects.accounting.transactions import Transactions


class Account:
    """
    Represents a user account with basic details such as user ID, account holder name, and account type.

    This class allows account holders to manage their account details, view account information,
    and check transactions. It also handles password and transaction history for the account.

    Attributes:
        _account_name (str): The name of the account.
        holder_name (str): The name of the account holder.
        _user_id (int): A unique user ID (initialized to a static value of 654).
        user_name (str): The username for the account.
        _user_password (str): The password associated with the account.
        transactions (list): A list of transactions associated with the account.
        current_budget_warnings (int): A counter for budget warnings issued to the account holder.
    """

    def __init__(self, user_name: str, new_password: str,
                 holder_name: str = "", account_name: str = None):
        """
          Initializes the Account object with the user's details.

          Args:
              user_name (str): The username for the account.
              new_password (str): The password for the account.
              holder_name (str, optional): The name of the account holder (default is an empty string).
              account_name (str, optional): The name of the account (default is None).
          """
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = 654  # this will be used as an ID . All objects will be named account?
        self.user_name = user_name
        self._user_password = new_password
        self.transactions = []
        self.current_budget_warnings = 0

    def view_account_details(self, checking_balance, savings_balance):
        """
        Displays the account details, including the checking and savings balances.

        Args:
            checking_balance (float): The current balance of the checking account.
            savings_balance (float): The current balance of the savings account.

        Returns:
            str: A formatted string containing the account details, such as account ID, account holder name,
                 and balances for both checking and savings accounts.
        """
        return (f"""
********************************
Account ID: {self._user_id}
Account Holder: {self.holder_name}
Checking Balance: {checking_balance}
Savings Balance: {savings_balance}
********************************""")

    def get_account_details(self):
        """
        Retrieves a detailed view of the account, including transaction history and balances.

        This method is intended for backend operations or administrative purposes, providing details
        such as the user ID, account holder name, username, password, transaction history, and current
        balances of both checking and savings accounts.

        Returns:
            dict: A dictionary containing the account details, including:
                - User ID
                - Account holder name
                - Username
                - Password (in plain text)
                - Transaction history (in JSON format)
                - Checking balance
                - Savings balance
                - Budget warnings
        """
        tran = Transactions()
        trans_history = tran.transactions

        return {'User_ID': self._user_id, 'Account_Holder_Name': self.holder_name, 'User_name': self.user_name,
                'User_password': self._user_password, 'Transaction_History': json.dumps(trans_history),
                'Checking_Balance': tran.balance['Checking_balance'], 'Savings_Balance': tran.balance['Savings_balance'],
                'Current_Budget_Warnings': self.current_budget_warnings}
