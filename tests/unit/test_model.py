from dataclasses import FrozenInstanceError

import pytest

from kingdom_sdk.domain.entity import EntityDiscardedError


class TestEntity:
    def test_entity_creation(self, example_entity):
        assert example_entity.name == "created"

    def test_entity_update(self, example_entity):
        last_version = example_entity.version
        example_entity.name = "updated"

        assert example_entity.name == "updated"
        assert example_entity.updated_at == example_entity.registered_at
        assert example_entity.version == last_version

        example_entity.update()

        assert example_entity.name == "updated"
        assert example_entity.updated_at > example_entity.registered_at
        assert example_entity.version == last_version + 1

    def test_entity_discard(self, example_entity):
        assert not example_entity.is_discarded

        example_entity.discard()

        assert example_entity.is_discarded

        with pytest.raises(EntityDiscardedError):
            example_entity.name = "discarded"
            example_entity.update()


class TestAggregate:
    def test_aggregate_creation(self, example_aggregate):
        assert example_aggregate.value == 1.0

    def test_aggregate_update(self, example_aggregate):
        last_version = example_aggregate.version
        example_aggregate.value = 2.0

        assert example_aggregate.value == 2.0
        assert example_aggregate.updated_at == example_aggregate.registered_at
        assert example_aggregate.version == last_version

        example_aggregate.update()

        assert example_aggregate.value == 2.0
        assert example_aggregate.updated_at > example_aggregate.registered_at
        assert example_aggregate.version == last_version + 1

    def test_aggregate_discard(self, example_aggregate):
        assert not example_aggregate.is_discarded

        example_aggregate.discard()

        assert example_aggregate.is_discarded

        with pytest.raises(EntityDiscardedError):
            example_aggregate.value = 0.0
            example_aggregate.update()


class TestValueObject:
    def test_vo_creation(self, example_value_object):
        assert example_value_object.field == "immutable"

    def test_vo_update_failed(self, example_value_object):
        with pytest.raises(FrozenInstanceError):
            example_value_object.field = "changed!"
