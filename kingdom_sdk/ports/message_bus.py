from abc import ABC, abstractmethod
from typing import List

from kingdom_sdk.domain.message import Message


class AbstractMessageBus(ABC):
    @abstractmethod
    async def handle(self, message: Message) -> List[Warning]:
        raise NotImplementedError
