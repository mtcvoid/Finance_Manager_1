import json
from account_objects.accounting.transactions import Transactions


class ActiveAccount:
    def __init__(self, user_id: int, holder_name: str, user_name: str, user_password,
                 transactions: list, checking_balance: int, savings_balance: int, c_b_w: int):
        self.holder_name = holder_name
        self._user_id = user_id
        self.user_name = user_name
        self._user_password = user_password
        self.transactions = transactions
        self.current_budget_warnings = c_b_w
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    def __repr__(self):
        # Returning dictionary representation in __repr__
        return {
            "user_id": self._user_id,
            "Account_Holder_Name": self.holder_name,
            "user_name": self.user_name,
            "checking_balance": self.checking_balance,
            "savings_balance": self.savings_balance,
            "current_budget_warnings": self.current_budget_warnings,
            "transaction_history": self.transactions
        }

    def view_account_details(self, checking_balance, savings_balance):
        return (f"""
********************************
Account ID: {self._user_id}
Account Holder: {self.holder_name}
Checking Balance: {checking_balance}
Savings Balance: {savings_balance}
********************************""")

    def get_account_details(self):
        return {'User_ID': self._user_id, 'Account_Holder_Name': self.holder_name, 'User_name': self.user_name,
                'User_password': self._user_password, 'Transaction_History': json.dumps(self.transactions),
                'Checking_Balance': self.checking_balance,
                'Savings_Balance': self.savings_balance,
                'Current_Budget_Warnings': self.current_budget_warnings}
