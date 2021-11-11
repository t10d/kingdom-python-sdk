from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValueObject(ABC):
    """Represent a transient value.

    Implement it as a frozen dataclass.

    >>> @dataclass(frozen=True)
    ... class MyClass(ValueObject):
    ...     field: type
    ...
    ...     @classmethod
    ...     def create(cls, ...) -> MyClass:
    ...         ...
    """

    @classmethod
    def create(cls, **kwargs: Any) -> ValueObject:
        raise NotImplementedError
