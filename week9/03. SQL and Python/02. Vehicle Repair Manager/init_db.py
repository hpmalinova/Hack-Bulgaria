import sqlite3


def create_tables(script_name):
    with open(script_name, 'r') as sql_file:
        sql_script = sql_file.read()

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    cursor.executescript(sql_script)

    connection.commit()
    connection.close()


def add_data():
    add_baseUsers()
    add_clients()
    add_mechanics()
    add_services()


def add_baseUsers():
    users_data = []
    for i in range(6):
        users_data.append(
            f'("user_name_{i}", "email_{i}", "{1000000000 + i*81646}", "address_{i}")'
        )

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = f'''
        INSERT INTO baseUser (user_name, email, phone_number, address)
          VALUES {','.join(users_data)}
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


def add_clients():
    client_data = []
    for i in range(1, 4):
        client_data.append(
            f'("{i}")'
        )

    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    query = f'''
        INSERT INTO client (base_id)
          VALUES {','.join(client_data)}
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


def add_mechanics():
    mechanic_data = []
    for i in range(4, 7):
        mechanic_data.append(
            f'("{i}", "mechanic_{i}")'
        )

    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    query = f'''
        INSERT INTO mechanic (base_id, title)
          VALUES {','.join(mechanic_data)}
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


def add_services():
    service_data = []
    for service in ['Oil change', 'Tire change', 'Engine repair', 'Inspection', 'Alternator replacement']:
        service_data.append(
            f'({service})'
        )

    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    query = f'''
        INSERT INTO service (name)
          VALUES {','.join(service_data)}
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_tables("create_tables.sql")
    add_data()
