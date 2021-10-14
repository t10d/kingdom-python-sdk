import os

from kingdom_core.utils import files


def test_files_find_ok(src_dir):
    assert files.find(file_name="__init__.py", base_dir=src_dir)

    assert files.find(
        file_name="__init__.py",
        base_dir=src_dir,
        excluded_dirs=[os.path.join(src_dir, "utils")],
    )
