import os
from typing import Iterable, List


def find(
    file_name: str, base_dir: str, excluded_dirs: Iterable[str] = ()
) -> List[str]:
    """Return a list containing the paths of the files found."""
    return [
        os.path.join(root, file_name)
        for root, subdirs, files in os.walk(base_dir)
        if root not in excluded_dirs and file_name in files
    ]
