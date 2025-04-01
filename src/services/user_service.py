from entities.user import User
# from repositories.user_repository import user_repository
from repositories.user_repository import UserRepository

class InvalidCredentialsError(Exception):
    pass

class InvalidUsernameError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class UserService:
    def __init__(self, user_repository):
        self._repo = user_repository
        self._current_user = None

    def create_user(self, username, password, auto_login=True):
        if len(username) > 20 or len(username) < 1:
            raise InvalidUsernameError("Username is too long or too short(within 1-20 characters)")
        if self._repo.find_by_username(username):
            raise UsernameExistsError("Username already exists")

        user = self._repo.create(User(username=username, password=password))
        if auto_login:
            self._current_user = user

        return user

    def login(self, username, password):
        user = self._repo.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._current_user = user
        return user

    def logout(self):
        self._current_user = None

    def get_current_user(self):
        return self._current_user

    def get_all_users(self):
        return self._repo.find_all()


