from Interface.user_interaction import *



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
    choices_and_funcs = [('View options', main_menu_options)]
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def main_menu_options():
    header = ''
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def account_main_menu():
    header = ''
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def account_options_menu():
    header = ''
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def admin_options_menu():
    header = ''
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def market_watch_menu():
    header = ''
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def bill_tracking_menu():
    header = ''
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)



