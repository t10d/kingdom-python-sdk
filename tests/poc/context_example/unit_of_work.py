from kingdom_sdk.adapters.unit_of_work import SQLAlchemyUnitOfWork
from tests.poc.context_example import repository


class PocUnitOfWork(SQLAlchemyUnitOfWork):
    repository: repository.PocRepository
