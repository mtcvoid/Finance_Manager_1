from Interface.menu_builder import *
from accounts.account_handler import *


def main_menu():
    menu_header = 'Main Menu'
    main_choices_and_funcs = [('LOG IN', log_in()), ('View options', main_menu_options())]
    menu_builder(menu_header, main_choices_and_funcs)


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
