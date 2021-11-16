from kingdom_sdk import config


class KingdomError(Exception):
    _message: str
    _code: str

    def __init__(self, message: str, code: str) -> None:
        super().__init__(message)
        self._message = message
        self._code = code

    def __repr__(self) -> str:
        if config.is_debug_active():
            return f"{self.__class__.__name__}: {self.message} [{self.code}]"
        else:
            return self.code

    @property
    def message(self) -> str:
        return self._message

    @property
    def code(self) -> str:
        return self._code
