from importlib import import_module
from importlib.machinery import SourceFileLoader
from typing import Iterable, Optional

from sqlalchemy import MetaData

from kingdom_core.utils import files


def _load_start_mappers_auto(src_dir: str, metadata: MetaData) -> None:
    orm_files = files.find("orm.py", src_dir)
    for path in orm_files:
        module = SourceFileLoader("start_mappers", path).load_module()
        module.start_mappers(metadata)  # type: ignore


def _load_start_mappers_manual(
    modules: Iterable[str], metadata: MetaData
) -> None:
    for module_name in modules:
        module = import_module(module_name)
        module.start_mappers(metadata)  # type: ignore


def start_mappers(
    src_dir: Optional[str] = None,
    modules: Optional[Iterable[str]] = None,
) -> MetaData:
    """Update metadata reference and run sqlalchemy's mappers, classical way.

    :param src_dir: if wanted load all start_mappers automatically, inform this
    single path.
    :param modules: if wanted load only specific start_mappers, inform a
    list containing the modules (dot-case format).
    """
    if not src_dir and not modules:
        raise TypeError("One argument must be specified")

    if src_dir and modules:
        raise TypeError("The arguments are mutually exclusive")

    metadata = MetaData()

    if src_dir:
        _load_start_mappers_auto(src_dir, metadata)
    else:
        _load_start_mappers_manual(modules, metadata)

    return metadata
