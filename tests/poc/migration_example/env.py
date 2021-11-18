from logging.config import fileConfig

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import orm

from kingdom_sdk.database.migrations import (
    run_migrations_offline,
    run_migrations_online,
)
from tests.poc.context_example.bootstrap import bootstrap

load_dotenv()

# This is the Alembic Config object,
# which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your model's MetaData object here.
# For 'autogenerate' support:
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
orm.clear_mappers()
target_metadata = bootstrap()

# Postgres schema name, where the "alembic_version" table will be stored.
SCHEMA_NAME = "poc"

# Other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


if context.is_offline_mode():
    run_migrations_offline(SCHEMA_NAME, target_metadata)
else:
    run_migrations_online(SCHEMA_NAME, target_metadata)
