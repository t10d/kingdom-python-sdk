from kingdom_sdk.adapters.unit_of_work import BaseUnitOfWork
from tests.poc.context_example import repository


class PocUnitOfWork(BaseUnitOfWork):
    repository = repository.PocRepository
