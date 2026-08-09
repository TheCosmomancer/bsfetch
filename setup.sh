#!/usr/bin/env bash
set -e

if ! command -v python3 &>/dev/null; then
        echo "Could not detect python. Please install python before proceeding." >&2
        exit 1
fi
if ! python3 -c "import colorama" &>/dev/null; then
        echo "Colorama not detected in provided python environment. Please install colorama before proceeding." >&2
        exit 1
fi

# --- Install the script itself ---
chmod +x bsfetch.py
sudo install -m 755 bsfetch.py /usr/local/bin/bsfetch
sudo mkdir -p /usr/local/share/bsfetch
sudo cp -r logo /usr/local/share/bsfetch

echo "Moved bsfetch.py to /usr/local/bin/bsfetch
You can now run it by typing: bsfetch"