"""
Bill Tracking Handler Module

This module provides a `BillHandler` class that facilitates the tracking and management of bills.
It offers functionalities for adding, removing, and tracking due dates for bills, as well as
reminding users of upcoming due dates and marking bills as paid.

Main Features:
- **Add bills**: Allows users to add new bills with details such as the bill name, total amount,
  due date, and whether the bill has been paid.
- **Remove bills**: Supports removing bills from the tracking list by their name.
- **Due date reminders**: Calculates how many days are left until the due date for each bill and
  displays reminders.
- **Payment tracking**: Bills can be marked as paid once they have been settled.

Classes:
    - BillHandler: The main class that manages all bill-related operations.

Dependencies:
    - `datetime`: For handling dates and calculating due dates.
    - `data_handler.variables.constants`: Contains constants such as `BILLS`, `TOTAL`, `DUE_DATE`, `CURRENT_DATE`,
      `PAID`, `NO`, and `YES` used throughout the module.

Usage Example:
    handler = BillHandler()
    handler.add_bill("Electricity", 100.0, "2024-09-25", datetime.now())
    handler.get_bill_reminders()
    handler.bill_paid("Electricity")

Notes:
    - Ensure that `data_handler.variables.constants` is properly configured with the necessary constants
      before using this module.
    - The date format for due dates must be in the 'YYYY-MM-DD' format.

"""

from datetime import datetime
from data_handler.variables.constants import *


class BillHandler:
    """
    A class to handle bill management, including adding, removing, tracking due dates,
    and marking bills as paid.

    Attributes:
        bills (list): A list to store bill information.
        bill_reminders (list): A list to store reminder information for bills.
    """
    def __init__(self):
        self.bills = []
        self.bill_reminders = []

    def add_bill(self, bill_name: str, bill_total: float, due_date: str, current_date, paid=NO, days=None):
        """
        Adds a new bill to the list of bills.

        Args:
            bill_name (str): The name of the bill.
            bill_total (float): The total amount of the bill.
            due_date (str): The due date of the bill in 'YYYY-MM-DD' format.
            current_date (datetime): The current date.
            paid (str, optional): The paid status of the bill. Default is NO.
            days (int, optional): Days remaining until the due date. Default is None.
        """
        self.bills.append({BILLS: bill_name, TOTAL: bill_total, DUE_DATE: due_date, CURRENT_DATE: current_date,
                           PAID: paid, DAYS: days})

    def remove_bill(self, bill_name):
        """
        Removes a bill from the list of bills based on its name.

        Args:
            bill_name (str): The name of the bill to be removed.
        """
        for bill in self.bills:
            if bill[BILLS] == bill_name:
                self.bills.remove(bill)
                return self.bills

    def get_bill_reminders(self):
        """
        Retrieves reminders for all bills, calculating the days left until the due date
        and printing the reminder information for each bill.
        """
        for bill in self.bills:

            bill_name = bill.get(BILLS)

            current_date = datetime.now().date()

            due_date = datetime.strptime(bill.get(DUE_DATE), '%Y-%m-%d').date()

            days = (due_date - current_date).days

            paid = bill.get(PAID)

            print(
f'''Bill: {bill_name}
Due: {due_date}
Days till due: {days}
paid: {paid}
```````````````````''')

    def bill_paid(self, bill_name):
        """
        Marks a bill as paid based on its name.

        Args:
            bill_name (str): The name of the bill to mark as paid.
        """
        for bill in self.bills:
            if bill[BILLS] == bill_name:
                bill[PAID] = YES
