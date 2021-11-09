from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generator


class AbstractUnitOfWork(ABC):
    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args: Any) -> None:
        self.rollback()

    def commit(self) -> None:
        self._commit()

    def rollback(self) -> None:
        return self._rollback()

    @abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _rollback(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def execute_native_statement(self, statement: str, **params: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def collect_new_events(self) -> Generator:
        raise NotImplementedError
