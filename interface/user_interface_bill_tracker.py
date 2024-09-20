"""
handles user interaction for bill tracker
"""
import time

from interface.user_interface_general import *
from mods.bill_tracker.bill_tracking_handler import *


def user_add_bill(active_user_account):
    print("""
    You will need the following information to add a bill to your account: 
    - Name of bill
    - Bill total
    - Date the bill is due (YYYY-MM-DD)
    """)

    # Importing DatabaseUnpacker inside the function to avoid potential circular imports.

    confirmation = get_user_confirmation("Would you like to add a bill? (Y)/(N): ")
    if confirmation:

        from data_handler.database.data_base_handler import DatabaseUnpacker

        # objects for handling bill logic and database transfer
        bill_handler = BillHandler()
        pusher_puller = DatabaseUnpacker()

        # Get the active user's account details (such as balances, transaction history, etc.)
        active = active_user_account.get_account_details()

        # Pull the current data of the user from the database, using the user's ID as a key
        current_data = pusher_puller.pull_from_database(active[USER_ID])

        # Retrieve the current bills list  from the database and set it in the bills object
        handler = current_data[BILLS]

        # get users information  and adds new bill to bill object
        name = input_with_validation('bill name: ')
        total = input_with_validation('bill total: ')
        date = input_with_validation('bill due date (YYYY-MM-DD): ')

        # adds bill to handler
        bill_handler.add_bill(name, total, date, current_date=None, paid=None, days=None)

        # bill object gets transferred back to user for push to database
        for bill in bill_handler.bills:
            handler.append(bill)

        # Push the updated account data back into the database to save the changes
        pusher_puller.push_to_database(handler)

        # returns to previous menu
        from interface.menu_handler import previous_menu
        print('Returning to Bill Tracking menu')
        time.sleep(2)
        previous_menu(active_user_account, 'Bill Tracker')
    else:
        from interface.menu_handler import previous_menu
        print('Returning to Bill Tracking menu')
        time.sleep(2)
        previous_menu(active_user_account, 'Bill Tracker')


def user_remove_bill(active_user_account):
    pass


def user_view_all_bills():
    bill = BillHandler()
    bill.add_bill('Comcast', 150.35, "2024-10-05")

    for item in bill.bills:
        for key, value in item.items():
            print(key, value)
def user_set_reminder():
    pass