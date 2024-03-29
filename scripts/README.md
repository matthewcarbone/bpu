# Helper scripts
While these scripts are used for making the build and installation processes easier for this repository, they might also be helpful for you (or me in the future)!

## Install script
`install.sh` is a helper script for installing various required dependencies from the `pyproject.toml` file in the root of the project.

For example, you can run `bash install.sh` to install the core project dependencies. Or, you can run `bash install.sh build` to install anything that the *build system* itself requires. The argument you supply to `install.sh` must match a sub-header under the `[project.optional-dependencies]` header in your `pyproject.toml` file, but otherwise the script takes care of the rest for you, using pip to install any package listed.

## Build script
`build.sh` builds the project. It does this in the following steps.

1. Installs all build dependencies using `bash install.sh build`. In this case, that's flit and dunamai.
2. Rewrites the `_version.py` file, using a fixed string from the dunamai command line interface to hard-code the current version.
3. Builds via `flit build`.
4. Reverts `_version.py` to it's previous state by using `git checkout`.
