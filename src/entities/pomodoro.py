# from datetime import datetime
import uuid


class PomodoroSession:
    def __init__(self, task_id, start_time, end_time, duration, session_id=None):  # pylint: disable=too-many-positional-arguments
        """
        One task may have multiple pomodoro sessions.
        """
        self.id = session_id or str(uuid.uuid4())
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
