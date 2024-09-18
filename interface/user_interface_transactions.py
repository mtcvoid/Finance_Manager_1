"""
handles user interaction for transactions
"""
from account_objects.accounting.transactions import Transactions
from interface.user_interface_general import get_user_confirmation
from data_handler.database.data_base_handler import DatabaseUnpacker
import json


def transaction_interaction(transaction_type, active_user_account):
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
                else:
                    print('Please try again....')
            else:
                print('Please try again and enter a valid amount.')
        elif c_or_s.lower() == 'savings':
            amount = input(f'How much would you like to {transaction_type} into {c_or_s}: ')
            amount_confirmation = get_user_confirmation(f'${amount} Correct? (Y)/(N)')
            if amount.isdigit():
                if amount_confirmation:
                    transaction_handler(c_or_s, transaction_type, amount)
        else:
            print('Please try again and enter a valid account...')
    else:
        print('Returning to account menu...')


def transaction_vew_balance(active_user_account):
    from interface.menu_handler import menu_header
    active = active_user_account.__repr__()
    total = active['checking_balance'] + active['savings_balance']
    menu_header(active['Account_Holder_Name'])
    print('        ACCOUNT BALANCES')
    print(f"""
    Checking Balance: ${active['checking_balance']}
    Savings Balance: ${active['savings_balance']}
    Total balance: ${total}
        """)
    print("    ******************************")
    print('Returning to account menu...')


def transaction_handler(account, transaction_type, amount, active_user_account):
    pusher = DatabaseUnpacker
    transaction = Transactions()
    active = active_user_account.get_account_details()

    transaction.transactions = json.loads(active['Transaction_History'])

    transaction.balance['Checking_balance'] = active['Checking_Balance']
    transaction.balance['Savings_balance'] = active['Savings_Balance']

    transaction.deposit_withdrawal(account, transaction_type, amount)

    test = transaction.transactions
    print(test)
