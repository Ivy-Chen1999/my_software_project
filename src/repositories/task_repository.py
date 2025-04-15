from entities.task import Task
from database_connection import get_database_connection


class TaskRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def create(self, task: Task):
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO tasks (id, user_id, content, done, created_at, category)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (task.id, task.user_id, task.content, int(task.done), task.created_at, task.category))
        self._connection.commit()
        return task

    def find_all(self):
        cursor = self._connection.cursor()
        result = cursor.execute("SELECT * FROM tasks").fetchall()
        return [self._row_to_task(row) for row in result]

    def find_by_user_id(self, user_id):
        cursor = self._connection.cursor()
        result = cursor.execute(
            "SELECT * FROM tasks WHERE user_id = ?", (user_id,)).fetchall()
        return [self._row_to_task(row) for row in result]

    def set_done(self, task_id, done=True):
        cursor = self._connection.cursor()
        cursor.execute("UPDATE tasks SET done = ? WHERE id = ?",
                       (int(done), task_id))
        self._connection.commit()

    def delete(self, task_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM tasks")
        self._connection.commit()

# AI generated code begin
    def _row_to_task(self, row):
        return Task(
            id=row["id"],
            content=row["content"],
            done=bool(row["done"]),
            user_id=row["user_id"],
            category=row["category"],
            created_at=row["created_at"]
        )

# AI generated code ends


task_repository = TaskRepository()
