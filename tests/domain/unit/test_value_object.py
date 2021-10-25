from dataclasses import FrozenInstanceError

import pytest


def test_vo_creation(default_value_object):
    assert default_value_object.field == "immutable"


def test_vo_update_failed(default_value_object):
    with pytest.raises(FrozenInstanceError):
        default_value_object.field = "changed!"
