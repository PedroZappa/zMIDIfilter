# midi_filter
MIDI message Filter for Raspberry Pi 5 RNBO implementation

## Setup midi_filter

```sh
# Create venv for `midi_filter`
pyhon3 -m venv .venv
# Activate venv
source venv/bin/activate
# install Dependencies
pip install -r requirements.txt
```

## Usage

```sh
# Activate venv (if not already active)
source venv/bin/activate
# Run the script
mididings -f filter_note_off.py
# Setup ALSA MIDI routing w/ aconnect
aconnect "MIDI USB Device:0" "mididings:0"
aconnect "mididings:1" "RNBO:0"

```

