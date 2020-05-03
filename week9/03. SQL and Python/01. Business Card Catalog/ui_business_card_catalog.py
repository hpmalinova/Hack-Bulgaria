from business_card_catalog import *


def init():
    print('''
    Hello! This is your business card catalog.
    What would you like?
    (Enter "help" to list all available options)
    ''')

    create_users_table()

    my_command = get_input('Enter command: ', allows_null=False)

    while my_command != 'exit':
        execute_command(my_command)
        my_command = get_input('Enter command: ', allows_null=False)

    print('Thank you for using the Business Card Catalog!\nGoodbye!')


def execute_command(command):
    command_to_function = {'add': my_add, 'list': list_all, 'get': get, 'delete': delete, 'help': my_help}

    if command in command_to_function:
        command_to_function[command]()
    else:
        print('Invalid command. Try again')


def my_add():
    full_name = get_input('Enter user name: ', allows_null=False)
    email = get_input('Enter email: ', allows_null=False)
    age = get_int_input('Enter age: ')
    phone = get_input('Enter phone: ', allows_null=False)
    additional_info = get_input('Enter additional info (optional): ')

    add_business_card(full_name=full_name, email=email, age=age,
                      phone=phone, additional_info=additional_info)


def list_all():
    all_contacts = get_all_business_cards()

    if not all_contacts:
        print('There are no contacts in the DataBase.')
    else:
        print('''
    ##############
    ###Contacts###
    ##############''')
        for i in range(len(all_contacts)):
            print(f'''
    --- {i} ---
    ID: {all_contacts[i][0]}
    Email: {all_contacts[i][2]}
    Name: {all_contacts[i][1]}''')
        print('')


def print_contact(my_id):
    contact = get_contact_by_id(my_id)
    if contact:
        print(f'''
    ##############
    ID: {contact[0]}
    Email: {contact[2]}
    Name: {contact[1]}
    Age: {contact[3]}
    Phone: {contact[4]}
    Additional info: {contact[5]}
    ##############
        ''')
    else:
        print('No such user.')


def get():
    id_to_get = get_int_input('Enter id: ')

    print('Contact info: ')
    print_contact(id_to_get)


def delete():
    id_to_delete = get_int_input('Enter id: ')
    print('Following contact is deleted successfully:')
    print_contact(id_to_delete)
    delete_contact_by_id(id_to_delete)


def my_help():
    print('''
    #############
    ###Options###
    #############

    1. `add` - insert new business card
    2. `list` - list all business cards
    3. `delete` - delete a certain business card (`ID` is required)
    4. `get` - display full information for a certain business card (`ID` is required)
    5. `help` - list all available options
    6. `exit` - exit the program
    ''')


def get_input(msg, allows_null=True):
    var = input(msg)

    while not allows_null and not var:
        var = input(msg)

    return var


def get_int_input(msg):
    while True:
        try:
            var = input(msg)
            int(var)
            return var
        except ValueError:
            print('Input a number!')
            var = input(msg)


if __name__ == '__main__':
    init()
