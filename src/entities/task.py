from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Task:
    """Task entity. 'done' defaults to False; 'category' may not be used in statistics."""

    content: str
    done: bool = False
    user_id: str = None
    category: str = field(default="general")
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
