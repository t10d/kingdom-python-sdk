from importlib import import_module
from importlib.machinery import SourceFileLoader

from sqlalchemy import MetaData

from kingdom_core.utils import files


def auto_start_mappers(src_dir: str) -> MetaData:
    """Discover orm.py files and run sqlalchemy's mappers automatically."""
    metadata = MetaData()
    orm_files = files.find("orm.py", src_dir)

    for path in orm_files:
        module = SourceFileLoader("start_mappers", path).load_module()
        module.start_mappers(metadata)  # type: ignore

    return metadata


def start_mappers(*modules: str) -> MetaData:
    """Update metadata reference and run sqlalchemy's mappers, classical way.

    :param modules: enumeration of the modules (dot-case format).

    Example:
    >>> start_mappers('my.module.1.orm', 'my.module.2.orm')
    """
    metadata = MetaData()

    for module_name in modules:
        module = import_module(module_name)
        module.start_mappers(metadata)  # type: ignore

    return metadata
