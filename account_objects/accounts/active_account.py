from data_handler.variables.constants import *


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

    def get_account_details(self):
        return {USER_ID: self._user_id, ACCOUNT_HOLDER_NAME: self.holder_name, USER_NAME: self.user_name,
                USER_PASSWORD: self._user_password, TRANSACTION_HISTORY: self.transactions,
                CHECKING_BALANCE: self.checking_balance,
                SAVINGS_BALANCE: self.savings_balance,
                CURRENT_BUDGET_WARNINGS: self.current_budget_warnings}
