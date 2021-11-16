from abc import ABC, abstractmethod
from typing import List, Optional

from kingdom_sdk.database.types import PrimaryKey_T
from kingdom_sdk.domain.aggregate import Aggregate


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, aggregate: Aggregate) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Aggregate]:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: PrimaryKey_T) -> Optional[Aggregate]:  # noqa
        raise NotImplementedError
