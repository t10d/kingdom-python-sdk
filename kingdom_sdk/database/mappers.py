from typing import Any, Type

from sqlalchemy import Table
from sqlalchemy.orm import mapper

from kingdom_sdk.domain.aggregate import Aggregate
from kingdom_sdk.domain.entity import Entity


def entity_mapper(
    entity: Type[Entity], table: Table, **properties: Any
) -> None:
    mapper(
        entity,
        table,
        column_prefix="_",
        **properties,
    )


def aggregate_mapper(
    aggregate: Type[Aggregate], table: Table, **properties: Any
) -> None:
    entity_mapper(aggregate, table, **properties)
