#!/usr/bin/env bash
set -e

echo "Manually triggering main.py"

cd /app

poetry run run-bot "$@"
