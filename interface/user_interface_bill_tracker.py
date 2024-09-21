"""
User Interface for Bill Tracker

This module handles the interaction between the user and the bill tracking system. It provides
functions that allow users to add new bills, retrieve bill reminders, and (in the future)
remove bills. The module integrates with the `BillHandler` class for bill management and
interacts with the database to store and retrieve bill-related information.

Main Features:
- **Add Bills**: Prompts the user to enter details for a new bill (name, total amount, and due date)
  and adds the bill to the user's account, which is then saved to the database.
- **Bill Reminders**: Retrieves all bills from the database, calculates the number of days until
  their due date, and displays the reminders to the user.
- **Remove Bills**: A placeholder function for removing bills from the user's account (functionality
  to be implemented).

Functions:
    - `user_add_bill(active_user_account)`: Collects user input to add a new bill to the user's account
      and updates the database with the new bill information.
    - `user_remove_bill(active_user_account)`: (Currently a placeholder) Will allow the user to remove
      a bill from their account.
    - `user_get_bill_reminders(active_user_account)`: Retrieves bill reminders from the database and
      displays the due dates for the user's bills.

Dependencies:
    - `time`: Used to introduce delays for user experience, e.g., returning to menus.
    - `interface.user_interface_general`: Provides helper functions for user interactions, such as input validation
      and confirmations.
    - `mods.bill_tracker.bill_tracking_handler`: The `BillHandler` class is used for managing bill logic.
    - `data_handler.database.data_base_handler`: Interacts with the database to store and retrieve user bills.

Usage Example:
    active_user_account = get_active_user()  # Assume this retrieves the currently logged-in user.
    user_add_bill(active_user_account)       # Allows the user to add a new bill.
    user_get_bill_reminders(active_user_account)  # Retrieves and displays bill reminders.

Notes:
    - The `DatabaseUnpacker` class handles interactions with the database, ensuring that bill data is
      correctly saved and retrieved.
    - The date format for due dates must follow the 'YYYY-MM-DD' format.
"""
import time

from interface.user_interface_general import *
from mods.bill_tracker.bill_tracking_handler import *


def user_add_bill(active_user_account):
    """
    Prompts the user to add a new bill to their account and updates the database with the new bill information.

    The function interacts with the user by collecting information about the bill (such as the name, total amount,
    and due date) and adds this information to the bill tracker. It then updates the user's account in the database
    with the new bill.

    Args:
        active_user_account (object): The active user's account object, which contains their account details.

    Flow:
        1. Prompts the user for bill details.
        2. Adds the bill to the user's account through the `BillHandler`.
        3. Updates the user's account information in the database.
        4. Returns to the previous menu.

    """
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

        handler.append(bill_handler.bills)

        current_data[BILLS] = handler

        # Push the updated account data back into the database to save the changes
        pusher_puller.push_to_database(current_data)

        # returns to previous menu
        from interface.menu_handler import menu_maker
        print('Returning to Bill Tracking menu')
        time.sleep(2)
        menu_maker('Bill Tracker', active_user_account)
    else:
        from interface.menu_handler import menu_maker
        print('Returning to Bill Tracking menu')
        time.sleep(2)
        menu_maker('Bill Tracker', active_user_account)


def user_remove_bill(active_user_account):
    """
    Placeholder function for removing a bill from the user's account.

    Args:
        active_user_account (object): The active user's account object, which contains their account details.

    Note:
        This function is currently a placeholder and has no implemented functionality.
    """
    pass


def user_get_bill_reminders(active_user_account):
    """
    Retrieves and displays bill reminders for the user's account.

    This function pulls the user's bill data from the database and uses the `BillHandler` class to
    calculate how many days are left until each bill's due date. The reminders are then displayed
    to the user.

    Args:
        active_user_account (object): The active user's account object, which contains their account details.

    Flow:
        1. Retrieves the user's bill data from the database.
        2. Uses the `BillHandler` to calculate the days left until each bill's due date.
        3. Displays the reminders for each bill.
        4. Returns to the Bill Tracking menu.
    """
    from data_handler.database.data_base_handler import DatabaseUnpacker
    from interface.menu_handler import menu_maker

    # objects for handling bill logic and database transfer
    bill_handler = BillHandler()
    pusher_puller = DatabaseUnpacker()

    # Get the active user's account details.
    active = active_user_account.get_account_details()
    current_data = pusher_puller.pull_from_database(active[USER_ID])

    # Pulls 'bills' from current data in list form to then be added to the bill handler.
    data_transfer = current_data[BILLS]
    for item in data_transfer:
        bill_handler.bills.append(item)

    # Gets current time and prints out all bill information to user.
    bill_handler.get_bill_reminders()

    # Return to the previous menu.
    print('Returning to main menu....')
    time.sleep(2)
    menu_maker('Bill Tracker', active_user_account)
