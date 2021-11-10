from __future__ import annotations

import logging
from typing import Any, AsyncGenerator, Callable, Dict, List, Type

from kingdom_sdk.domain.exception import KingdomError
from kingdom_sdk.domain.message import Command, Event, Message
from kingdom_sdk.ports.message_bus import AbstractMessageBus
from kingdom_sdk.ports.unit_of_work import AbstractUnitOfWork

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MessageBus(AbstractMessageBus):
    _uow: AbstractUnitOfWork
    _event_handlers: Dict[Type[Event], List[Callable]]
    _command_handlers: Dict[Type[Command], Callable]
    _queue: List[Message]

    def __init__(
        self,
        uow: AbstractUnitOfWork,
        event_handlers: Dict[Type[Event], List[Callable]],
        command_handlers: Dict[Type[Command], Callable],
        queue: List[Message],
    ) -> None:
        self._uow = uow
        self._event_handlers = event_handlers
        self._command_handlers = command_handlers
        self._queue = queue

    @classmethod
    def create(
        cls,
        uow: AbstractUnitOfWork,
        event_handlers: Dict[Type[Event], List[Callable]],
        command_handlers: Dict[Type[Command], Callable],
        dependencies: Dict[str, Any],
    ) -> MessageBus:
        """Create a message bus with its handlers dependencies set
        programmatically.

        Default dependencies do matter and are used on production environments.
        """
        command_injected = {
            command_type: cls._inject_dependencies(
                command_handler, dependencies
            )
            for command_type, command_handler in command_handlers.items()
        }
        event_injected = {
            event_type: [
                cls._inject_dependencies(handler, dependencies)
                for handler in event_handlers
            ]
            for event_type, event_handlers in event_handlers.items()
        }
        return cls(
            uow=uow,
            event_handlers=event_injected,
            command_handlers=command_injected,
            queue=[],
        )

    async def _handle_event(self, event: Event) -> AsyncGenerator:
        for handler in self._event_handlers[type(event)]:
            logger.info(
                "Handling event %s with handler %s", event, handler.__name__
            )
            try:
                for warning in handler(event) or ():
                    yield warning
                self._queue.extend(self._uow.collect_new_events())
            except Exception as ex:
                logger.exception("Exception handling event %s: %s", event, ex)
                # raise

    async def _handle_command(self, command: Command) -> AsyncGenerator:
        logger.info("Handling command %s", command)
        try:
            handler = self._command_handlers[type(command)]
            for warning in handler(command) or ():
                yield warning
            self._queue.extend(self._uow.collect_new_events())
        except Exception as ex:
            logger.exception("Exception handling command %s: %s", command, ex)
            raise

    def _handle_map(self, message: Message) -> Callable:
        if isinstance(message, Event):
            return self._handle_event
        elif isinstance(message, Command):
            return self._handle_command
        else:
            raise UnknownMessage()

    async def handle(self, message: Message) -> List[Warning]:
        self._queue = [message]
        warnings = []
        while self._queue:
            # ever consuming queue
            current_msg = self._queue.pop(0)
            handle = self._handle_map(current_msg)
            warnings.extend(await self._run(handle(current_msg)))
        if self._queue:
            logger.warning(f"Not awaitable tasks: {self._queue}")
        return warnings

    @staticmethod
    async def _run(handler: AsyncGenerator) -> List[Any]:
        return [r async for r in handler]


class UnknownMessage(KingdomError):
    def __init__(self) -> None:
        super().__init__("Unknown Message", "UNKNOWN_MESSAGE")
