from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Integer, MetaData, Table
from sqlalchemy.dialects.postgresql import UUID

from kingdom_sdk.utils import time


def create_entity_table(
    name: str, metadata: MetaData, *columns: Column
) -> Table:
    return Table(
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


def create_aggregate_table(
    name: str, metadata: MetaData, *columns: Column
) -> Table:
    return create_entity_table(name, metadata, *columns)


def create_root_aggregate_table(
    name: str, metadata: MetaData, *columns: Column
) -> Table:
    return create_aggregate_table(name, metadata, *columns)
