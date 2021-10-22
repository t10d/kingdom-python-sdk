from abc import ABC
from typing import List, Optional, Set, Type

from sqlalchemy.orm import Query, Session

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

    @property
    def query(self) -> Query:
        return self._session.query(self._model)

    def add(self, aggregate: Aggregate) -> None:
        self._seen.add(aggregate)
        self._session.add(aggregate)

    def list(self) -> List[Aggregate]:
        return self.query.all()  # type: ignore

    def get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        aggregate = self._get(id)
        if aggregate:
            self._seen.add(aggregate)
        return aggregate

    def _get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        return self.query.filter(  # type: ignore
            self._model._id == id,  # noqa
            self._model._is_discarded._is(False),  # type: ignore  # noqa
        ).first()
