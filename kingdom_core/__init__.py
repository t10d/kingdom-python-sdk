import os

# Define the package's version.
# - Is used for indexing and distributing the package
# - Follow the conventions defined by PEP440
__version__ = "0.1.0"


def _get_base_dir() -> str:
    """Return the absolute path for kingdom_core's root directory."""
    path, _ = os.path.split(os.path.dirname(__file__))
    return path


def _get_src_dir() -> str:
    """Return the absolute path for kingdom_core's source directory."""
    return os.path.dirname(__file__)