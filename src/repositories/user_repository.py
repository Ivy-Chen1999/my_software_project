from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(user_id=row["id"], username=row["username"], password=row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (id, username, password) VALUES (?, ?, ?)",
            (user.id, user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return get_user_by_row(row)

    def delete_all(self):
        self._connection.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
