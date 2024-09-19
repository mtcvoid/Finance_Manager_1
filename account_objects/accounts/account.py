import json
import random

from account_objects.accounting.transactions import Transactions
from data_handler.variables.constants import *


class Account:
    """
    Represents a user account with basic details such as user ID, account holder name, and account type.

    This class allows account holders to manage their account details, view account information,
    and check transactions. It also handles password and transaction history for the account.

    Attributes:

        holder_name (str): The name of the account holder.
        _user_id (int): A unique user ID (initialized to a static value of 654).
        user_name (str): The username for the account.
        _user_password (str): The password associated with the account.
        transactions (list): A list of transactions associated with the account.
        current_budget_warnings (int): A counter for budget warnings issued to the account holder.
    """

    def __init__(self, user_name: str, new_password: str,
                 holder_name: str = ""):
        """
          Initializes the Account object with the user's details.

          Args:
              user_name (str): The username for the account.
              new_password (str): The password for the account.
              holder_name (str, optional): The name of the account holder (default is an empty string).

          """

        self.holder_name = holder_name
        self._user_id = random.randint(1, 31324)  # this will be used as an ID . All objects will be named account?
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

    def get_new_account_details(self):
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

        return {USER_ID: self._user_id, ACCOUNT_HOLDER_NAME: self.holder_name, USER_NAME: self.user_name,
                USER_PASSWORD: self._user_password, TRANSACTION_HISTORY: self.transactions,
                CHECKING_BALANCE: tran.balance[CHECKING_BALANCE],
                SAVINGS_BALANCE: tran.balance[SAVINGS_BALANCE],
                CURRENT_BUDGET_WARNINGS: self.current_budget_warnings}
