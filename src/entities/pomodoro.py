from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class PomodoroSession:
    task_id: str
    start_time: datetime
    end_time: datetime
    duration: int
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
