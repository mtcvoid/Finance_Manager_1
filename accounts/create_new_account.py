from accounts.account import Account


def create_new_account():  # This logic needs to be moved to another place.
    while True:
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
        while True:
            y_n = input('Create a new account? (Y)es, (N)o')
            if y_n.lower() == 'y':
                user_name = new_account_getter("Username")
                new_password = new_account_getter('Password')
                holder_name = new_account_getter("Account holder name")
                account_name = new_account_getter('Name for the account')
                break

        account = Account(user_name, new_password, holder_name, account_name)
        print('Account Created')
        return account


def new_account_getter(getter_type: str):  # this logic needs to be moved to another palce
    routine_running = True
    while routine_running:
        getter = input(f'Please enter a {getter_type}: ')
        y_n = input(f'Is this correct: {getter}. (Y)es, (N)o')
        if y_n.lower() == 'y':
            return getter
        elif y_n.lower() == 'n':
            print('Please try again.')
            continue
        else:
            print('Please Enter a valid choice.')
            o_t = input("""
(1)Try again
(2)Exit to main Interface
                               """)
            if o_t == '1':
                continue
            else:
                routine_running = False
                # main_menu() # make this
