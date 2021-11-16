from datetime import datetime

import pytz

from kingdom_sdk import config


def generate_now() -> datetime:
    tz = pytz.timezone(config.get_timezone_region())
    return datetime.now(tz)
