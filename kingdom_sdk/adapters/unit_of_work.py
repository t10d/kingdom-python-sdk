from abc import ABC
from typing import Any, Generator, Iterator, List, Set, Tuple

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from kingdom_sdk import config
from kingdom_sdk.domain.aggregate import Aggregate
from kingdom_sdk.domain.exception import KingdomError
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


class SQLAlchemyUnitOfWork(AbstractUnitOfWork, ABC):
    """Generic SQLAlchemy Unit of Work.

    You only need to extend it and annotate the repositories types.

    >>> class MyUnitOfWork(SQLAlchemyUnitOfWork):
    ...     repository: ...
    """

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
        self._initialize_repositories(self._session)
        return super().__enter__()

    def __exit__(self, *args: Any) -> None:
        super().__exit__(*args)
        self._session.close()

    def _commit(self) -> None:
        self._session.commit()

    def _rollback(self) -> None:
        self._session.rollback()

    def execute_native_statement(self, statement: str, **params: Any) -> Any:
        return self._session.execute(statement, params)

    def collect_new_events(self) -> Generator:
        dirty: Set[Aggregate] = set()

        for field_name, _ in self._repositories:
            try:
                repository = self.__dict__[field_name]
            except KeyError as error:
                raise RepositoryNotIntializedError(str(error))

            if hasattr(repository, "_seen"):
                dirty = dirty.union(repository._seen)  # noqa

        for aggregate in dirty:
            while aggregate.has_events:
                yield aggregate.next_event

    def _initialize_repositories(self, session: Session) -> None:
        for field_name, repository in self._repositories:
            self.__dict__[field_name] = repository(session)

    @property
    def _repositories(self) -> Iterator[Tuple[str, Any]]:
        return (
            (field, module)
            for field, module in self.__annotations__.items()
            if not field.startswith("_")
        )


class RepositoryNotIntializedError(KingdomError):
    def __init__(self, repository_name: str) -> None:
        super().__init__(
            f"The repository '{repository_name}' haven't been initialized yet",
            "REPOSITORY_NOT_INITIALIZED_ERROR",
        )
