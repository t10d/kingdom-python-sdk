import pytest

from tests.poc.context_example.model import ExampleEntity, ExampleVO


@pytest.fixture
def transient_entity():
    return ExampleEntity.create(name="created")


@pytest.fixture
def default_value_object():
    return ExampleVO.create(field="immutable")
