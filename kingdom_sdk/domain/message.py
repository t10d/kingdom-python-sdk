from __future__ import annotations

from abc import ABC
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from kingdom_sdk.domain.value_object import ValueObject
from kingdom_sdk.utils import loader


@dataclass(frozen=True)
class Message(ValueObject, ABC):
    """Base class for all commands and messages.

    Messages are value objects, so they are equality comparable.

    Args:
        raised_at: Timestamp when the message had generated.
        delay: ...
    """

    raised_at: datetime
    delay: int


@dataclass(frozen=True)
class Command(Message, ABC):
    """Base domain command.

    You must implement this class and annotate it with @dataclass(frozen=True).

    >>> @dataclass(frozen=True)
    ... class MyCommand(Command):
    ...     @classmethod
    ...     def create(cls, ...) -> MyCommand:
    ...         ...
    """


@dataclass(frozen=True)
class Event(Message, ABC):
    """Base domain event.

    You must implement this class and annotate it with @dataclass(frozen=True).

    >>> @dataclass(frozen=True)
    ... class MyEvent(Event):
    ...     @classmethod
    ...     def create(cls, ...) -> MyEvent:
    ...         ...

    Args:
        raised_by: The originating aggregate root id.
    """

    raised_by: UUID


@dataclass(frozen=True)
class PersistentMessage(ValueObject):
    module: str
    classname: str
    data: Dict[str, Any]

    @classmethod
    def create(cls, message: Message) -> PersistentMessage:  # type: ignore
        return cls(
            module=message.__class__.__module__,
            classname=message.__class__.__name__,
            data=asdict(message),
        )

    def load_object(self) -> Message:
        cls = loader.object_from_module(self.module, self.classname)
        return cls(**self.data)  # type: ignore
