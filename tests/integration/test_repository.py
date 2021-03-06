from dataclasses import asdict

from tests.poc.context_example.model import ExampleAggregate, ExampleEntity


def test_aggregate_save(uow, example_command):
    entity = ExampleEntity.create(**asdict(example_command))
    aggregate = ExampleAggregate.create(
        value=example_command.value,
        reference=entity,
    )

    with uow:
        uow.repository.add(aggregate)
        uow.commit()


def test_aggregate_list(uow):
    with uow:
        result = uow.repository.list()
        assert result
