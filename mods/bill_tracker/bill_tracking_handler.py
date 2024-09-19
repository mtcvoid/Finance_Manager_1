"""
logic for bills
"""
from datetime import datetime


class BillHandler:

    def __init__(self):
        self.bills = []

    def add_bill(self, bill_name: str, bill_total: float, due_date: str):

        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        except:
            raise ValueError('Due date must be formated  in YYYY-MM-DD')

        self.bills.append({'Bill': bill_name, 'Total': bill_total, 'Due Date': due_date})

    def remove_bill(self, bill_name):
        for bill in self.bills:
            if bill['Bill'] == bill_name:
                self.bills.remove(bill)

    def view_all_bills(self):
        return self.bills

    def set_bill_reminder(self):
        pass



