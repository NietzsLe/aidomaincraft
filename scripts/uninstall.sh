#!/bin/sh
# Remove aidomaincraft lookup blocks from a target repo or directory.
# All arguments are forwarded to scripts/aidomaincraft_setup.py uninstall.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$here/aidomaincraft_setup.py" uninstall "$@"
