from abc import ABC
from datetime import datetime
from typing import List
from uuid import UUID

from kingdom_sdk.domain.entity import Entity
from kingdom_sdk.domain.message import Event


class Aggregate(Entity, ABC):
    """Base class for aggregates."""

    _events: List[Event]

    def __init__(
        self,
        id: UUID,  # noqa
        version: int,
        is_discarded: bool,
        registered_at: datetime,
        updated_at: datetime,
    ) -> None:
        super().__init__(id, version, is_discarded, registered_at, updated_at)
        self._events = []

    def add_events(self, *events: Event) -> None:
        self._check_not_discarded()
        self._events.extend(events)

    @property
    def has_events(self) -> bool:
        return len(self._events) > 0

    @property
    def next_event(self) -> Event:
        return self._events.pop(0)

    @property
    def events(self) -> List[Event]:
        return self._events
