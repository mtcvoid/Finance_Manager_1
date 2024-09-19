from interface.menu_handler import *
from data_handler.database.data_base_handler import DatabaseUnpacker
if __name__ == "__main__":
    # Ensure the database table is created when the application starts
    db_unpacker = DatabaseUnpacker()

    # Now call your main menu or other application logic
    main_menu()
