from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import Any, Callable, Type

from kingdom_sdk.domain.message import Command, Event, Message
from kingdom_sdk.ports.unit_of_work import AbstractUnitOfWork


class AbstractMessageBus(ABC):
    @classmethod
    @abstractmethod
    def create(
        cls,
        uow: AbstractUnitOfWork,
        event_handlers: dict[Type[Event], list[Callable]],
        command_handlers: dict[Type[Command], Callable],
        dependencies: dict[str, Any],
    ) -> AbstractMessageBus:
        raise NotImplementedError

    @abstractmethod
    async def handle(self, message: Message) -> list[Warning]:
        raise NotImplementedError

    @staticmethod
    def _inject_dependencies(
        handler: Callable, dependencies: dict[str, Any]
    ) -> Callable:
        """Inspect a handler function to figure out its arguments and returns
        the same handler with its arguments already set given a dependencies
        mapping.
        """
        params = inspect.signature(handler).parameters
        set_dependencies = {
            param: dependency
            for param, dependency in dependencies.items()
            if param in params
        }
        return lambda message: handler(message, **set_dependencies)
