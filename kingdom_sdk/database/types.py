from typing import Callable

from sqlalchemy import MetaData, Table

TableFactory_T = Callable[[MetaData], Table]

__all__ = ["TableFactory_T"]
