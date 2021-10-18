import pytest

import kingdom_core


@pytest.fixture
def base_dir():
    return kingdom_core._get_base_dir()  # noqa


@pytest.fixture
def src_dir():
    return kingdom_core._get_src_dir()  # noqa
