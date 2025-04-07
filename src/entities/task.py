from datetime import datetime
import uuid


class Task:
    def __init__(self, content, done=False, user_id=None, task_id=None, category=None, created_at=None):
        """
            done: default to be false.
            category function might not be applied in the stats module.
        """

        self.id = task_id or str(uuid.uuid4())
        self.user_id = user_id
        self.content = content
        self.done = done
        self.created_at = created_at or datetime.now()
        self.category = category or "general"
