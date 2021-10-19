from abc import ABC
from typing import Iterable

from kingdom_sdk.domain.model.entity import Entity
from kingdom_sdk.domain.model.event import Event


class Aggregate(Entity, ABC):
    _events: Iterable[Event]


class RootAggregate(Aggregate, ABC):
    pass
