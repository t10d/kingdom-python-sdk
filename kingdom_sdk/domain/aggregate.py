from abc import ABC
from typing import List

from kingdom_sdk.domain.entity import Entity
from kingdom_sdk.domain.message import Event


class Aggregate(Entity, ABC):
    """Base class for aggregates."""

    _events: List[Event]

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


class RootAggregate(Aggregate, ABC):
    """Base class for root aggregates.

    There's only one root aggregate for each bounded context.
    """
