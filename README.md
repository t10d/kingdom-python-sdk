# 🏰 Kingdom Core

Library containing the core modules for the kingdom-python-server.

## Test

To test the database package, you need do it manually, running a migration. Make sure the databse is configured before.

```bash
cd tests/poc/
alembic revision --autogenerate
alembic upgrade head
```

The rest, run `pytest`.

Don't commit the generated revision.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `kingdom-core`.

```bash
pip install kingdom-core
```

You can use [poetry]() as well.

```bash
poetry add kingdom-core
```

## Usage

```python
from kingdom_sdk.utils import files

orm_files = files.find("orm.py", "/")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

> This file is based on [Make a README](https://www.makeareadme.com/).
