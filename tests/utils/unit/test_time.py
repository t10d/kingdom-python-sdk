from datetime import datetime

from kingdom_sdk.utils import time


def test_generate_now():
    assert isinstance(time.generate_now(), datetime)
