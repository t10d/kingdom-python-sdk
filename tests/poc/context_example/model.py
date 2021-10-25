from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import uuid4

from kingdom_sdk.domain.aggregate import Aggregate
from kingdom_sdk.domain.entity import Entity
from kingdom_sdk.utils import time


class ExampleEntity(Entity):
    _name: str

    def __init__(
        self,
        id: UUID,  # noqa
        version: int,
        is_discarded: bool,
        registered_at: datetime,
        updated_at: datetime,
        name: str,
    ) -> None:
        super().__init__(id, version, is_discarded, registered_at, updated_at)
        self._name = name

    def __repr__(self) -> str:
        return self._base_repr(self._id.hex)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ExampleEntity):
            return self.id == other.id
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.id)

    @classmethod
    def create(cls, **kwargs: Any) -> ExampleEntity:
        """Use this instead the constructor.

        Keyword Args:
            name (str): ...
        """
        now = time.generate_now()
        return cls(
            id=uuid4(),
            version=0,
            is_discarded=False,
            registered_at=now,
            updated_at=now,
            name=kwargs["name"],
        )

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value


class ExampleAggregate(Aggregate):
    _value: float
    _reference: ExampleEntity

    def __init__(
        self,
        id: UUID,  # noqa
        version: int,
        is_discarded: bool,
        registered_at: datetime,
        updated_at: datetime,
        value: float,
        reference: ExampleEntity,
    ) -> None:
        super().__init__(id, version, is_discarded, registered_at, updated_at)
        self._value = value
        self._reference = reference

    def __repr__(self) -> str:
        return self._base_repr(self._id.hex)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ExampleEntity):
            return self.id == other.id
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.id)

    @classmethod
    def create(cls, **kwargs: Any) -> ExampleAggregate:
        """Use this instead the constructor..

        Keyword Args:
            value (float): ...
            reference (ExampleEntity): ...
        """
        now = time.generate_now()
        return cls(
            id=uuid4(),
            version=0,
            is_discarded=False,
            registered_at=now,
            updated_at=now,
            value=kwargs["value"],
            reference=kwargs["reference"],
        )
