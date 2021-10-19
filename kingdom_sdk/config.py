import os

from kingdom_sdk.utils import casting

DEFAULT_TIMEZONE_REGION = "America/Sao_Paulo"
DEFAULT_DEBUG = "False"


def get_timezone_region() -> str:
    return os.environ.get("TIMEZONE_REGION", DEFAULT_TIMEZONE_REGION)


def is_debug_active() -> bool:
    value = os.environ.get("DEBUG", DEFAULT_DEBUG)
    return casting.bool_from_string(value)
