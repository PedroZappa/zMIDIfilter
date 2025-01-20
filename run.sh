#!/usr/bin/env bash
# set -euo pipefail
# -e : Exit immediately if a command exits with a non-zero status;
# -u : Treat unset variables as an error and exit;
# -o pipeline : Set the exit status to the last command in the pipeline that failed.

# Load Colors
if [ -d ~/.dotfiles ]; then
    source ~/.dotfiles/scripts/colors.sh
else
    if [ ! -f ~/colors.sh ]; then
        echo -e "${YEL}Colors script not found, downloading: ${D}"
        wget https://raw.githubusercontent.com/PedroZappa/.dotfiles.min/refs/heads/main/scripts/colors.sh
    fi
    source ./colors.sh
fi

# Navigate to the filter program directory
cd ~/midi_filter

# Check if venv is created, if not create it
if [ ! -d .venv ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -e .[dev]
    echo "${GRN}.venv created${D}"
    pip list
fi

# Activate the virtual environment
source .venv/bin/activate

# Start mididings with the filter script
# mididings -f midi_filter.py

# Remove the colors script
if [ -f "~/colors.sh" ]; then
    rm ~/colors.sh
fi
