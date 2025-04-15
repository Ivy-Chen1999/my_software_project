from datetime import datetime
from entities.pomodoro import PomodoroSession
from repositories.pomodoro_repository import pomodoro_repository


class PomodoroService:
    def __init__(self, pomodoro_repo=pomodoro_repository):
        self._repo = pomodoro_repo
        self._current_start_time = None

    def start(self):
        self._current_start_time = datetime.now()
        print(
            f"Pomodoro started at {self._current_start_time.strftime('%H:%M:%S')}")

    def stop(self, task_id):
        if not task_id:
            raise ValueError("Task ID cannot be empty.")
        if not self._current_start_time:
            raise ValueError("No Pomodoro session was started.")

        end_time = datetime.now()
        duration = (end_time - self._current_start_time).seconds // 60

        session = PomodoroSession(
            task_id=task_id,
            start_time=self._current_start_time,
            end_time=end_time,
            duration=duration
        )

        self._current_start_time = None
        return self._repo.create(session)

    def get_sessions_by_task(self, task_id):
        if not task_id:
            raise ValueError("Task ID is required.")
        return self._repo.find_by_task_id(task_id)

    def get_all_sessions(self):
        return self._repo.find_all()

    def delete_all(self):
        self._repo.delete_all()
