"""
handles user interaction for transactions
"""
from account_objects.accounting.transactions import Transactions
from interface.user_interface_general import get_user_confirmation
from data_handler.database.data_base_handler import DatabaseUnpacker


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
                    transaction_handler(transaction_type, c_or_s.lower(), amount)
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


def transaction_vew_balance(active_user):
    from interface.menu_handler import menu_header
    active = active_user.__repr__()
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


def transaction_handler(account,transaction_type, amount):
    transaction = Transactions()
    data_push = DatabaseUnpacker()
    if transaction_type == 'Deposit':
        transaction.deposit_withdrawal(account: str, transaction_type: str, amount: float = 0)
    if transaction_type == 'Withdrawal':
        pass

    data_push.push_to_database()

