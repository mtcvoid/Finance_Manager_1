from accounts.account import Account


# Step 1: Separate account creation logic from user interaction
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


# Step 2: Refactor the input gathering logic
def input_with_validation(field_name):
    """
    Handles input validation and allows users to confirm their input.
    Returns the validated input or None if the user cancels the process.
    """
    while True:
        user_input = input(f'Please enter {field_name}: ')
        if get_user_confirmation(f'Is this correct: {user_input}? (Y)es, (N)o'):
            return user_input
        else:
            retry_or_exit = get_retry_or_exit_choice()
            if retry_or_exit == 'exit':
                return None  # User decided to cancel


def get_user_confirmation(prompt):
    """
    Returns True if the user confirms 'Y', False if 'N'.
    """
    while True:
        choice = input(prompt).lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Invalid choice, please enter (Y)es or (N)o.')


def get_retry_or_exit_choice():
    """
    Offers the user the choice to retry input or exit the process.
    Returns 'retry' to retry the input or 'exit' to cancel the process.
    """
    while True:
        choice = input("(1) Try again\n(2) Exit to main interface\nEnter choice: ")
        if choice == '1':
            return 'retry'
        elif choice == '2':
            return 'exit'
        else:
            print('Invalid choice. Please select 1 or 2.')


# Step 3: Clean up the interface
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