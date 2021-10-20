from typing import Any

from sqlalchemy import Table
from sqlalchemy.orm import mapper

from kingdom_sdk.domain.aggregate import Aggregate, RootAggregate
from kingdom_sdk.domain.entity import Entity


def entity_mapper(entity: Entity, table: Table, **properties: Any) -> None:
    mapper(
        entity,
        table,
        properties={
            "_id": table.c.id,  # noqa
            "_version": table.c.version,  # noqa
            "_is_discarded": table.c.is_discarded,  # noqa
            "_registered_at": table.c.registered_at,  # noqa
            "_updated_at": table.c.updated_at,  # noqa
            **properties,
        },
    )


def aggregate_mapper(
    aggregate: Aggregate, table: Table, **properties: Any
) -> None:
    entity_mapper(aggregate, table, **properties)


def root_aggregate_mapper(
    aggregate: RootAggregate, table: Table, **properties: Any
) -> None:
    aggregate_mapper(aggregate, table, **properties)
