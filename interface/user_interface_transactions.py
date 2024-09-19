"""
Module: Transaction Interaction

This module handles user interactions related to bank account transactions such as deposits, withdrawals,
and balance inquiries. It provides functions for confirming and processing transactions, updating account
data, and displaying the current account balance.

Key Functions:
--------------
1. transaction_interaction(transaction_type, active_user_account):
   - Manages user input and interaction for performing a transaction (deposit or withdrawal).
   - Prompts the user to confirm the transaction type and account (checking/savings).
   - Validates and confirms the transaction amount, then processes the transaction.

2. transaction_view_balance(active_user_account):
   - Displays the current balances for the checking and savings accounts of the active user.
   - Retrieves and shows the account holder's name, checking balance, savings balance, and total balance.

3. transaction_handler(account, transaction_type, amount, active_user_account):
   - Executes a deposit or withdrawal on the specified account (checking or savings).
   - Interacts with the database to update account balances and transaction history after processing the transaction.

Imports and Circular Dependency Handling:
------------------------------------------
To prevent circular imports, certain modules (like `DatabaseUnpacker` and `active_user_menu`) are imported
inside functions rather than globally at the top of the module. This ensures that functionality is accessible
without causing import loops in a multi-module project.

Usage:
------
This module is designed to be part of a banking system, where the user can initiate and process transactions
and view their account balances. It relies on user input and interaction to confirm actions before processing
transactions.
"""
from interface.user_interface_general import get_user_confirmation
from account_objects.accounting.transactions import *
import time


def transaction_interaction(transaction_type, active_user_account):
    """
    Manages user interaction for performing a transaction (deposit/withdrawal) on the user's accounts.

    Args:
        transaction_type (str): The type of transaction being performed, e.g., 'deposit' or 'withdrawal'.
        active_user_account (object): An instance of the ActiveAccount class representing the active user.

    Flow:
        - Confirms the type of transaction with the user (deposit or withdrawal).
        - Prompts the user to select either the checking or savings account for the transaction.
        - Asks the user to input the transaction amount and confirms the correctness.
        - Calls transaction_handler to process the transaction and update the database.
        - Returns to the account menu after completing or canceling the transaction.
    """

    transaction_confirmed = get_user_confirmation(f'You are making a {transaction_type}. Is this correct? (Y)/(N)')

    while transaction_confirmed:

        c_or_s = input('Checking or savings: ').lower()

        # Ensure the account type is either 'checking' or 'savings'
        if c_or_s in ['checking', 'savings']:

            amount = input(f'How much would you like to {transaction_type} into {c_or_s}: ')

            if amount.isdigit():

                amount_confirmation = get_user_confirmation(f'${amount} Correct? (Y)/(N)')

                # If the user confirms the amount, process the transaction
                if amount_confirmation:
                    amount = float(amount)  #
                    transaction_handler(c_or_s, transaction_type, amount, active_user_account)
                    transaction_confirmed = False  # Exit the loop once the transaction is successfully processed
                else:
                    print('Please try again...')
            else:
                print('Invalid amount. Please enter a numeric value.')
        else:
            print('Please enter a valid account type (checking/savings).')

    print('Returning to account menu...')

    from interface.menu_handler import active_user_menu

    time.sleep(2)

    active_user_menu(active_user_account)


def transaction_view_balance(active_user_account):
    """
    Displays the current balance for both checking and savings accounts of the active user.

    Args:
        active_user_account (object): An instance of ActiveAccount representing the active user.

    Flow:
        - Retrieves the user's account details from the database.
        - Displays the account holder's name, the checking and savings account balances, and the total balance.
        - Returns control to the active user menu after a short delay.
    """
    # Import menu header for displaying the account header and database handler for interacting with the database
    from interface.menu_handler import menu_header
    from data_handler.database.data_base_handler import DatabaseUnpacker

    # Create an instance of DatabaseUnpacker to retrieve data from the database
    puller = DatabaseUnpacker()

    # Get the active user's account details (such as user ID)
    active = active_user_account.get_account_details()

    # Pull the balance data from the database using the active user's ID
    balance_viewer = puller.pull_from_database(active[USER_ID])

    # Calculate the total balance by adding checking and savings account balances
    total = balance_viewer[CHECKING_BALANCE] + balance_viewer[SAVINGS_BALANCE]

    # Display the account holder's name using the menu header and print the account balances
    menu_header(balance_viewer[ACCOUNT_HOLDER_NAME])
    print('        ACCOUNT BALANCES')
    print(f"""
    Checking Balance: ${balance_viewer[CHECKING_BALANCE]}
    Savings Balance: ${balance_viewer[SAVINGS_BALANCE]}
    Total balance: ${total}
        """)
    print("    ******************************")

    # Print a message to indicate that the function is returning to the account menu
    print('Returning to account menu...')

    # Import the menu for returning the user to the account menu and add a short delay before calling it
    from interface.menu_handler import active_user_menu
    time.sleep(2)

    # Return control to the active user menu after displaying the balance
    active_user_menu(active_user_account)


def transaction_handler(account, transaction_type, amount, active_user_account):
    """
    Handles deposit or withdrawal transactions for the user's account.

    Args:
        account (str): The type of account to transact with, either 'checking' or 'savings'.
        transaction_type (str): The type of transaction being performed, e.g., 'deposit' or 'withdrawal'.
        amount (float): The amount of money to be deposited or withdrawn.
        active_user_account (object): An instance of the ActiveAccount class containing user account details.

    Flow:
        - Retrieves current account data from the database based on the active user's account.
        - Updates the balance and transaction history according to the transaction (deposit/withdrawal).
        - Saves the updated data back to the database.
    """
    # Importing DatabaseUnpacker inside the function to avoid potential circular imports.
    from data_handler.database.data_base_handler import DatabaseUnpacker

    # Create an instance of DatabaseUnpacker to interact with the database
    pusher_puller = DatabaseUnpacker()

    # Create an instance of Transactions to handle the transaction logic
    transaction = Transactions()

    # Get the active user's account details (such as balances, transaction history, etc.)
    active = active_user_account.get_account_details()

    # Pull the current data of the user from the database, using the user's ID as a key
    current_data = pusher_puller.pull_from_database(active[USER_ID])

    # Retrieve the current transaction history from the database and set it in the transaction object
    transaction.transactions = current_data[TRANSACTION_HISTORY]

    # Set the checking and savings balances in the transaction object from the current database data
    transaction.balance[CHECKING_BALANCE] = current_data[CHECKING_BALANCE]
    transaction.balance[SAVINGS_BALANCE] = current_data[SAVINGS_BALANCE]

    # Perform the transaction (deposit or withdrawal) on the specified account (checking/savings)
    transaction.deposit_withdrawal(account, transaction_type, amount)

    # Update the current account data with the new balances and transaction history
    current_data[CHECKING_BALANCE] = transaction.balance[CHECKING_BALANCE]
    current_data[SAVINGS_BALANCE] = transaction.balance[SAVINGS_BALANCE]
    current_data[TRANSACTION_HISTORY] = transaction.transactions

    # Push the updated account data back into the database to save the changes
    pusher_puller.push_to_database(current_data)
