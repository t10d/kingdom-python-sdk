import os
from unittest.mock import MagicMock
from uuid import uuid4

import pytest

import kingdom_sdk
from kingdom_sdk.adapters.message_broker import RedisMessageBroker
from kingdom_sdk.adapters.message_bus import MessageBus
from tests.poc.context_example.bootstrap import bootstrap
from tests.poc.context_example.command import (
    CreateExampleAggregate,
    ExemplifyUnhandlableCommand,
)
from tests.poc.context_example.event import ExampleAggregateCreated
from tests.poc.context_example.model import (
    ExampleAggregate,
    ExampleEntity,
    ExampleVO,
)
from tests.poc.context_example.unit_of_work import PocUnitOfWork


@pytest.fixture(scope="session")
def uow():
    bootstrap()
    return PocUnitOfWork()


@pytest.fixture(scope="session")
def message_broker():
    return RedisMessageBroker()


@pytest.fixture(scope="session")
def message_bus(uow, example_event_handlers, example_command_handlers):
    return MessageBus.create(
        uow=uow,
        event_handlers=example_event_handlers,
        command_handlers=example_command_handlers,
        dependencies={},
    )


@pytest.fixture
def base_dir():
    return kingdom_sdk._get_base_dir()  # noqa


@pytest.fixture
def src_dir():
    return kingdom_sdk._get_src_dir()  # noqa


@pytest.fixture
def poc_dir(base_dir):
    return os.path.join(base_dir, "tests/poc/")


@pytest.fixture
def query_path(poc_dir):
    return os.path.join(poc_dir, "context_example/queries/query.sql")


@pytest.fixture
def example_entity():
    return ExampleEntity.create(name="created")


@pytest.fixture
def example_aggregate(example_entity):
    return ExampleAggregate.create(value=1.0, reference=example_entity)


@pytest.fixture
def example_value_object():
    return ExampleVO.create(field="immutable")


@pytest.fixture
def example_command():
    return CreateExampleAggregate.create(name="raised", value=1.0)


@pytest.fixture
def example_unhandlable_command():
    return ExemplifyUnhandlableCommand.create()


@pytest.fixture(scope="session")
def example_command_handlers():
    return {CreateExampleAggregate: MagicMock()}


@pytest.fixture
def example_event():
    return ExampleAggregateCreated.create(id=uuid4(), name="raised")


@pytest.fixture(scope="session")
def example_event_handlers():
    return {ExampleAggregateCreated: [MagicMock(), MagicMock()]}
