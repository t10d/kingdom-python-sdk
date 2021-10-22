from abc import ABC
from typing import Any, List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from kingdom_sdk import config
from kingdom_sdk.ports.unit_of_work import AbstractUnitOfWork

DEFAULT_SESSION_FACTORY = sessionmaker(
    # ISOLATION LEVEL ENSURES aggregate's version IS RESPECTED
    # That is, if version differs it will raise an exception
    bind=create_engine(
        config.get_database_url(),
        isolation_level="REPEATABLE_READ",
    ),
    autoflush=False,
)


class BaseUnitOfWork(AbstractUnitOfWork, ABC):
    _errors: List[Any]
    _session_factory: sessionmaker
    _session: Session

    def __init__(
        self, session_factory: sessionmaker = DEFAULT_SESSION_FACTORY
    ) -> None:
        self._errors = []
        self._session_factory = session_factory

    def __enter__(self) -> AbstractUnitOfWork:
        self._session = self._session_factory()
        return super().__enter__()

    def __exit__(self, *args: Any) -> None:
        super().__exit__(*args)
        self._session.close()

    def _commit(self) -> None:
        self._session.commit()

    def _rollback(self) -> None:
        self._session.rollback()
