from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any
from uuid import UUID

from kingdom_sdk.domain.exception import KingdomError
from kingdom_sdk.utils import time


class Entity(ABC):
    """Represent the base element in the domain model, for entities and its
    aggregates.

    Args:
        id: Global unique identifier.
        version: Value used to handle optmistic concurrency.
        is_discarded: Flag used by the no-deletion convention.
        registered_at: Timestamp when the entity had created.
        updated_at: Timestamp when the last modification had done.
    """

    _id: UUID
    _version: int
    _is_discarded: bool
    _registered_at: datetime
    _updated_at: datetime

    def __init__(
        self,
        id: UUID,  # noqa
        version: int,
        is_discarded: bool,
        registered_at: datetime,
        updated_at: datetime,
    ) -> None:
        self._id = id
        self._version = version
        self._is_discarded = is_discarded
        self._registered_at = registered_at
        self._updated_at = updated_at

    def _check_not_discarded(self) -> None:
        """Call this method before every update action."""
        if self.is_discarded:
            classname = self.__class__.__name__
            raise EntityDiscardedError(f"{classname} object is discarded")

    def _base_repr(self, identifier: str, **kwargs: str) -> str:
        """Use this method in the __repr__ implementation.

        >>> def __repr__(...) -> str:
        ...     return self._base_repr(...)
        """
        pairs = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
        return "{prefix}<{classname} '{identifier}'{extra}>".format(
            prefix="**DISCARDED** " if self.is_discarded else "",
            classname=self.__class__.__name__,
            identifier=identifier,
            extra=f" ({pairs})" if kwargs else "",
        )

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def create(cls, **kwargs: Any) -> Entity:
        raise NotImplementedError

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def version(self) -> int:
        return self._version

    @property
    def is_discarded(self) -> bool:
        return self._is_discarded

    @property
    def registered_at(self) -> datetime:
        return self._registered_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update(self) -> None:
        """Remember to call this method before commiting a change."""
        self._check_not_discarded()
        self._update()

    def _update(self) -> None:
        self._version += 1
        self._updated_at = time.generate_now()

    def discard(self) -> None:
        """By convention, isn't necessary delete an object, only mark it as
        discarded.
        """
        self._is_discarded = True
        self._update()


class EntityDiscardedError(KingdomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, "ENTITY_DISCARDED_ERROR")
