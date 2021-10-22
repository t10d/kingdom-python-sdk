from importlib import import_module
from typing import Any


def object_from_module(module_name: str, object_name: str) -> Any:
    module = import_module(module_name)
    return getattr(module, object_name)
