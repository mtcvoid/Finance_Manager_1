"""
handles user interaction for transactions
"""
from interface.user_interface_general import get_user_confirmation
from account_objects.accounting.transactions import *


def transaction_interaction(transaction_type, active_user_account):  # logic needs fixed. No need for the same code 2x
    transaction_confirmed = get_user_confirmation(f'You are making a {transaction_type}. Is this correct? (Y)/(N)')
    while transaction_confirmed:
        c_or_s = input('Checking or savings: ')
        if c_or_s.lower() == 'checking':
            amount = input(f'How much would you like to {transaction_type} into {c_or_s}: ')
            amount_confirmation = get_user_confirmation(f'${amount} Correct? (Y)/(N)')
            if amount.isdigit():
                if amount_confirmation:
                    amount = float(amount)
                    transaction_handler(c_or_s.lower(), transaction_type, amount, active_user_account)
                    transaction_confirmed = False
                else:
                    print('Please try again....')
            else:
                print('Please try again and enter a valid amount.')
        elif c_or_s.lower() == 'savings':
            amount = input(f'How much would you like to {transaction_type} into {c_or_s}: ')
            amount_confirmation = get_user_confirmation(f'${amount} Correct? (Y)/(N)')
            if amount.isdigit():
                if amount_confirmation:
                    amount = float(amount)
                    transaction_handler(c_or_s.lower(), transaction_type, amount, active_user_account)
                    transaction_confirmed = False
                else:
                    print('Please try again....')
            else:
                print('Please try again and enter a valid amount.')
        else:
            print('Please try again and enter a valid account...')
    else:
        print('Returning to account menu...')


def transaction_vew_balance(active_user_account):
    """
    Displays the current balance for both checking and savings accounts of the active user.

    Args:
        active_user_account (object): An instance of the user's account which holds account details.

    Flow:
        - Fetches the user's account details and pulls the latest checking and savings balances from the database.
        - Displays the account holder's name, checking balance, savings balance, and the total balance.
        - Returns control to the account menu after displaying the balances.
    """
    from interface.menu_handler import menu_header
    from data_handler.database.data_base_handler import DatabaseUnpacker

    puller = DatabaseUnpacker()
    active = active_user_account.get_account_details()

    balance_viewer = puller.pull_from_database(active[USER_ID])

    total = balance_viewer[CHECKING_BALANCE] + balance_viewer[SAVINGS_BALANCE]
    menu_header(balance_viewer[ACCOUNT_HOLDER_NAME])
    print('        ACCOUNT BALANCES')
    print(f"""
    Checking Balance: ${balance_viewer[CHECKING_BALANCE]}
    Savings Balance: ${balance_viewer[SAVINGS_BALANCE]}
    Total balance: ${total}
        """)
    print("    ******************************")
    print('Returning to account menu...')


def transaction_handler(account, transaction_type, amount, active_user_account):
    from data_handler.database.data_base_handler import DatabaseUnpacker
    pusher_puller = DatabaseUnpacker()
    transaction = Transactions()

    active = active_user_account.get_account_details()

    current_data = pusher_puller.pull_from_database(active[USER_ID])

    transaction.transactions = current_data[TRANSACTION_HISTORY]

    transaction.balance[CHECKING_BALANCE] = current_data[CHECKING_BALANCE]
    transaction.balance[SAVINGS_BALANCE] = current_data[SAVINGS_BALANCE]

    transaction.deposit_withdrawal(account, transaction_type, amount)

    current_data[CHECKING_BALANCE] = transaction.balance[CHECKING_BALANCE]
    current_data[SAVINGS_BALANCE] = transaction.balance[SAVINGS_BALANCE]
    current_data[TRANSACTION_HISTORY] = transaction.transactions

    pusher_puller.push_to_database(current_data)
