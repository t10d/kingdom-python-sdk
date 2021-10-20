from __future__ import annotations

from abc import ABC
from dataclasses import asdict, dataclass
from datetime import datetime
from importlib import import_module
from typing import Any, Dict
from uuid import UUID

from kingdom_sdk.utils import time


@dataclass(frozen=True)
class Message(ABC):
    """Base class for all commands and messages.

    Messages are value objects, so they are equality comparable.

    Args:
        type: ...
        kind: ...
        raised_at: Timestamp when the message had generated.
        delay: ...
    """

    type: str
    kind: str
    raised_at: datetime
    delay: int


@dataclass(frozen=True)
class Command(Message, ABC):
    """Base domain command."""


@dataclass(frozen=True)
class Event(Message, ABC):
    """Base domain event.

    Args:
        raised_by: The originating aggregate root id.
    """

    raised_by: UUID


@dataclass(frozen=True)
class PersistentMessage:
    module: str
    classname: str
    data: Dict[str, Any]

    def load_object(self) -> Message:
        module = import_module(self.module)
        cls = getattr(module, self.classname)
        return cls(**self.data)  # type: ignore


if __name__ == "__main__":
    # Example to store the data in JSON and load it as object again.

    msg = Message(
        type="GenericMessage",
        kind="Event",
        raised_at=time.generate_now(),
        delay=1,
    )

    pm = PersistentMessage(
        msg.__class__.__module__, msg.__class__.__name__, asdict(msg)
    )

    print(pm.load_object())
