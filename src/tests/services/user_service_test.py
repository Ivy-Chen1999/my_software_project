import unittest
from entities.user import User
from services.user_service import (
    UserService, InvalidCredentialsError, UsernameExistsError, InvalidUsernameError)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def create(self, user):
        self.users.append(user)
        return user

    def delete_all(self):
        self.users = []


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService(FakeUserRepository())
        self.user = User("Ivy", "cyx123456")

    def test_create_user(self):
        user = self.service.create_user("banana", "0")
        self.assertEqual(user.username, "banana")

    def test_create_invalid_user(self):
        self.assertRaises(
            InvalidUsernameError,
            lambda: self.service.create_user("", "0")
        )
        self.assertRaises(
            InvalidUsernameError,
            lambda: self.service.create_user("a" * 21, "0")
        )

    def test_create_existing_user(self):
        self.service.create_user("same", "0")
        self.assertRaises(
            UsernameExistsError,
            lambda: self.service.create_user("same", "1")
        )

    def test_create_user_auto_login(self):
        self.service.create_user("auto", "1", auto_login=True)
        self.assertEqual(self.service.get_current_user().username, "auto")

    def test_login_success(self):
        self.service.create_user("peach", "111")
        user = self.service.login("peach", "111")
        self.assertEqual(user.username, "peach")

    def test_login_invalid_password(self):
        self.service.create_user("wrongpass", "1")
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.service.login("wrongpass", "2")
        )

    def test_login_nonexistent(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.service.login("none", "0")
        )

    def test_logout(self):
        self.service.create_user("apple", "111")
        self.service.login("apple", "111")
        self.service.logout()
        self.assertIsNone(self.service.get_current_user())

    def test_get_current_user(self):
        self.service.create_user("grape", "0")
        self.service.login("grape", "0")
        self.assertEqual(self.service.get_current_user().username, "grape")

    def test_get_all_users(self):
        self.service.create_user("melon1", "0")
        self.service.create_user("melon2", "0")
        self.service.create_user("melon3", "0")
        self.service.create_user("melon4", "0")

        users = self.service.get_all_users()
        usernames = []
        for user in users:
            usernames.append(user.username)
        self.assertEqual(usernames, ["melon1", "melon2", "melon3", "melon4"])


if __name__ == "__main__":
    unittest.main()
