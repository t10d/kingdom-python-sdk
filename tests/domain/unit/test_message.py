from dataclasses import FrozenInstanceError
from datetime import datetime
from uuid import UUID

import pytest


def test_raise_command(raised_command):
    assert raised_command.type == "Command"
    assert isinstance(raised_command.kind, str)
    assert isinstance(raised_command.raised_at, datetime)
    assert isinstance(raised_command.delay, int)
    assert raised_command.name == "raised"
    assert raised_command.value == 1.0


def test_update_command_fail(raised_command):
    with pytest.raises(FrozenInstanceError):
        raised_command.value = 5.7


def test_raise_event(raised_event):
    assert raised_event.type == "Event"
    assert isinstance(raised_event.kind, str)
    assert isinstance(raised_event.raised_at, datetime)
    assert isinstance(raised_event.delay, int)
    assert isinstance(raised_event.raised_by, UUID)


def test_update_event_fail(raised_event):
    with pytest.raises(FrozenInstanceError):
        raised_event.type = "Changed!"
