from typing import Callable, Union
from uuid import UUID

from sqlalchemy import MetaData, Table

PrimaryKey_T = Union[int, str, UUID]
TableFactory_T = Callable[[MetaData], Table]

__all__ = ["PrimaryKey_T", "TableFactory_T"]
