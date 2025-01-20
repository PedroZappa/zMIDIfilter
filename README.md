# zMIDIfilter
MIDI message Filter for MPK mini 3 (for use with RNBO)

This Python script filters MIDI Messages.
For the time being it only filters Control Change (CC) messages with a value of 0 from the MPK mini 3.

## Requirements:
- Python 3
- `mididings` library
- `aconnect` utility
- A Bash script `getMPK.sh` to fetch the MPK client and port dynamically.

## Usage:
1. Make sure your MPK mini 3 is connected.
2. Ensure `getMPK.sh` is executable (`chmod +x getMPK.sh`).
3. Run the script:

```bash
python3 app.py
```

## Setup zMIDIfilter

```sh
# Create venv for `zMIDIfilter`
./run.sh
```

## Usage

```sh
# Activate venv (if not already active)
source .venv/bin/activate
# Run the script
python3 app.py
# or
mididings -f app.py
```

