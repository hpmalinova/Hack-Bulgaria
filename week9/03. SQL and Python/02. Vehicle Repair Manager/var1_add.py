import sqlite3


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
    users_data = []
    for i in range(1, 4):
        users_data.append(
            f'("{i}")'
        )

    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    query = f'''
        INSERT INTO client (base_id)
          VALUES {','.join(users_data)}
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


def main():
    add_baseUsers()
    add_clients()


if __name__ == '__main__':
    main()
