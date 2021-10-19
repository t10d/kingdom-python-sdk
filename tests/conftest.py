import pytest

import kingdom_sdk


@pytest.fixture
def base_dir():
    return kingdom_sdk._get_base_dir()  # noqa


@pytest.fixture
def src_dir():
    return kingdom_sdk._get_src_dir()  # noqa
