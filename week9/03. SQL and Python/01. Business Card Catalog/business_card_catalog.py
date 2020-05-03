import sqlite3


def create_users_table():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    create_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(30) UNIQUE NOT NULL,
        age INTEGER NOT NULL CHECK(age BETWEEN 18 and 120),
        phone VARCHAR(10) NOT NULL CHECK (length(phone) >= 10),
        additional_info TEXT
    );
    '''
    cursor.execute(create_table)
    connection.commit()
    connection.close()


def add_business_card(*, full_name, email, age, phone, additional_info):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    insert_query = '''
        INSERT INTO users (full_name, email, age, phone, additional_info)
            VALUES (?, ?, ?, ?, ?);
    '''
    try:
        cursor.execute(insert_query, (full_name, email, int(age), phone, additional_info))
    except sqlite3.IntegrityError:
        print('Invalid data. User was not added. Please, try again!')

    connection.commit()
    connection.close()


def get_all_business_cards():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    select_query = 'SELECT id, email, full_name FROM users;'
    cursor.execute(select_query)
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result


def get_contact_by_id(id_to_get):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    select_query = f'SELECT * FROM users WHERE id={id_to_get};'
    cursor.execute(select_query)
    result = cursor.fetchone()

    connection.commit()
    connection.close()

    return result


def delete_contact_by_id(id_to_delete):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    delete_query = f'''
    DELETE FROM users
        WHERE id = {id_to_delete};
    '''
    cursor.execute(delete_query)

    connection.commit()
    connection.close()
