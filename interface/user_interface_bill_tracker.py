"""
handles user interaction for bill tracker
"""
from interface.user_interface_general import *


def user_add_bill(active_user_account):
    print("""
    You will need the following information: 
    - Name of bill
    - Bill total
    - Date the bill is due
    """)
    confirmation = get_user_confirmation("Would you like to add a bill")
    if confirmation:
        pass
    else:
        pass  # need to add an account menu.

    '''
    
    So you will need to figure out the logic behind holding an account in place once you have chosen said account. 
    if you return to main menu you can log out maybe? set up a log in and log out method maybe?
    
    - if you set up a log in method then once the user has logged in they it can set that account to 'Active' and then 
    that account is what gets pulled for all of the menu options? think about this before you go and do market watch 
    stuff. 
    
    
    
    def menu_maker(menu_key):          
  
        'Chosen-Account Menu'
    '''


def user_remove_bill():
    pass


def user_view_all_bills():
    pass
