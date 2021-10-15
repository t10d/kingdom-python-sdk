import pytest

from kingdom_core.adapters.security.cryptography import PycryptoAESAlgorithm


def test_aes_encrypt_decrypt_ok():
    aes_algorithm = PycryptoAESAlgorithm("#" * 32)
    original_msg = "random_word()"

    encrypted_msg = aes_algorithm.encrypt(original_msg)
    assert encrypted_msg != original_msg

    decrypted_msg = aes_algorithm.decrypt(encrypted_msg)
    assert decrypted_msg == original_msg


def test_aes_invalid_secret():
    with pytest.raises(ValueError):
        PycryptoAESAlgorithm("#")
