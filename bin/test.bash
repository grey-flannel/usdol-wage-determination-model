#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

uv run safety scan
uv run ruff check
uv run flake8 src tests
uv run bandit -r src
uv run bandit -r tests -s B101
uv run -m pytest -vv --cov=src --cov-report=term --cov-report=xml
