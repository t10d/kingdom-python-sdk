from abc import ABC
from typing import List, Optional, Set, Type

from sqlalchemy.orm import Query, Session

from kingdom_sdk.database.types import PrimaryKey_T
from kingdom_sdk.domain.aggregate import Aggregate
from kingdom_sdk.ports.repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository, ABC):
    """Generic SQLAlchemy repository.

    You only need to extend it and override the static attribute __model__.

    >>> class MyRepositoy(SQLAlchemyRepository):
    ...     __model__ = ...
    """

    __model__: Type[Aggregate]

    _session: Session
    _seen: Set[Aggregate]

    def __init__(self, session: Session) -> None:
        self._session = session
        self._seen: Set[Aggregate] = set()

    @property
    def query(self) -> Query:
        return self._session.query(self.__model__)

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
            self.__model__._id == id,  # noqa
            self.__model__._is_discarded == False,  # noqa
        ).first()
