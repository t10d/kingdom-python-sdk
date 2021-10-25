import os

from sqlalchemy import MetaData

import kingdom_sdk
from kingdom_sdk.database.orm import auto_start_mappers


def bootstrap() -> MetaData:
    return auto_start_mappers(
        os.path.join(kingdom_sdk._get_base_dir(), "tests/poc/")  # noqa
    )
