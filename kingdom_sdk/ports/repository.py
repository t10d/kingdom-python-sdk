from abc import ABC, abstractmethod
from typing import List, Optional

from kingdom_sdk.database.types import PrimaryKey_T
from kingdom_sdk.domain.aggregate import Aggregate


class AbstractRepository(ABC):
    def add(self, aggregate: Aggregate) -> None:
        return self._add(aggregate)

    def list(self) -> List[Aggregate]:
        return self._list()

    def get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        return self._get(id)

    @abstractmethod
    def _add(self, aggregate: Aggregate) -> None:
        raise NotImplementedError

    @abstractmethod
    def _list(self) -> List[Aggregate]:
        raise NotImplementedError

    @abstractmethod
    def _get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        raise NotImplementedError
