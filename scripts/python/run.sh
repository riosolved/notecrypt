#!/bin/sh

. "$(dirname "$0")/setup.sh" "$@"

python -B ./api/application.py
