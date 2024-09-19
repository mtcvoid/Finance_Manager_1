"""
logic for bills
"""


class Bills:

    def __init__(self):
        self.bills = []

    def add_bill(self, bill_name: str, bill_total: float, due_date: str):
        self.bills.append({'Bill': bill_name, 'Total': bill_total, 'Due Date': due_date})

    def remove_bill(self, bill_name):
        for bill in self.bills:
            if bill['Bill'] == bill_name:
                self.bills.remove(bill)

    def view_all_bills(self):
        return self.bills
