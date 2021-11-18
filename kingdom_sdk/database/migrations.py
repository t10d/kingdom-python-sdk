from typing import Optional

from alembic import context
from sqlalchemy import MetaData, create_engine

from kingdom_sdk import config

_include_object = (
    lambda schema: lambda object, name, type, reflected, compare_to: not (
        type == "table" and object.schema != schema
    )
)


def run_migrations_offline(
    metadata: MetaData, schema: Optional[str] = None
) -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    if schema:
        context.configure(
            url=config.get_database_url(),
            target_metadata=metadata,
            literal_binds=True,
            include_schemas=True,
            include_object=_include_object(schema),
            dialect_opts={"paramstyle": "named"},
            version_table_schema=schema,
        )
    else:
        context.configure(
            url=config.get_database_url(),
            target_metadata=metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online(
    metadata: MetaData, schema: Optional[str] = None
) -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = create_engine(config.get_database_url())

    with connectable.connect() as connection:
        if schema:
            context.configure(
                connection=connection,
                target_metadata=metadata,
                include_schemas=True,
                include_object=_include_object(schema),
                version_table_schema=schema,
            )
        else:
            context.configure(connection=connection, target_metadata=metadata)

        with context.begin_transaction():
            context.run_migrations()
