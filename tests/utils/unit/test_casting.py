import pytest

from kingdom_sdk.utils import casting


@pytest.mark.parametrize(
    "string, expected_result",
    [
        (x, True)
        for x in (
            "true",
            "True",
            "TRUE",
            "yes",
            "Yes",
            "YES",
            "t",
            "T",
            "y",
            "Y",
            "1",
        )
    ]
    + [
        (x, False)
        for x in (
            "false",
            "False",
            "FALSE",
            "no",
            "No",
            "NO",
            "f",
            "F",
            "n",
            "N",
            "0",
        )
    ],
)
def test_cast_bool_from_string(string, expected_result):
    assert casting.bool_from_string(string) == expected_result


@pytest.mark.parametrize(
    "module, expected_result",
    [
        ("", ("", "")),
        ("A", ("", "A")),
        ("a.B", ("a", "B")),
        ("a.b.C", ("a.b", "C")),
        ("a_a_a.b_b_b.C_C_C", ("a_a_a.b_b_b", "C_C_C")),
    ],
)
def test_split_module_class(module, expected_result):
    assert casting.split_module_class(module) == expected_result
