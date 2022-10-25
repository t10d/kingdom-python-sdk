from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from kingdom_sdk.domain.message import Event
from kingdom_sdk.utils import time


@dataclass(frozen=True)
class ExampleAggregateCreated(Event):
    name: str

    @classmethod
    def create(cls, **kwargs: Any) -> ExampleAggregateCreated:
        """Use this insted the constructor.

        Keyword Args:
            id (UUID): ...
            name (str): ...
        """
        return cls(
            raised_at=time.generate_now(),
            delay=0,
            raised_by=kwargs["id"],
            name=kwargs["name"],
        )
