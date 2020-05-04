CREATE TABLE IF NOT EXISTS baseUser(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    phone_number INTEGER NOT NULL,
    address VARCHAR(30) NOT NULL
    );

CREATE TABLE IF NOT EXISTS client(
    base_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY(base_id) REFERENCES baseUser(id)
);

CREATE TABLE IF NOT EXISTS mechanic(
    base_id INTEGER UNIQUE NOT NULL,
    title VARCHAR(20) NOT NULL,
    FOREIGN KEY(base_id) REFERENCES baseUser(id)
);

CREATE TABLE IF NOT EXISTS service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS mechanicService (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mechanic_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY(mechanic_id) REFERENCES mechanic(base_id),
    FOREIGN KEY(service_id) REFERENCES service(id)
);

CREATE TABLE IF NOT EXISTS vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category VARCHAR(10),
    make VARCHAR(10),
    model VARCHAR(10),
    register_number VARCHAR(10) NOT NULL,
    gear_box VARCHAR(10),
    owner_id INTEGER,
    FOREIGN KEY(owner_id) REFERENCES baseUser(id)
);

CREATE TABLE IF NOT EXISTS repairHour (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date VARCHAR(10) NOT NULL,
    start_hour VARCHAR(5) NOT NULL,
    vehicle_id INTEGER,
    bill REAL CHECK(bill > 0),
    mechanic_service INTEGER,
    FOREIGN KEY(vehicle_id) REFERENCES vehicle(id),
    FOREIGN KEY(mechanic_service) REFERENCES mechanicService(id)
);
