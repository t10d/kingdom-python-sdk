# 🏰 Kingdom SDK

Library containing the core modules for the kingdom-python-server.

## Features

See the [changelog](./CHANGELOG.md) to see all the features supported.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `kingdom-sdk`.

```bash
pip install kingdom-sdk
```

You can use [poetry](https://python-poetry.org/) as well.

```bash
poetry add kingdom-sdk
```

## Usage

```python
from kingdom_sdk.utils import files

orm_files = files.find("orm.py", "/")
```

## Test

To test the database package, you need do it manually, running a migration. Make sure the database is configured before.

```bash
cd tests/poc/
alembic revision --autogenerate
alembic upgrade head
```

The rest, run `pytest`.

Don't commit the generated revision.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
