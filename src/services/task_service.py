from entities.task import Task
from repositories.task_repository import task_repository


class TaskService:
    def __init__(self):
        self._task_repo = task_repository

    def add_task(self, content, user_id, category="general"):
        task = Task(content=content, user_id=user_id, category=category)
        return self._task_repo.create(task)

    def get_tasks_by_user(self, user_id):
        return self._task_repo.find_by_user_id(user_id)

    def mark_done(self, task_id):
        self._task_repo.set_done(task_id, done=True)

    def mark_undone(self, task_id):
        self._task_repo.set_done(task_id, done=False)

    def delete_task(self, task_id):
        self._task_repo.delete(task_id)

    def clear_all_tasks(self):
        self._task_repo.delete_all()


task_service = TaskService()
