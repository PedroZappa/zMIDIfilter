"""
This script sets up a MIDI filter using mididings, fetching the MPK mini 3 client
and port dynamically, and applying a filter to remove Control Change (CC) messages
with a value of 0 (release events).

Requirements:
    - `mididings` Python package
    - `aconnect` command to list MIDI connections
    - Bash script `getMPK.sh` to fetch MPK client and port

Workflow:
    1. Fetch MPK mini 3 client and port.
    2. Configure `mididings` with the obtained values.
    3. Filter CC messages with a value of 0.
"""

# === Import Dependencies ===

import subprocess
import logging
from mididings import *

# === Functions ===

# Function to fetch the MPK mini 3 client and port
def get_mpk_ports():
    """
    Fetches the client and port for the MPK mini 3 from the aconnect output.
    
    Returns:
        tuple: A tuple containing the client ID and port number as strings.
    """
    try:
        # Call the Bash script that fetches the client and port
        output = subprocess.check_output(['./getMPK.sh']).decode('utf-8').strip()
        # Split the output into client and port
        client, port = output.split()
        return client, port
    except subprocess.CalledProcessError as e:
        logging.error(f"Error fetching MPK mini 3 port: {e}")
        raise

def filterCCrelease(e):
    if e.type == CTRL : 
        if hasattr(e, 'value') and e.value == 0:
            return None # Ignore CC release (value == 0)
    # Allow all other messages
    return e

# === Init ===

# Init Logging
logging.basicConfig(level=logging.INFO)

# Get MPK mini 3 client and port dynamically
client, port = get_mpk_ports()

# Configure Mididings Global Settings
config(
    backend='alsa', # Alsa Sequencer
    # backend='jack', # Jack MIDI buffered
    # backend='jack-rt', # Jack MIDI direct
    client_name='zMidiFilter',
    in_ports = [
        (f'MPK mini 3', f'{client}:{port}')
    ],
    out_ports = [
        ('zMIDIfilter OUT', '14:0'),
    ],
)

# Start Mididings
run(
    Process(filterCCrelease) >> Print()
)
