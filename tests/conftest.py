import pytest

import kingdom_core


@pytest.fixture
def base_dir():
    return kingdom_core.get_base_dir()


@pytest.fixture
def src_dir():
    return kingdom_core.get_src_dir()
