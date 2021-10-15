from Crypto.Cipher import AES

from kingdom_core.ports.security.cryptography import AbstractAESAlgorithm


class PycryptoAESAlgorithm(AbstractAESAlgorithm):
    PADDING = b"\0"

    def __init__(self, secret_key: str):
        if len(secret_key) != 32:
            raise ValueError("secret_key lenght must be 32.")

        super().__init__()
        self.aes_algorithm = AES.new(secret_key, AES.MODE_ECB)

    def encrypt(self, string: str, encoding: str = "utf-8") -> str:
        byte_string: bytes = self.aes_algorithm.encrypt(
            self._strjust(string.encode(encoding))
        )
        return byte_string.hex()

    def decrypt(self, hex_string: str, encoding: str = "utf-8") -> str:
        byte_string = bytes.fromhex(hex_string)
        return (
            self.aes_algorithm.decrypt(byte_string)
            .lstrip(self.PADDING)
            .decode(encoding)
        )

    def _strjust(self, bytes_string: bytes) -> bytes:
        lenght = len(bytes_string)
        nfill = 16 - (lenght % 16)
        return bytes_string.rjust(lenght + nfill, self.PADDING)
