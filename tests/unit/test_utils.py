import os
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

import pytest

import tests.poc.loader_example.my_module
from kingdom_sdk.utils import casting, files, loader, serializer, time


class TestCasting:
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
    def test_cast_bool_from_string(self, string, expected_result):
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
    def test_split_module_class(self, module, expected_result):
        assert casting.split_module_class(module) == expected_result


class TestFiles:
    def test_files_find_ok(self, src_dir):
        assert files.find(file_name="__init__.py", base_dir=src_dir)

        assert files.find(
            file_name="__init__.py",
            base_dir=src_dir,
            excluded_dirs=[os.path.join(src_dir, "utils")],
        )


class TestLoader:
    def test_object_from_module(self):
        foo = loader.object_from_module(
            "tests.poc.loader_example.my_module", "return_ok"
        )
        assert foo() == tests.poc.loader_example.my_module.return_ok()


class TestTime:
    def test_generate_now(self):
        assert isinstance(time.generate_now(), datetime)


class TestSerializer:
    def test_serialize_decimal(self):
        value = Decimal("1.0")
        assert str(value) == serializer.json_dumps(value)

    def test_serialize_uuid(self):
        value = uuid4()
        assert f'"{value}"' == serializer.json_dumps(value)
