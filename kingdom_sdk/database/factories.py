from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Integer, Table
from sqlalchemy.dialects.postgresql import UUID

from kingdom_sdk.database.types import TableFactory_T
from kingdom_sdk.utils import time


def entity_table_factory(name: str, *columns: Column) -> TableFactory_T:
    return lambda metadata: Table(
        name,
        metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        Column("version", Integer(), nullable=False, default=0),
        Column("is_discarded", Boolean(), nullable=False, default=False),
        Column(
            "registered_at",
            DateTime(),
            nullable=False,
            default=time.generate_now,
        ),
        Column(
            "updated_at",
            DateTime(),
            nullable=False,
            default=time.generate_now,
        ),
        *columns,
    )


def aggregate_table_factory(name: str, *columns: Column) -> TableFactory_T:
    return entity_table_factory(name, *columns)


def root_aggregate_table_factory(
    name: str, *columns: Column
) -> TableFactory_T:
    return aggregate_table_factory(name, *columns)


def relationship_table_factory(name: str, *columns: Column) -> TableFactory_T:
    return lambda metadata: Table(name, metadata, *columns)
