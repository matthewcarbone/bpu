# Version utilities
This module contains utilities for managing package versions, something that can be a pain in the neck to do by hand every time a project is released. We use [dunamai](https://github.com/mtkennerly/dunamai) as our package of choice to extract the current version from your version control system. It's an excellent tool and you should check it out!

## Usage
At some point in your code, you should have a `__version__` attribute importable via something like

```python
# __init__.py
from ._version import __version__

# _version.py
__version__ = "v0.0.1"
```

You can use `bpu.version` to replace this logic in the following way:

```python
# __init__.py
from ._version import __version__

# _version.py
from bpu.version import get_version

__version__ = get_version()
```

You can also pass a parameter, `fallback_version` to `get_version`. This fallback is set to `"dev"` by default but can be specified. It will be used if `dunamai` is not installed.

## An aside on building your packages

This allows for a flexible approach to both dynamic and static versioning. For example, you can use `_version.py` as a default for development as shown above, where `get_version` allows you to get the version of the code you're currently developing dynamically. However, when it comes to deploying the code on e.g. PyPI, you can completely replace the `_version.py` file using something like this:

```bash
# install build dependencies (including dunamai)
bash scripts/install.sh build

# completely replace _version.py using dunamai's command line interface
echo "__version__ = '$(dunamai from any --style=pep440 --no-metadata)'" >sva/_version.py

# then build your project using your tool of choice
flit build
```

