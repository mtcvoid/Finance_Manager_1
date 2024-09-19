
Finance Manager Application

Overview
--------

The Finance Manager application is a terminal-based financial account management tool that allows users to interact with various account-related functionalities, including account creation, modification, and data management. The application presents a simple menu-driven interface, enabling users to navigate and perform financial tasks intuitively.

Features
--------

- Account Management:
  - Create new accounts.
  - Select and modify existing accounts.
- Menu-Driven Interface:
  - Provides an easy-to-use menu system for navigating different options.
- Modular Design:
  - The application is organized into different modules, each responsible for specific aspects of the program, making it easily extendable and maintainable.

Project Structure
-----------------

Finance_Manager_1-master/
├── account_objects/           # Handles financial account-related objects and classes
├── data_handler/              # Manages data storage, retrieval, and modification
├── interface/                 # Contains user interface and menu handling
│   ├── menu_handler.py        # Builds and manages menus for user interaction
│   └── user_interaction.py    # Handles input/output with users
├── main/                      # Core application logic
│   └── app.py                 # Entry point for the application
├── mods/                      # Contains any additional modifications or enhancements
├── testing/                   # Unit tests for the various modules
└── README.md                  # Project description and instructions

How It Works
------------

The application is based on a menu-driven system where users are presented with different options based on the available actions. These menus are built using Python and organized in the interface module, specifically within the menu_handler.py file.

Main Components
---------------

- app.py (Main entry point): The app.py file starts the application by invoking the main_menu() function from menu_handler.py. This initializes the first user interaction.

- menu_handler.py: This file is responsible for displaying menus, handling user selections, and calling the corresponding functions for each menu option. It uses a dictionary structure (MENU_LIST) to map options to specific functions like "Create Account" or "Choose Account."

- Account Management: The actual account management functionality is modularized in the account_objects/ folder, which handles the creation, modification, and retrieval of account data.

Example Flow
------------

1. Main Menu: The program first displays the main menu with options like "Create Account" or "Choose Account."
2. User Input: Based on the user's choice, the program executes the corresponding function. For example, selecting "Create Account" leads to the account creation process.
3. Submenus: Depending on the action, the program may present further submenus to refine the user's choice or collect additional information.

Dependencies
------------

This application uses only Python's standard libraries, making it lightweight and easy to run. However, it is important to ensure that Python 3.x is installed on your machine.

Installation
------------

To get started with the Finance Manager application, follow these steps:

1. Clone this repository or download the zip file.
2. Ensure that you have Python 3.x installed.
3. Navigate to the project directory.
4. Run the application:
   python3 main/app.py

Testing
-------

The testing/ folder contains unit tests for various components of the application. To run the tests, use the following command:

python3 -m unittest discover -s testing

Future Improvements
-------------------

- Add more financial functionalities such as transaction tracking and report generation.
- Implement data encryption for enhanced security.
- Expand the account options with more detailed financial information.


