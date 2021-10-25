from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import UUID  # noqa: F401

from kingdom_sdk.domain.message import Event
from kingdom_sdk.utils import time


@dataclass(frozen=True)
class ExampleAggregateCreated(Event):
    @classmethod
    def create(cls, **kwargs: Any) -> ExampleAggregateCreated:
        """Use this insted the constructor.

        Keyword Args:
            id (UUID): ...
        """
        return cls(
            raised_at=time.generate_now(),
            type="Event",
            kind=cls.__name__,
            delay=0,
            raised_by=kwargs["id"],
        )
