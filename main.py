from customio import custom_output as co
from customio import custom_input as ci
from filehandler import file_handler as fh

def retrieve_passwords_using_pagination():
    page = 0
    rows = 10
    while True:
        passwords = fh.read_active_passwords(page, rows) # for firt version lets print platform and password
        co.print_list(passwords)
        co.print_paginated_options()
        pagination_move = ci.read_user_input()
        if pagination_move == "n":
            page+=1 #we need to know when to stop letting the user add more pages
        elif pagination_move == "b":
            page-=1
            if page<0:
                page=0
        elif pagination_move == "q":
            break
        else:
            co.print_invalid_option_error()

def retrieve_passwords_using_name_match():
    while True:
        co.print_retrieve_password_by_match_options()
        word = ci.read_user_input()
        if word == " ":
            break
        passwords = fh.read_active_passwords_word_matched(word)
        co.print_list(passwords)

def retrieve_password():
    # consider a while loop if after a bad option provided we want to stay in this menu
    co.print_retrieve_password_options()
    option = ci.read_user_input()
    if option == "1": #pagination
        retrieve_passwords_using_pagination()
    elif option == "2": #word match
        retrieve_passwords_using_name_match()
    else:
        co.print_invalid_option_error()

def start_listening_commands():
    while True:
        co.print_initial_command_options()
        value = ci.read_user_input()
        if value == "5":
            break
        elif value == "1":
            retrieve_password()
        elif value == "2":
            print("dos")
        elif value == "3":
            print("tres")
        elif value == "4":
            print("cuatro")
        else:
            co.print_invalid_option_error()

def main():
    co.print_welcome()
    start_listening_commands()
    co.print_farewell()

if __name__ == "__main__":
    main()
