import sqlite3


# returns ID if user exists
# returns False if user doesn't exist
def check_if_user_exists(username):
    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    select_query = f'SELECT id FROM baseUser WHERE user_name={username};'
    cursor.execute(select_query)
    result = cursor.fetchone()

    connection.commit()
    connection.close()

    return result if result else False


def check_for(id, table_name):
    if table_name not in ['client', 'mechanic']:
        print(f'{table_name} is not a valid user type')
        return False
    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    select_query = f'SELECT base_id FROM {table_name} WHERE base_id={id};'

    cursor.execute(select_query)
    result = cursor.fetchone()

    connection.commit()
    connection.close()

    return result if result else False

# ADD user
def add_user(user_type, username, email, phone, address, title):
    add_user_to_baseUser(username, email, phone, address)
    new_user_id = check_if_user_exists(username)
    if title:
        add_mechanic(new_user_id, title)
    else:
        add_client(new_user_id)


def add_user_to_baseUser(username, email, phone, address):
    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    insert_query = '''
        INSERT INTO baseUser (user_name, email, phone_number, address)
            VALUES (?, ?, ?, ?);
    '''
    try:
        cursor.execute(insert_query, (username, email, int(phone), address))
    except sqlite3.IntegrityError:
        print('Invalid data. User was not added. Please, try again!')

    connection.commit()
    connection.close()


def add_client(user_id):
    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    insert_query = '''
        INSERT INTO client (base_id)
            VALUES (?);
    '''
    try:
        cursor.execute(insert_query, (user_id))
    except sqlite3.IntegrityError:
        print('Invalid data. User was not added. Please, try again!')

    connection.commit()
    connection.close()


def add_mechanic(user_id, title):
    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    insert_query = '''
        INSERT INTO mechanic (base_id, title)
            VALUES (?, ?);
    '''
    try:
        cursor.execute(insert_query, (user_id, title))
    except sqlite3.IntegrityError:
        print('Invalid data. User was not added. Please, try again!')

    connection.commit()
    connection.close()




# def check_if_client(id):
#     connection = sqlite3.connect('users.db')
#     connection.execute("PRAGMA foreign_keys = 1")
#     cursor = connection.cursor()

#     select_query = f'SELECT base_id FROM client WHERE base_id={id};'
#     cursor.execute(select_query)
#     result = cursor.fetchone()

#     connection.commit()
#     connection.close()

#     return result if result else False

# def check_if_mechanic(id):
#     connection = sqlite3.connect('users.db')
#     connection.execute("PRAGMA foreign_keys = 1")
#     cursor = connection.cursor()

#     select_query = f'SELECT base_id FROM mechanic WHERE base_id={id};'
#     cursor.execute(select_query)
#     result = cursor.fetchone()

#     connection.commit()
#     connection.close()

#     return result if result else False