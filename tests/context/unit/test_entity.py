import pytest

from kingdom_sdk.domain.entity import EntityDiscardedError


def test_entity_creation(transient_entity):
    assert transient_entity.name == "created"


def test_entity_update(transient_entity):
    last_version = transient_entity.version
    transient_entity.name = "updated"

    assert transient_entity.name == "updated"
    assert transient_entity.updated_at == transient_entity.registered_at
    assert transient_entity.version == last_version

    transient_entity.update()

    assert transient_entity.name == "updated"
    assert transient_entity.updated_at > transient_entity.registered_at
    assert transient_entity.version == last_version + 1


def test_entity_discard(transient_entity):
    assert not transient_entity.is_discarded

    transient_entity.discard()

    assert transient_entity.is_discarded

    with pytest.raises(EntityDiscardedError):
        transient_entity.name = "discarded"
        transient_entity.update()
