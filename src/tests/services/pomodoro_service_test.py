import unittest
from datetime import datetime, timedelta
from services.pomodoro_service import PomodoroService
from entities.pomodoro import PomodoroSession


class FakePomodoroRepository:
    def __init__(self):
        self.sessions = []

    def create(self, session):
        self.sessions.append(session)
        return session

    def find_by_task_id(self, task_id):
        result = []
        for session in self.sessions:
            if session.task_id == task_id:
                result.append(session)
        return result

    def find_all(self):
        return self.sessions

    def delete_all(self):
        self.sessions.clear()


class TestPomodoroService(unittest.TestCase):
    def setUp(self):
        self.repo = FakePomodoroRepository()
        self.service = PomodoroService(pomodoro_repo=self.repo)

    def test_start_and_stop_creates_session(self):
        self.service.start()
        self.service._current_start_time -= timedelta(minutes=10)
        session = self.service.stop(task_id="appletask")

        self.assertEqual(session.task_id, "appletask")
        self.assertEqual(session.duration, 10)
        self.assertEqual(len(self.repo.sessions), 1)

    def test_stop_without_start_raises_error(self):
        with self.assertRaises(ValueError):
            self.service.stop(task_id="appletask")

    def test_get_sessions_by_task(self):
        session1 = PomodoroSession(
            task_id="banana1", start_time=datetime.now(), end_time=datetime.now(), duration=20)
        session2 = PomodoroSession(
            task_id="banana2", start_time=datetime.now(), end_time=datetime.now(), duration=30)
        self.repo.create(session1)
        self.repo.create(session2)

        task1_sessions = self.service.get_sessions_by_task("banana1")
        self.assertEqual(len(task1_sessions), 1)
        self.assertEqual(task1_sessions[0].task_id, "banana1")

    def test_delete_all(self):
        self.repo.create(PomodoroSession(
            task_id="grape", start_time=datetime.now(), end_time=datetime.now(), duration=10))
        self.service.delete_all()
        self.assertEqual(len(self.repo.find_all()), 0)


if __name__ == "__main__":
    unittest.main()
