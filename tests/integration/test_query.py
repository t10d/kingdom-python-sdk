from uuid import uuid4

from sqlalchemy.engine import CursorResult

from kingdom_sdk.adapters.query import DQLInterface


def test_query_missing_params(uow, query_path):
    query = DQLInterface(query_path)
    result = query.execute(uow, id=uuid4().hex)
    assert isinstance(result, CursorResult)


def test_query_full_params(uow, query_path):
    query = DQLInterface(query_path)
    result = query.execute(uow, id=uuid4().hex, name="%a%")
    assert isinstance(result, CursorResult)
