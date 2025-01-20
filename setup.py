from setuptools import setup

setup(
    name="zMIDIfilter",
    version="0.1",
    description="Filter MIDI Notes",
    author="Zedro",
    scripts=["run.sh"],
    install_requires=[
        "setuptools",
        "mididings",
    ],
    extras_require={
        "dev": ["debugpy", "black"],
    },
    data_files=[("scripts", ["run.sh"])],
)

