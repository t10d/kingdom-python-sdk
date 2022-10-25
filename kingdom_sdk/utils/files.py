import os
from typing import Iterable


def find(
    file_name: str, base_dir: str, excluded_dirs: Iterable[str] = ()
) -> list[str]:
    """Return a list containing the paths of the files found."""
    return [
        os.path.join(root, file_name)
        for root, _, files in os.walk(base_dir)
        if root not in excluded_dirs and file_name in files
    ]
