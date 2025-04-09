"""only for temporary use before UI settled done"""
from services.user_service import user_service
from services.task_service import task_service
from repositories.user_repository import user_repository

#AI generated code begin

def handle_register():
    username = input("Username: ")
    password = input("Password: ")
    try:
        user_service.create_user(username, password)
        print("Registered and logged in.")
    except Exception as e:
        print(f"Error: {e}")


def handle_login():
    username = input("Username: ")
    password = input("Password: ")
    try:
        user_service.login(username, password)
        print("Login successful.")
    except Exception as e:
        print(f"Error: {e}")


def handle_current_user():
    user = user_service.get_current_user()
    if user:
        print(f"Current user: {user.username}")
    else:
        print("No user currently logged in.")


def handle_logout():
    user_service.logout()
    print("Logged out.")


def handle_view_all_users():
    users = user_service.get_all_users()
    if not users:
        print("No users registered.")
    else:
        print("Registered users:")
        for user in users:
            print(f"- {user.username}")


def handle_view_tasks():
    user = user_service.get_current_user()
    if not user:
        print("Please log in first.")
        return

    tasks = task_service.get_tasks_by_user(user.id)
    if not tasks:
        print("You have no tasks.")
    else:
        print("Your tasks:")
        for t in tasks:
            status = "done" if t.done else "undone"
            print(f"- [{status}] {t.id} | {t.content} (Category: {t.category})")


def handle_add_task():
    user = user_service.get_current_user()
    if not user:
        print("Please log in first.")
        return

    content = input("Task content: ")
    category = input("Category (optional, default: general): ") or "general"
    task_service.add_task(content, user.id, category)
    print("Task added.")


def handle_mark_done():
    user = user_service.get_current_user()
    if not user:
        print("Please log in first.")
        return

    task_id = input("Task ID to mark as done: ")
    task_service.mark_done(task_id)
    print("Task marked as done.")


def handle_delete_task():
    user = user_service.get_current_user()
    if not user:
        print("Please log in first.")
        return

    task_id = input("Task ID to delete: ")
    task_service.delete_task(task_id)
    print("Task deleted.")


def handle_reset_all():
    user_service.logout()
    user_repository.delete_all()
    task_service.clear_all_tasks()
    print("All data cleared and logged out.")


def main():
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
        print("99: Reset all (dev only)")
        print("0: Exit")

        command = input("> ")

        if command == "1":
            handle_register()
        elif command == "2":
            handle_login()
        elif command == "3":
            handle_current_user()
        elif command == "4":
            handle_logout()
        elif command == "5":
            handle_view_all_users()
        elif command == "6":
            handle_view_tasks()
        elif command == "7":
            handle_add_task()
        elif command == "8":
            handle_mark_done()
        elif command == "9":
            handle_delete_task()
        elif command == "99":
            handle_reset_all()
        elif command == "0":
            print("Exiting.")
            break

#AI generated code end
if __name__ == "__main__":
    main()
