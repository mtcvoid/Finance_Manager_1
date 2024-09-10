
from Interface.user_interaction import *
from accounts.account_handler import *

def menu_header(header_title):
    print(f"""
       #####Finance Manager#####
    ******************************
             {menu_header}
    ******************************""")


def menu_choices(choices_and_functions):
    for index, (choice, _) in enumerate(choices_and_functions, start=1):
        print(f'({index}) {choice}')

    print("******************************")


def main_menu():
    header = 'Main Menu'
    choices_and_funcs = [('LOG IN', log_in), ('View options', main_menu_options)]
    menu_header(header)
    menu_choices(choices_and_funcs)
    user_choice = get_user_choice(choices_and_funcs)
    print(user_choice)


def main_menu_options():
    menu_header = 'Account Menu'
    main_choices_and_funcs = []
    menu_builder(menu_header, main_choices_and_funcs)


def account_main_menu():
    menu_header = 'Account Menu'
    main_choices_and_funcs = []
    menu_builder(menu_header, main_choices_and_funcs)


def account_options_menu():
    menu_header = 'Account Options '
    main_choices_and_funcs = []
    menu_builder(menu_header, main_choices_and_funcs)


def admin_options_menu():
    menu_header = 'Admin Options'
    main_choices_and_funcs = []
    menu_builder(menu_header, main_choices_and_funcs)


def market_watch_menu():
    menu_header = 'Stock Market Watcher '
    main_choices_and_funcs = []
    menu_builder(menu_header, main_choices_and_funcs)


def bill_tracking_menu():
    menu_header = 'Bill Tracking'
    main_choices_and_funcs = []
    menu_builder(menu_header, main_choices_and_funcs)


main_menu()

