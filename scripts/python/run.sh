#!/bin/sh

. "$(dirname "$0")/setup.sh" "$@"

python ./api/application.py
