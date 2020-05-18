import sqlite3


def create_all_tables():
    create_base_user_table()
    create_client_table()
    create_mechanic_table()
    create_service_table()
    create_mechanic_service_table()
    create_vehicle_table()
    create_repair_hour_table()


def create_base_user_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS baseUser (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(30) UNIQUE NOT NULL,
        email VARCHAR(30) UNIQUE NOT NULL,
        phone_number INTEGER NOT NULL,
        address VARCHAR(30)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_client_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS client (
        #base_id INTEGER AUTOINCREMENT NOT NULL,
        base_id INTEGER, # NOT NULL ?
        FOREIGN KEY(base_id) REFERENCES baseUser(id)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_mechanic_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS mechanic (
        #base_id INTEGER AUTOINCREMENT NOT NULL,
        base_id INTEGER # NOT NULL
        title VARCHAR(20) NOT NULL,
        FOREIGN KEY(base_id) REFERENCES baseUser(id)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_service_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS service (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) UNIQUE, NOT NULL
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_mechanic_service_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS mechanicService (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mechanic_id INTEGER, #NOT NULL?
        service_id INTEGER,
        #mechanic_id INTEGER AUTOINCREMENT,
        #service_id INTEGER AUTOINCREMENT,
        FOREIGN KEY(mechanic_id) REFERENCES mechanic(base_id)
        FOREIGN KEY(service_id) REFERENCES service(id)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_vehicle_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS vehicle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category VARCHAR(10),
        make VARCHAR(10),
        model VARCHAR(10),
        register_number VARCHAR(10) NOT NULL,
        gear_box VARCHAR(10)
        owner_id INTEGER # NOT NULL
        FOREIGN KEY(owner_id) REFERENCES baseUser(id)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_repair_hour_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS repairHour (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date VARCHAR(10) NOT NULL,
        start_hour VARCHAR(5) NOT NULL,
        vehicle_id INTEGER,
        bill REAL CHECK (bill > 0)
        mechanic_service INTEGER # NOT NULL
        FOREIGN KEY(vehicle_id) REFERENCES vehicle(id)
        FOREIGN KEY(mechanic_service) REFERENCES mechanicService(id)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def main():
    create_all_tables()


if __name__ == '__main__':
    main()
