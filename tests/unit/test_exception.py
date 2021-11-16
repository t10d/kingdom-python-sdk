import os

from tests.poc.context_example.exception import ExampleError


class TestException:
    def test_error_message_debug_active(self):
        message = "Random message"
        error = ExampleError(message)

        os.environ["DEBUG"] = "True"

        assert error.code
        assert error.message == message
        assert message in str(error)
        assert message in repr(error)

    def test_error_message_debug_inactive(self):
        message = "Random message"
        error = ExampleError(message)

        os.environ["DEBUG"] = "False"

        assert error.code
        assert error.message == message
        assert message in str(error)
        assert message not in repr(error)
