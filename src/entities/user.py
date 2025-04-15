from dataclasses import dataclass, field
import uuid


@dataclass
class User:
    """User entity. Supports multiple users, extensible in future."""
    username: str
    password: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
