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


def test_raise_command(raised_command):
    assert is_dataclass(raised_command)
    assert isinstance(raised_command, Message)
    assert isinstance(raised_command, Command)
    assert isinstance(raised_command.raised_at, datetime)
    assert isinstance(raised_command.delay, int)
    assert raised_command.name == "raised"
    assert raised_command.value == 1.0


def test_update_command_fail(raised_command):
    with pytest.raises(FrozenInstanceError):
        raised_command.name = "Changed!"


def test_raise_event(raised_event):
    assert is_dataclass(raised_event)
    assert isinstance(raised_event, Message)
    assert isinstance(raised_event, Event)
    assert isinstance(raised_event.raised_at, datetime)
    assert isinstance(raised_event.delay, int)
    assert isinstance(raised_event.raised_by, UUID)
    assert raised_event.name == "raised"


def test_update_event_fail(raised_event):
    with pytest.raises(FrozenInstanceError):
        raised_event.name = "Changed!"


def test_persistent_message_command(raised_command):
    pm = PersistentMessage.create(raised_command)
    obj = pm.load_object()
    assert obj == raised_command


def test_persistent_message_event(raised_event):
    pm = PersistentMessage.create(raised_event)
    obj = pm.load_object()
    assert obj == raised_event
