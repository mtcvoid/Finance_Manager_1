"""
handles user interaction for budget
"""
from interface.user_interface_general import input_with_validation, get_user_confirmation

def user_add_remove_expense():
    print('''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Expenses are categorized under certain categories to better
    help you  understand where you are spending your money. 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Essential Expenses:
                -Housing        -Utilities
                -Groceries      -Transportation
                -Insurance      -Healthcare
                -Debt Payments (Mortgages, Credit Cards, etc...)

    Non-Essential Expenses:
                -Dining Out     -Entertainment
                -Personal Care  -Clothing
                -Education      -Hobbies and Leisure
                -Gifts          -Travel/Vacations

    Savings and Investments:
                -Emergency Fund
                -Retirement Savings
                -Investments
                -Education Savings
                -Major Purchases (Home, Vehicle, etc....)''')


    run_expenses = get_user_confirmation('Would you like to add an expense? (Y)/(N)')

    if run_expenses:
        pass
    else:
        pass # go back to budget menu



    pass