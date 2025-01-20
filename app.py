from mididings import *

# Configuration: Use ALSA as the audio backend
config(
    backend='alsa',
)

# Define the MIDI routing and filtering logic
run(
    Selector([
        Filter(NOTEON),  # Pass only Note On messages
       Filter(CTRL)     # Pass Control Change (CC) messages
    ])
)
