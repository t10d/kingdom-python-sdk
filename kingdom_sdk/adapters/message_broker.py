from typing import Dict, Iterator, Optional

from redis import Redis

from kingdom_sdk import config
from kingdom_sdk.domain.message import Message
from kingdom_sdk.ports.message_broker import AbstractMessageBroker
from kingdom_sdk.utils.serializer import json_dumps


class RedisMessageBroker(AbstractMessageBroker):
    _redis: Redis

    def __init__(self) -> None:
        self._redis = Redis(
            host=config.get_redis_host(),
            port=config.get_redis_port(),
            password=config.get_redis_password(),
        )

    def publish(
        self, channel: str, message: Message, schedule: int = 0
    ) -> None:
        msg = message.__dict__
        msg["schedule"] = schedule
        del msg["raised_at"]  # doesn't make sense to be recreated
        self._redis.publish(channel, json_dumps(msg))

    def subscribe(self, *channels: str) -> Iterator[Optional[Dict]]:
        pubsub = self._redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(*channels)
        return pubsub.listen()  # type: ignore
