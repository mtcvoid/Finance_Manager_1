"""
Module for handling user interaction for creating a new account in the Finance Manager application.

This module provides functions that guide the user through the process of creating a new account.
It handles user input validation, account creation confirmation, and displays an interface for
entering necessary information to create the account.

Functions:
-----------
- create_new_account_interface():
    Handles the user interaction for the account creation process, confirming whether the user
    wants to proceed and gathering necessary inputs.

- create_new_account():
    Gathers input from the user and creates a new Account object. This function ensures that the
    data entered by the user is valid, and prepares the account data for insertion into the database.

- print_account_creation_banner():
    Displays the banner and instructions for the account creation process, explaining to the user
    what information is required for creating a new account.

Dependencies:
-------------
- Requires the `Account` class from `accounts.account` to create new account objects.
- Requires the `Transactions` class from `accounting.transactions` to handle transaction-related data.
- Requires the `DatabaseUnpacker` class from `data_base_handler` to manage database operations.
- Requires input validation and user interaction functions from `interface.user_interaction`
  (e.g., `input_with_validation`, `get_user_confirmation`).
"""

from interface.user_interface_general import *
from account_objects.accounts.account import Account
from account_objects.accounting.transactions import *
from data_handler.database.data_base_handler import *


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
        create_account = get_user_confirmation('Create a new account? (Y)es, (N)o: ')
        if not create_account:
            print('Exiting account creation...')
            return None  # User chooses not to create a new account

        account = create_new_account()
        if account:
            print('Account Created Successfully!')
            return account


def create_new_account():
    """
       Gathers user input, creates an Account object, and stores the account data in the database.

       This function is responsible for guiding the user through the process of creating a new account by
       prompting for the required information such as username, password, account holder name, and account name.
       It validates each input step using the `input_with_validation` function to ensure correct and valid data.
       If any input is invalid or the user cancels at any step, the function returns `None`.

       Once all the required information is gathered, the function creates an `Account` object and a
       `Transactions` object for the user. It then combines the account and transaction data using the
       `DatabaseUnpacker` to prepare the information for insertion into the 'accountlog' table in the database.

       Finally, the account information, including balances and transaction history, is inserted into
       or updated in the database using the `push_to_database` method.

       Parameters:
       -----------
       None

       Returns:
       --------
       Account :
           The created `Account` object containing the provided information (username, password,
           account holder name, account name).

       None :
           If the user cancels the account creation process or provides invalid inputs at any stage.

       Steps:
       ------
       1. **Input Gathering**:
           - The function prompts the user for:
               - `Username`: Unique identifier for the account.
               - `Password`: Account password.
               - `Account holder name`: Name of the person who owns the account.
               - `Account name`: A custom name for the account (e.g., "John's Savings").
           - If any input validation fails, the function exits and returns `None`.

       2. **Account Creation**:
           - An `Account` object is created using the gathered user input.

       3. **Transaction Setup**:
           - A `Transactions` object is created to manage the initial checking and savings balances.
           - The method `new_balance_setter()` from `Transactions` is called to set up the user's initial balances.

       4. **Data Handling**:
           - A `DatabaseUnpacker` object is created to handle the preparation of the account data.
           - The `get_data()` method is called to combine the account and transaction data into a structured format.

       5. **Database Insertion**:
           - The combined account data is inserted or updated in the database by calling `push_to_database()`, which
             stores the account details and the initial transaction history into the 'accountlog' table.
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

    # Creates account object from user input
    account = Account(user_name, new_password, holder_name, account_name)

    # sets up object to pull data from new account
    data_handler = DatabaseUnpacker()

    # creates transaction object for new user to set check
    get_tran_data = Transactions()

    new_user_tran = get_tran_data.new_balance_setter()

    account_holder = data_handler.get_data(account, new_user_tran)

    # pushes data to database
    data_handler.push_to_database(account_holder)


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
