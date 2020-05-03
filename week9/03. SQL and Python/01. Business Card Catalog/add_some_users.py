import sqlite3


def create_users_table():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(30) UNIQUE NOT NULL,
        age INTEGER NOT NULL CHECK(age BETWEEN 18 and 120),
        phone VARCHAR(10) NOT NULL CHECK (length(phone) >= 10),
        additional_info TEXT
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def populate_users_table():
    users_data = []

    for i in range(20):
        users_data.append(
            f'("name_{i}", "email_{i}", "{i + 18}", "phone_{i + 1000}", "{i}")'
        )

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    query = f'''
        INSERT INTO users (full_name, email, age, phone, additional_info)
          VALUES {','.join(users_data)}
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def main():
    create_users_table()
    populate_users_table()


if __name__ == '__main__':
    main()