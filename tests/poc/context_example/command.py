from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from kingdom_sdk.domain.message import Command
from kingdom_sdk.utils import time


@dataclass(frozen=True)
class CreateExampleAggregate(Command):
    value: float
    name: str

    @classmethod
    def create(cls, **kwargs: Any) -> CreateExampleAggregate:
        """Use this insted the constructor.

        Keyword Args:
            value (float): ...
            name (str): ...
        """
        return cls(
            raised_at=time.generate_now(),
            delay=0,
            value=kwargs["value"],
            name=kwargs["name"],
        )


@dataclass(frozen=True)
class ExemplifyUnhandlableCommand(Command):
    @classmethod
    def create(cls, **kwargs: Any) -> ExemplifyUnhandlableCommand:
        """Use this insted the constructor."""
        return cls(
            raised_at=time.generate_now(),
            delay=0,
        )
