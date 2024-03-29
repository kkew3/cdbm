#!/bin/bash
# It's totally okay to run this script with zsh.
set -e

# === Show help if requested ===
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    echo "BINDIR=/path/to/bin ./install.sh"
    exit 0
fi

# === Check dependencies ===
if ! command which python3 > /dev/null; then
    echo "python3 must be installed to run this script!" >&2
    exit 1
fi

# === Ensure BINDIR is set ===
if [ -z "$BINDIR" ]; then
    echo "BINDIR not set! Set it to, e.g., /usr/local/bin." >&2
    exit 1
fi

# === Handle python virtualenv ===
# Create a python virtualenv if not yet exists.
if [ ! -d venv ]; then
    python3 -m venv venv
fi
# Install the cdbm package to this venv.
./venv/bin/pip install .

# === Craft the launch script and install it to BINDIR ===
# It's assumed that there's no whitespace characters in $_PY.
_PY="$(pwd)/venv/bin/python3"
printf '#!/bin/sh\n%s -m cdbm "$@"\n' "$_PY" > cdbm.tmp
install -b cdbm.tmp "$BINDIR/cdbm"
rm cdbm.tmp
