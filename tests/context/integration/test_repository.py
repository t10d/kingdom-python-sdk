from dataclasses import asdict

from tests.poc.context_example.model import ExampleAggregate, ExampleEntity


def test_aggrate_save(uow, raised_command):
    entity = ExampleEntity.create(**asdict(raised_command))
    aggregate = ExampleAggregate.create(
        value=raised_command.value,
        reference=entity,
    )

    with uow:
        uow.repository.add(aggregate)
        uow.commit()

    with uow:
        result: ExampleAggregate = uow.repository.get(aggregate.id)

    assert result
    assert result == aggregate
    assert result.reference == entity


def test_aggregate_list(uow):
    with uow:
        result = uow.repository.list()
        assert result
