from account_objects.accounting.transactions import Transactions
from data_handler.variables.constants import *


class Account:
    def __init__(self, user_id: int, holder_name: str, user_name: str, user_password: str,
                 transactions=None, checking_balance=0, savings_balance=0,
                 c_b_w=None, bills=None, bill_reminders=None, monthly_income=None, expenses=None, budgets=None,
                 budget_alerts=None, current_debt=None, total_debt=None,
                 assets=None, credit_card_balances_and_limits=None, net_worth=None):
        self.holder_name = holder_name
        self._user_id = user_id
        self.user_name = user_name
        self._user_password = user_password
        self.transactions = transactions or []
        self.current_budget_warnings = c_b_w or []
        self.checking_balance = checking_balance or 0
        self.savings_balance = savings_balance or 0
        self.bills = bills or []
        self.bill_reminders = bill_reminders or []

        # these need added to database push and pull
        self.monthly_income = monthly_income or 0
        self.expenses = expenses or []
        self.budgets = budgets or []
        self.budget_alerts = budget_alerts or []
        self.current_debt = current_debt or []
        self.total_debt = total_debt or 0
        self.assets = assets or 0
        self.credit_card_balances_and_limits = credit_card_balances_and_limits or []
        self.net_worth = net_worth or 0

    def get_account_details(self) -> dict:
        return {USER_ID: self._user_id, ACCOUNT_HOLDER_NAME: self.holder_name, USER_NAME: self.user_name,
                USER_PASSWORD: self._user_password, TRANSACTION_HISTORY: self.transactions,
                CHECKING_BALANCE: self.checking_balance,
                SAVINGS_BALANCE: self.savings_balance,
                CURRENT_BUDGET_WARNINGS: self.current_budget_warnings,
                BILLS: self.bills, BILL_REMINDERS: self.bill_reminders, MONTHLY_INCOME: self.monthly_income,
                EXPENSES: self.expenses, BUDGETS: self.budgets, BUDGET_ALERTS: self.budget_alerts,
                CURRENT_DEBT: self.current_debt, TOTAL_DEBT: self.total_debt, ASSETS: self.assets,
                CREDIT_CARD_BALANCES_AND_LIMITS: self.credit_card_balances_and_limits, NETWORTH: self.net_worth}

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

        return {USER_ID: self._user_id, ACCOUNT_HOLDER_NAME: self.holder_name, USER_NAME: self.user_name,
                USER_PASSWORD: self._user_password, TRANSACTION_HISTORY: self.transactions,
                CHECKING_BALANCE: tran.balance[CHECKING_BALANCE],
                SAVINGS_BALANCE: tran.balance[SAVINGS_BALANCE],
                CURRENT_BUDGET_WARNINGS: self.current_budget_warnings,
                BILLS: self.bills, BILL_REMINDERS: self.bill_reminders, MONTHLY_INCOME: self.monthly_income,
                EXPENSES: self.expenses, BUDGETS: self.budgets, BUDGET_ALERTS: self.budget_alerts,
                CURRENT_DEBT: self.current_debt, TOTAL_DEBT: self.total_debt, ASSETS: self.assets,
                CREDIT_CARD_BALANCES_AND_LIMITS: self.credit_card_balances_and_limits, NETWORTH: self.net_worth}
