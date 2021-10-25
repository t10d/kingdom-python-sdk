from kingdom_sdk.adapters.repository import BaseRepository
from tests.poc.context_example import model


class PocRepository(BaseRepository):
    _model = model.ExampleAggregate
