"""
Module for handling user interaction for creating a new account in the Finance Manager application.

This module provides functions that guide the user through the process of creating a new account.
It handles user input validation, account creation confirmation, and displays an interface for
entering necessary information to create the account.

Functions:
-----------
- create_new_account_interface(): Handles the user interaction for the account creation process.
- create_new_account(): Gathers input from the user and creates a new Account object.
- print_account_creation_banner(): Displays the banner and instructions for the account creation process.

Dependencies:
-------------
- Requires the `Account` class from `accounts.account` to create new account objects.
- Requires input validation and user interaction functions from `interface.user_interaction`
  (e.g., `input_with_validation`, `get_user_confirmation`).
"""
from interface.user_interface_general import *
from account_objects.accounts.account import Account


def create_new_account_interface():
    """
    Handles the user interaction for account creation.

    This function manages the process of creating a new account by interacting with the user
    to gather necessary details, such as username, password, and account holder name. It confirms
    whether the user wants to proceed with the account creation or cancel the process.

    Returns:
    Account: The created Account object if the process is completed successfully.
    None: If the user chooses to cancel the account creation process.
    """
    print_account_creation_banner()

    while True:
        create_account = get_user_confirmation('Create a new account? (Y)es, (N)o')
        if not create_account:
            print('Exiting account creation...')
            return None  # User chooses not to create a new account

        account = create_new_account()
        if account:
            print('Account Created Successfully!')
            return account


def create_new_account():
    """
    Gathers input and creates an Account object.

    This function prompts the user for required information such as the username, password,
    account holder's name, and account name. It uses input validation functions to ensure
    that the data entered by the user is correct and allows the user to retry or exit the process.

    Returns:
    Account: The created Account object containing the provided information.
    None: If the user cancels the account creation process at any step.
    """
    user_name = input_with_validation("Username")
    if not user_name:
        return None

    new_password = input_with_validation("Password")
    if not new_password:
        return None

    holder_name = input_with_validation("Account holder name")
    if not holder_name:
        return None

    account_name = input_with_validation("Name for the account")
    if not account_name:
        return None

    return Account(user_name, new_password, holder_name, account_name)


def print_account_creation_banner():
    """
    Prints the account creation banner and instructions.

    This function displays the interface for the account creation process. It explains to the user
    what information will be required and provides instructions for filling out the account details.

    Returns:
    None
    """
    print(f"""
                   ####Finance Manager####
                *****************************
                      Account Creation
                *****************************
The following information will be required for creating a new account. 
        Please review all information for accuracy. 
                            **
       - Account username and password for logging into account.
       - Account holder full name.
       - A name for the Account. (Ex: John's Investment account)
            L All account's come with a checking and a savings
       - Initial fund's
                            **
    """)


