from importlib import import_module
from importlib.machinery import SourceFileLoader

from sqlalchemy import MetaData

from kingdom_sdk.utils import files


def auto_start_mappers(src_dir: str) -> MetaData:
    """Discover orm.py files and run sqlalchemy's mappers automatically.

    Args:
        src_dir: Absolute path where is located the source to search.

    Returns:
        SQLAlchemy MetaData.
    """
    metadata = MetaData()
    orm_files = files.find("orm.py", src_dir)

    for path in orm_files:
        module = SourceFileLoader("start_mappers", path).load_module()
        module.start_mappers(metadata)  # type: ignore

    return metadata


def start_mappers(*modules: str) -> MetaData:
    """Update metadata reference and run sqlalchemy's mappers, classical way.

    >>> start_mappers('my.module.1.orm', 'my.module.2.orm')

    Args:
        modules: Enumeration of the modules (dot-case format).

    Returns:
        SQLAlchemy MetaData.

    Raises:
        ModuleNotFoundError: If the module is wrong or it doesn't exist.
    """
    metadata = MetaData()

    for module_name in modules:
        module = import_module(module_name)
        module.start_mappers(metadata)  # type: ignore

    return metadata
