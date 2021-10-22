from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AbstractUnitOfWork(ABC):
    def __enter__(self) -> AbstractUnitOfWork:
        return self._with_context()

    def __exit__(self, *args: Any) -> None:
        self.rollback()

    def commit(self) -> None:
        self._commit()

    def rollback(self) -> None:
        return self._rollback()

    @abstractmethod
    def _with_context(self) -> AbstractUnitOfWork:
        raise NotImplementedError

    @abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _rollback(self) -> None:
        raise NotImplementedError
