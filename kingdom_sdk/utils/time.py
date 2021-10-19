from datetime import datetime

import pytz

from kingdom_sdk.config import get_timezone_region


def generate_now() -> datetime:
    tz = pytz.timezone(get_timezone_region())
    return datetime.now(tz)
