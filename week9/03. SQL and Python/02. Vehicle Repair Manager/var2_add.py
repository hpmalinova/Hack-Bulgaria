import sqlite3


def add_data():
    connection = sqlite3.connect('vehicle_management.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    # ADD baseUsers
    data = []

    for i in range(6):
        data.append(
            f'("user_name_{i}", "email_{i}", "{1000000000 + i*81646}", "address_{i}")'
        )

    query = f'''
        INSERT INTO baseUser (user_name, email, phone_number, address)
          VALUES {','.join(data)};
    '''
    cursor.execute(query)

    # ADD clients
    data = []

    for i in range(1, 4):
        data.append(
            f'("{i}")'
        )

    query = f'''
        INSERT INTO client (base_id)
          VALUES {','.join(data)};
    '''
    cursor.execute(query)

    # ADD mechanics
    data = []

    for i in range(4, 7):
        data.append(
            f'("{i}", "mechanic_{i}")'
        )

    query = f'''
        INSERT INTO mechanic (base_id)
          VALUES {','.join(data)};
    '''
    cursor.execute(query)

    connection.commit()
    connection.close()



def main():
    add_data()


if __name__ == '__main__':
    main()
