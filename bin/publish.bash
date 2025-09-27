#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

rm -rf dist && uv build
uv publish -t $(keyring get https://upload.pypi.org/legacy/ __token__)
