from vehicle_repair_manager import *
from user_commands import *
from mechanic_commands import *


def init():
    print('''
    -----------------------------------------
    Hello! Welcome to Vehicle Repair Manager!
    -----------------------------------------
    ''')

    login('Provide username: ')


def login(msg):
    while True:
        username = input(msg)

        while not username:
            username = input(msg)

        user_id = check_if_user_exists(username)

        if user_id:
            if check_for(user_id, 'client'):
                init_client(username)
                return  # ?
            if check_for(user_id, 'mechanic'):
                init_mechanic(username)
                return
        else:
            answer = input('Would you like to create new user? y/n')
            if answer == 'y':
                create_new_user()
                login(msg)


def create_new_user():
    user_type = input_user_type()
    title = ''
    if user_type == 'mechanic':
        title = get_input('Provide title: ')
    username = get_input('Provide username: ')
    email = get_input('Provide email: ')
    phone = get_input('Provide phone number: ')
    address = get_input('Provide address: ')

    add_user(user_type, username, email, phone, address, title)


def input_user_type():
    user_type = input('Are you a client or mechanic? ')
    while user_type not in ['client', 'mechanic']:
        user_type = input('Are you a client or mechanic? ')

    return user_type


def init_client(username):
    print(f'''
    Hello, {username}!
    You can choose from the following commands:
    ''')
    execute_user_command('help')

    my_command = get_input('Enter command: ')

    while my_command != 'exit':
        execute_user_command(my_command)
        my_command = get_input('Enter command: ')

    print('Thank you for using the Vehicle Repair Manager!\nGoodbye!')


def init_mechanic(username):
    pass


def get_input(msg):
    var = input(msg)

    while not var:
        var = input(msg)

    return var
