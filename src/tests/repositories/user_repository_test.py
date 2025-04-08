import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_melon = User('melon', '123')
        self.user_grape = User('grape', '456')

    def test_create(self):
        user_repository.create(self.user_melon)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_melon.username)

    def test_find_all(self):
        user_repository.create(self.user_melon)
        user_repository.create(self.user_grape)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_melon.username)
        self.assertEqual(users[1].username, self.user_grape.username)

    def test_find_by_username(self):
        user_repository.create(self.user_melon)
        user = user_repository.find_by_username(self.user_melon.username)

        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.user_melon.username)

    def test_delete_all(self):
        user_repository.create(self.user_melon)
        user_repository.create(self.user_grape)

        user_repository.delete_all()
        users = user_repository.find_all()
        self.assertEqual(len(users), 0)


if __name__ == "__main__":
    unittest.main()
