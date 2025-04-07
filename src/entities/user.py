import uuid


class User:
    def __init__(self, username, password, user_id=None):
        """
            Suppose there are multiple users
            might be change in the future

        """

        self.id = user_id or str(uuid.uuid4())
        self.username = username
        self.password = password
