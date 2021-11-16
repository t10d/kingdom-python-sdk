from abc import ABC, abstractmethod
from typing import Dict, Iterator, Optional

from kingdom_sdk.domain.message import Message


class AbstractMessageBroker(ABC):
    @abstractmethod
    def publish(
        self, channel: str, message: Message, schedule: int = 0
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def subscribe(self, *channels: str) -> Iterator[Optional[Dict]]:
        raise NotImplementedError
