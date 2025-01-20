#!/usr/bin/env bash
# set -euo pipefail
# -e : Exit immediately if a command exits with a non-zero status;
# -u : Treat unset variables as an error and exit;
# -o pipeline : Set the exit status to the last command in the pipeline that failed.

# Get the client and port info for MPK mini 3
output=$(aconnect -l | grep -A 1 "MPK mini 3")

# Use awk to process the output and remove the colon
echo "$output" | awk '/client/ {client=$2} /MIDI 1/ {port=$1} END {print substr(client, 1, length(client)-1), port}'
