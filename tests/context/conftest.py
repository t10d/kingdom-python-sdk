from uuid import uuid4

import pytest

from tests.poc.context_example.bootstrap import bootstrap
from tests.poc.context_example.command import CreateExampleAggregate
from tests.poc.context_example.event import ExampleAggregateCreated
from tests.poc.context_example.model import ExampleEntity, ExampleVO
from tests.poc.context_example.unit_of_work import PocUnitOfWork


@pytest.fixture
def transient_entity():
    return ExampleEntity.create(name="created")


@pytest.fixture
def default_value_object():
    return ExampleVO.create(field="immutable")


@pytest.fixture
def raised_command():
    return CreateExampleAggregate.create(name="raised", value=1.0)


@pytest.fixture
def raised_event():
    return ExampleAggregateCreated.create(id=uuid4())


@pytest.fixture(scope="session", autouse=True)
def uow():
    bootstrap()
    return PocUnitOfWork()
