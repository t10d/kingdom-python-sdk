from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

from kingdom_sdk.ports.unit_of_work import AbstractUnitOfWork


class AbstractRawSQLMixin(ABC):
    @abstractmethod
    def _build_statement(self) -> str:
        raise NotImplementedError


class AbstractTemplateSQLMixin(ABC):
    @abstractmethod
    def _build_statement(self, **params: Any) -> Tuple[str, Dict]:
        raise NotImplementedError


class AbstractWriteQuery(ABC):
    @abstractmethod
    def execute(self, uow: AbstractUnitOfWork, commit: bool = True) -> None:
        raise NotImplementedError


class AbstractReadQuery(ABC):
    @abstractmethod
    def execute(
        self, uow: AbstractUnitOfWork, commit: bool = False, **params: Any
    ) -> Dict:
        raise NotImplementedError


class AbstractDDLInterface(AbstractWriteQuery, ABC):
    """Data Definition Language Interface.

    Only use it for CREATE, ALTER, and DROP operations.
    """


class AbstractDMLInterface(AbstractWriteQuery, ABC):
    """Data Modification Language Interface.

    Only use it for INSERT, DELETE, and UPDATE operations.
    """


class AbstractDQLInterface(AbstractReadQuery, ABC):
    """Data Query Language Interface.

    Only use it for SELECT operations.
    """


class AbstractDTLInterface(AbstractReadQuery, ABC):
    """Data Transaction Language Interface.

    Only use it for BEGIN TRANSACTION, COMMIT, and ROLLBACK operations.
    """


class AbstractDCLInterface(AbstractWriteQuery, ABC):
    """Data Control Language Interface.

    Only use it for GRANT, REVOKE, and DENY operations.
    """
