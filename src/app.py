"""only for temporary use before UI settled done"""

from entities.user import User
from services.user_service import UserService


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

# AI generated code begin


def main():
    service = UserService(FakeUserRepository())
    print("Time Management App CLI")

    while True:
        print("\n1: Register")
        print("2: Login")
        print("3: Current user")
        print("4: Log out")
        print("5: View all users")
        print("0: Exit")

        command = input("> ")

        if command == "1":
            username = input("Username: ")
            password = input("Password: ")
            try:
                service.create_user(username, password)
                print("Registered and logged in.")
            except Exception as e:
                print(f"Error: {e}")

        elif command == "2":
            username = input("Username: ")
            password = input("Password: ")
            try:
                service.login(username, password)
                print("Login successful.")
            except Exception as e:
                print(f"Error: {e}")

        elif command == "3":
            user = service.get_current_user()
            if user:
                print(f"Current user: {user.username}")
            else:
                print("None.")

        elif command == "4":
            service.logout()
            print("Logged out.")

        elif command == "5":
            users = service.get_all_users()
            if not users:
                print("No users registered.")
            else:
                print("Registered users:")
                for user in users:
                    print(f"- {user.username}")

        elif command == "0":
            print("Exiting.")
            break

        else:
            print("Invalid command.")


# AI generated code end

if __name__ == "__main__":
    main()
