from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime
from uuid import UUID

import pytest

from kingdom_sdk.domain.message import (
    Command,
    Event,
    Message,
    PersistentMessage,
)


class TestCommand:
    def test_raise_command(self, example_command):
        assert is_dataclass(example_command)
        assert isinstance(example_command, Message)
        assert isinstance(example_command, Command)
        assert isinstance(example_command.raised_at, datetime)
        assert isinstance(example_command.delay, int)
        assert example_command.name == "raised"
        assert example_command.value == 1.0

    def test_update_command_fail(self, example_command):
        with pytest.raises(FrozenInstanceError):
            example_command.name = "Changed!"


class TestEvent:
    def test_raise_event(self, example_event):
        assert is_dataclass(example_event)
        assert isinstance(example_event, Message)
        assert isinstance(example_event, Event)
        assert isinstance(example_event.raised_at, datetime)
        assert isinstance(example_event.delay, int)
        assert isinstance(example_event.raised_by, UUID)
        assert example_event.name == "raised"

    def test_update_event_fail(self, example_event):
        with pytest.raises(FrozenInstanceError):
            example_event.name = "Changed!"


class TestPersistentMessage:
    def test_persistent_command(self, example_command):
        pm = PersistentMessage.create(example_command)
        obj = pm.load_object()
        assert obj == example_command

    def test_persistent_event(self, example_event):
        pm = PersistentMessage.create(example_event)
        obj = pm.load_object()
        assert obj == example_event
