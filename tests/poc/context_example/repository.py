from kingdom_sdk.adapters.repository import SQLAlchemyRepository
from tests.poc.context_example import model


class PocRepository(SQLAlchemyRepository):
    __model__ = model.ExampleAggregate
