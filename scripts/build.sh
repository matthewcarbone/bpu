#!/bin/bash

PROJECT="accord"

bash scripts/install.sh build
echo "__version__ = '$(dunamai from any --style=pep440 --no-metadata)'" >"${PROJECT}"/_version.py
flit build
git checkout "${PROJECT}"/_version.py
