import json


class Account:
    """
    Class that takes in a userID, account holder name, type of account(savings, checking, etc.), and initial funds.
    account will be able to update funds. Check transactions.
    """

    def __init__(self, user_name: str, new_password: str,
                 holder_name: str = "", account_name: str = None):
        """
        Takes in username, password, account holder name, and name of the account.
        :param user_name:
        :param new_password:
        :param holder_name:
        :param account_name:
        """
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = 555  # this will be used as an ID . All objects will be named account?
        self.user_name = user_name
        self._user_password = new_password
        self.transactions = []
        self.current_budget_warnings = 0

    def view_account_details(self, checking_balance, savings_balance):
        """
        Prints account details to user.
        """
        return (f"""
********************************
Account ID: {self._user_id}
Account Holder: {self.holder_name}
Checking Balance: {checking_balance}
Savings Balance: {savings_balance}
********************************""")

    def get_account_details(self, checking_balance, savings_balance, trans_history):
        """
        Returns a dictionary containing the detailed account information for administrative purposes.

        This method provides a comprehensive view of the account details, including the user ID,
        account holder name, username, password, transaction history, checking and savings balances,
        and any current budget warnings. It is intended for backend operations such as data manipulation
        or retrieval by administrators.

        Parameters:
        -----------
        checking_balance : float
            The current balance of the checking account.

        savings_balance : float
            The current balance of the savings account.

        trans_history : list
            A list of the transaction history associated with the account.

        :param checking_balance:
        :param savings_balance:
        :param trans_history:
        :return:
        """
        return {'User_ID': self._user_id, 'Account_Holder_Name': self.holder_name, 'User_name': self.user_name,
                'User_password': self._user_password, 'Transaction_History': json.dumps(trans_history),
                'Checking_Balance': checking_balance, 'Savings_Balance': savings_balance,
                'Current_Budget_Warnings': self.current_budget_warnings}

