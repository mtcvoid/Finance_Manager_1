"""
logic for bills
"""
from datetime import datetime
from data_handler.variables.constants import *


class BillHandler:

    def __init__(self):
        self.bills = []
        self.bill_reminders = []

    def add_bill(self, bill_name: str, bill_total: float, due_date: str, current_date, paid=NO, days=None):
        self.bills.append({BILLS: bill_name, TOTAL: bill_total, DUE_DATE: due_date, CURRENT_DATE: current_date, PAID: paid, DAYS: days})

    def remove_bill(self, bill_name):
        for bill in self.bills:
            if bill[BILLS] == bill_name:
                self.bills.remove(bill)

    def get_bill_reminders(self, bill_name):

        for bill in self.bills:
            current_date = datetime.now().date()
            days = (bill[DUE_DATE] - current_date).days
            bill[DAYS] = days
            bill[CURRENT_DATE] = current_date
            self.bill_reminders.append(bill)

        return self.bill_reminders

    def bill_paid(self, bill_name):
        for bill in self.bills:
            if bill[BILLS] == bill_name:
                bill[PAID] = YES
