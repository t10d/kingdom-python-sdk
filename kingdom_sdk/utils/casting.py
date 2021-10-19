def bool_from_string(string: str) -> bool:
    string = string.strip().lower()
    if string in ("true", "yes", "t", "y", "1"):
        return True
    elif string in ("false", "no", "f", "n", "0"):
        return False
    else:
        raise ValueError("String doesn't represent a valid boolean")
