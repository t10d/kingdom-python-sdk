import dataclasses
import json
from decimal import Decimal
from json import JSONEncoder
from typing import Any
from uuid import UUID


class CustomJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Decimal):
            return float(o)

        if isinstance(o, UUID):
            return str(o)

        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)

        return super().default(o)


def json_dumps(obj: Any) -> str:
    return json.dumps(obj, cls=CustomJSONEncoder)
