# zMIDIfilter
MIDI message Filter for Raspberry Pi 5 RNBO implementation

## Setup midi_filter

```sh
# Create venv for `midi_filter`
./run.sh
```

## Usage

```sh
# Activate venv (if not already active)
source venv/bin/activate
# Run the script
mididings -f app.py
# Setup ALSA MIDI routing w/ aconnect (NEEDS TESTING)
aconnect "MIDI USB Device:0" "mididings:0"
aconnect "mididings:1" "RNBO:0"

```

