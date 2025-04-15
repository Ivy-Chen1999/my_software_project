from datetime import datetime
from entities.pomodoro import PomodoroSession
from database_connection import get_database_connection


class PomodoroRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def create(self, session: PomodoroSession):
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO pomodoros (id, task_id, start_time, end_time, duration)
            VALUES (?, ?, ?, ?, ?)
        """, (
            session.id,
            session.task_id,
            session.start_time.isoformat(),
            session.end_time.isoformat(),
            session.duration
        ))
        self._connection.commit()
        return session

    def find_all(self):
        cursor = self._connection.cursor()
        rows = cursor.execute("SELECT * FROM pomodoros").fetchall()
        return [self._row_to_session(row) for row in rows]

    def find_by_task_id(self, task_id):
        cursor = self._connection.cursor()
        rows = cursor.execute(
            "SELECT * FROM pomodoros WHERE task_id = ?", (task_id,)
        ).fetchall()
        return [self._row_to_session(row) for row in rows]

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM pomodoros")
        self._connection.commit()

    def _row_to_session(self, row):
        return PomodoroSession(
            id=row["id"],
            task_id=row["task_id"],
            start_time=datetime.fromisoformat(row["start_time"]),
            end_time=datetime.fromisoformat(row["end_time"]),
            duration=row["duration"]
        )


pomodoro_repository = PomodoroRepository()
