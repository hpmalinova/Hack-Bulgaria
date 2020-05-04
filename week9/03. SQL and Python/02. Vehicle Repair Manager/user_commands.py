def execute_user_command(command):
    command_to_function = {'help': my_help}

    command = command.split(' ')

    if command[0] in command_to_function:
        if len(command) == 1:
            command_to_function[command[0]]()
        elif len(command) == 2:
            command_to_function[command[0]](command[1])
        else:
            print('Invalid number of arguments')
    else:
        print('Invalid command. Try again')


def my_help():
    print('''
    ----------------------------
    list_all_free_hours
    list_free_hours <date>
    save_repair_hour <hour_id>
    update_repair_hour <hour_id>
    delete_repair_hour <hour_id>
    add_vehicle
    update_vehicle <vehicle_id>
    delete_vehicle <vehicle_id>
    help --> see all commands
    exit --> exit the app
    ----------------------------
    ''')


def list_all_free_hours():
    pass


def list_free_hours(date):
    pass