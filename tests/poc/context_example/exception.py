from kingdom_sdk.domain.exception import KingdomError


class ExampleError(KingdomError):
    def __init__(self, message: str):
        super().__init__(message, "EXAMPLE_ERROR")
