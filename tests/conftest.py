import os
from uuid import uuid4

import pytest

import kingdom_sdk
from tests.poc.context_example.bootstrap import bootstrap
from tests.poc.context_example.command import CreateExampleAggregate
from tests.poc.context_example.event import ExampleAggregateCreated
from tests.poc.context_example.model import (
    ExampleAggregate,
    ExampleEntity,
    ExampleVO,
)
from tests.poc.context_example.unit_of_work import PocUnitOfWork


@pytest.fixture(scope="session", autouse=True)
def uow():
    bootstrap()
    return PocUnitOfWork()


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
def example_event():
    return ExampleAggregateCreated.create(id=uuid4(), name="raised")
