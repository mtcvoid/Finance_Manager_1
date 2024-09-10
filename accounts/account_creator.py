from Interface.user_interaction import *
from accounts.account import Account


def create_new_account_interface():
    """
    Handles the user interaction for account creation.
    Returns an Account object or None if the process is canceled.
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
    Gathers input and creates an account.
    Returns an Account object or None if canceled.
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
    Prints the account creation banner.
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
