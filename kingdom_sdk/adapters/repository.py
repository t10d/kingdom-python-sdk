from __future__ import annotations

from abc import ABC
from typing import List, Optional, Set, Type

from sqlalchemy.orm import Session

from kingdom_sdk.database.types import PrimaryKey_T
from kingdom_sdk.domain.aggregate import Aggregate
from kingdom_sdk.ports.repository import AbstractRepository


class BaseRepository(AbstractRepository, ABC):
    """Generic repository.

    You only need to extend it and override the static attribute _model.

    >>> class MyRepositoy(BaseRepository):
    ...     _model = ...
    """

    _model: Type[Aggregate]
    _session: Session
    _seen: Set[Aggregate]

    def __init__(self, session: Session) -> None:
        self._session = session
        self._seen: Set[Aggregate] = set()

    def get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        aggregate = self._get(id)
        if aggregate:
            self._seen.add(aggregate)
        return aggregate

    def _add(self, aggregate: Aggregate) -> None:
        self._seen.add(aggregate)
        self._session.add(aggregate)

    def _list(self) -> List[Aggregate]:
        return self._session.query(self._model).all()  # type: ignore

    def _get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        return (  # type: ignore
            self._session.query(self._model)
            .filter(
                self._model._id == id,  # noqa
                self._model._is_discarded._is(False),  # type: ignore  # noqa
            )
            .first()
        )
