from dataclasses import dataclass, field
from datetime import date
import uuid


@dataclass
class Statistics:
    """Daily statistics entity. Tracks total completed tasks and pomodoro time."""

    user_id: str
    tasks_completed: int = 0
    total_pomodoro_time: int = 0
    dstat_date: date = field(default_factory=date.today)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
