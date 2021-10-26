import os

import pytest

import kingdom_sdk


@pytest.fixture
def base_dir():
    return kingdom_sdk._get_base_dir()  # noqa


@pytest.fixture
def src_dir():
    return kingdom_sdk._get_src_dir()  # noqa


@pytest.fixture
def poc_dir(base_dir):
    return os.path.join(base_dir, "tests/poc/")


@pytest.fixture
def query_path(poc_dir):
    return os.path.join(poc_dir, "context_example/queries/query.sql")
