import os

from kingdom_sdk.utils import casting

try:
    from dotenv import load_dotenv

    load_dotenv()
except:  # noqa
    pass

DEFAULT_TIMEZONE_REGION = "America/Sao_Paulo"
DEFAULT_DEBUG = "False"
DEFAULT_DATABASE_URL = "postgresql://user:password@localhost:5432/database"
DEFAULT_REDIS_HOST = "127.0.0.1"
DEFAULT_REDIS_PORT = "6379"
DEFAULT_REDIS_PASSWORD = ""


def get_timezone_region() -> str:
    return os.environ.get("TIMEZONE_REGION", DEFAULT_TIMEZONE_REGION)


def is_debug_active() -> bool:
    value = os.environ.get("DEBUG", DEFAULT_DEBUG)
    return casting.bool_from_string(value)


def get_database_url() -> str:
    return os.environ.get("DATABASE_URL", DEFAULT_DATABASE_URL)


def get_redis_host() -> str:
    return os.environ.get("REDIS_HOST", DEFAULT_REDIS_HOST)


def get_redis_port() -> int:
    return int(os.environ.get("REDIS_PORT", DEFAULT_REDIS_PORT))


def get_redis_password() -> str:
    return os.environ.get("REDIS_PASSWORD", DEFAULT_REDIS_PASSWORD)
