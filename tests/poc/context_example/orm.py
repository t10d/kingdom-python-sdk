from typing import Any

from sqlalchemy import Column, Float, ForeignKey, MetaData, String
from sqlalchemy.orm import events, relationship

from kingdom_sdk.database.factories import (
    aggregate_table_factory,
    entity_table_factory,
)
from kingdom_sdk.database.mappers import aggregate_mapper, entity_mapper
from kingdom_sdk.domain.aggregate import Aggregate
from tests.poc.context_example import model

examples_entity = entity_table_factory(
    "poc", "examples_entity", Column("name", String(255), nullable=False)
)

examples_aggregate = aggregate_table_factory(
    "poc",
    "examples_aggregate",
    Column("value", Float(), nullable=False),
    Column(
        "reference_id", ForeignKey("poc.examples_entity.id"), nullable=False
    ),
)


def start_mappers(metadata: MetaData) -> None:
    examples_entity_t = examples_entity(metadata)
    entity_mapper(model.ExampleEntity, examples_entity_t)

    examples_aggregate_t = examples_aggregate(metadata)
    aggregate_mapper(
        model.ExampleAggregate,
        examples_aggregate_t,
        properties={
            "_reference": relationship(
                model.ExampleEntity, uselist=False, cascade="all, delete"
            )
        },
    )


@events.event.listens_for(model.ExampleAggregate, "load")
def load_event_list(aggregate: Aggregate, *_: Any) -> None:
    aggregate._events = []
