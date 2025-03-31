from datetime import date
import uuid

class Statistics:
    def __init__(self, user_id, date_select=None, tasks_completed=0, total_pomodoro_time=0, stat_id=None):
        """
        Daily statistics entity.
        Count the total tasks and overall working time.

        """
        self.id = stat_id or str(uuid.uuid4())
        self.user_id = user_id
        self.date = date_select or date.today()
        self.tasks_completed = tasks_completed
        self.total_pomodoro_time = total_pomodoro_time