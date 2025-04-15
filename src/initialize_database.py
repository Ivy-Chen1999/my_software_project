from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS tasks;")
    cursor.execute("DROP TABLE IF EXISTS pomodoros;")
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE tasks (
            id TEXT PRIMARY KEY,
            user_id TEXT,
            content TEXT NOT NULL,
            done INTEGER DEFAULT 0,
            created_at TIMESTAMP,
            category TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    """)

    cursor.execute("""
        CREATE TABLE pomodoros (
            id TEXT PRIMARY KEY,
            task_id TEXT,
            start_time TEXT,
            end_time TEXT,
            duration INTEGER
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
