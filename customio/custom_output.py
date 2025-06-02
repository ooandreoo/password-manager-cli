def print_welcome():
    print("\033c", end="")
    print("------------------------")
    print("# Password Manager CLI #")
    print("------------------------")
    print("")

def print_initial_command_options():
    print("What would you like to do?")
    print("(1) Retrieve password")
    print("(2) Update a password")
    print("(3) Register a new password")
    print("(4) Delete a password")
    print("(5) Exit")
    print("")

def print_farewell():
    print("")
    print("Thanks for using Password Manager CLI")
    print("See you soon! :)")
    print("")


def print_user_input(text):
    print("")
    print("You wrote: "+text)
    print("")

def print_invalid_option_error():
    print("")
    print("Invalid option. Please try again with a valid option.")
    print("")

def print_list(data):
    print("")
    for element in data:
        print(element)
    print("")

def print_retrieve_password_options():
    print("")
    print("How would you like to search for your password?")
    print("(1) List all passwords")
    print("(2) Name of platform")
    print("")

def print_paginated_options():
    print("")
    print("Options: (n)ext      (b)efore        (q)uit")
    print("")


def print_retrieve_password_by_match_options():
    print("")
    print("Write platform name or similar: (Type just spacebar if you want to quit)")
    print("")
