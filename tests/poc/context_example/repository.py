from kingdom_sdk.adapters.repository import BaseRepository
from tests.poc.context_example import model


class PocRepository(BaseRepository):
    __model__ = model.ExampleAggregate
