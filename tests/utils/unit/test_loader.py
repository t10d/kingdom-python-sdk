import tests.poc.loader_example.my_module
from kingdom_sdk.utils import loader


def test_object_from_module():
    foo = loader.object_from_module(
        "tests.poc.loader_example.my_module", "return_ok"
    )
    assert foo() == tests.poc.loader_example.my_module.return_ok()
