from mididings import *

# Configure Global Settings
config(
    backend='alsa', # Alsa Sequencer
    # backend='jack', # Jack MIDI buffered
    # backend='jack-rt', # Jack MIDI direct
    client_name='zMidiFilter',
    in_ports = [
        ('MPK', '24:0')
    ],
    out_ports = [
        ('zMIDIfilter OUT', '14:0'),
    ],
)

def filterCCrelease(e):
    if e.type == CTRL : 
        if hasattr(e, 'value') and e.value == 0:
            return None
    # Allow all other messages
    return e

run(
    Process(filterCCrelease) >> Print()
)

