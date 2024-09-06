"""
All functions for Interface building
"""


def menu_builder(menu_header: str, choices_and_funcs):
    """
    Displays an Interface and calls the appropriate function based on the user's choice.
    """
    while True:
        print(f"""
   #####Finance Manager#####
******************************
         {menu_header}
******************************""")
        for index, (choice, _) in enumerate(choices_and_funcs, start=1):
            print(f'({index}) {choice}')

        print("******************************")

        u_c = input('Choice: ')

        if u_c.isdigit():
            u_c = int(u_c)
            if 1 <= u_c <= choices_and_funcs:
                choice, func = choices_and_funcs[u_c, -1]
                if func:  # only call the function if it's not none. Will get you out of loop
                    func()
                else:
                    print('Exiting...')
                    break
            else:
                print('Invalid choice. Please select a valid option.')
        else:
            print('Invalid input. Please enter a number corresponding to a choice.')
