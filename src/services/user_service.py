from repositories.user_repository import user_repository
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class InvalidUsernameError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UserService:
    def __init__(self, user_repo):
        self._user_repo = user_repo
        self._current_user = None

    def create_user(self, username, password, auto_login=True):
        if len(username) > 20 or len(username) < 1:
            raise InvalidUsernameError(
                "Username is too long or too short (1-20 characters)")

        if self._user_repo.find_by_username(username):
            raise UsernameExistsError("Username already exists")

        user = self._user_repo.create(
            User(username=username, password=password))

        if auto_login:
            self._current_user = user

        return user

    def login(self, username, password):
        user = self._user_repo.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._current_user = user
        return user

    def logout(self):
        self._current_user = None

    def get_current_user(self):
        if self._current_user:
            real_user = self._user_repo.find_by_username(
                self._current_user.username)
            if real_user is None:
                self._current_user = None
        return self._current_user

    def get_all_users(self):
        return self._user_repo.find_all()


user_service = UserService(user_repository)
