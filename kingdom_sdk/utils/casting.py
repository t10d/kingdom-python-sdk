from typing import Tuple


def bool_from_string(string: str) -> bool:
    string = string.strip().lower()
    if string in ("true", "yes", "t", "y", "1"):
        return True
    elif string in ("false", "no", "f", "n", "0"):
        return False
    else:
        raise ValueError("String doesn't represent a valid boolean")


def split_module_class(module: str) -> Tuple[str, str]:
    split = module.split(".")
    return ".".join(split[:-1]), split[-1]
