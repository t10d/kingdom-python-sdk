from abc import ABC, abstractmethod


class AbstractAESAlgorithm(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self, string: str, encoding: str = "utf-8") -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, hex_string: str, encoding: str = "utf-8") -> str:
        raise NotImplementedError
