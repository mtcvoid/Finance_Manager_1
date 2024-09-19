"""
handles user interaction for bill tracker
"""
from interface.user_interface_general import *
from mods.bill_tracker.bill_tracking_handler import BillHandler



def user_add_bill(active_user_account):
    print("""
    You will need the following information: 
    - Name of bill
    - Bill total
    - Date the bill is due (YYY-DD-
    """)
   
    confirmation = get_user_confirmation("Would you like to add a bill")
    if confirmation:
        bill_handler = BillHandler()
       # name =
        #total =
        #date =

        #confirm


        #handly
        #bill_handler.add_bill(name,total,date)

        #add another bill?
            #loop back

        #no add
         #active user menu


    else:
        pass  # need to add an account menu.




def user_remove_bill():
    pass


def user_view_all_bills():
    bill = BillHandler()
    bill.add_bill('Comcast', 150.35, "2024-10-05")

    for item in bill.bills:
        for key, value in item.items():
            print(key, value)

