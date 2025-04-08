"""only for temporary use before UI settled done"""

from services.user_service import UserService
from services.task_service import task_service
from repositories.user_repository import user_repository
# from entities.task import Task


# AI generated code begin
def main():

    service = UserService(user_repository)
    print("Time Management App CLI")

    while True:
        print("\n=== MENU ===")
        print("1: Register")
        print("2: Login")
        print("3: Current user")
        print("4: Log out")
        print("5: View all users")
        print("6: View my tasks")
        print("7: Add a new task")
        print("8: Mark a task as done")
        print("9: Delete a task")
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

        elif command == "6":
            user = service.get_current_user()
            if not user:
                print("Please log in first.")
                continue

            tasks = task_service.get_tasks_by_user(user.id)
            if not tasks:
                print("You have no tasks.")
            else:
                print("Your tasks:")
                for t in tasks:
                    status = "done" if t.done else "undone"
                    print(
                        f"- [{status}] {t.id} | {t.content} (Category: {t.category})")

        elif command == "7":
            user = service.get_current_user()
            if not user:
                print("Please log in first.")
                continue

            content = input("Task content: ")
            category = input(
                "Category (optional, default: general): ") or "general"
            task_service.add_task(content, user.id, category)
            print("Task added.")

        elif command == "8":
            user = service.get_current_user()
            if not user:
                print("Please log in first.")
                continue

            task_id = input("Task ID to mark as done: ")
            task_service.mark_done(task_id)
            print("Task marked as done.")

        elif command == "9":
            user = service.get_current_user()
            if not user:
                print("Please log in first.")
                continue

            task_id = input("Task ID to delete: ")
            task_service.delete_task(task_id)
            print("Task deleted.")

        elif command == "0":
            print("Exiting.")
            break

        elif command == "99":
            user_repository.delete_all()
            task_service.clear_all_tasks()
            print("all removed")

        else:
            print("Invalid command.")


# AI generated code end
if __name__ == "__main__":
    main()
