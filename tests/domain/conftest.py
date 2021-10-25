import pytest

from tests.poc.context_example.model import ExampleEntity


@pytest.fixture
def transient_entity():
    return ExampleEntity.create(name="created")
