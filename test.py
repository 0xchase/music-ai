#!/usr/bin/python3

from src.song.session import *
from src.song.note import Note
from src.algorithms.generators.random import RandomClipGenerator

# Create a session, which contains all our tracks
session = Session("Test Session")

# Add tracks to the session
session.add_track(Track("Guitar"))

# Create a clip
clip = Clip(16)

# Add notes with pitch, note start, and note length to the clip
clip.add_note(Note("C1", 1), 1)
clip.add_note(Note("D1", 2), 1)
clip.add_note(Note("E1", 3), 1)
clip.add_note(Note("F1", 4), 1)
clip.add_note(Note("G1", 5), 1)
clip.add_note(Note("A1", 6), 1)
clip.add_note(Note("B1", 7), 1)
clip.add_note(Note("C2", 8), 1)

# Add the clip to the track
session.get_track("Guitar").add_clip(clip)

# -----------------------------------

session.add_track(Track("Piano"))

clip1 = RandomClipGenerator().generate(16)
clip2 = RandomClipGenerator().generate(16)
clip3 = RandomClipGenerator().generate(16)
clip4 = RandomClipGenerator().generate(16)

session.get_track("Piano").add_clip(clip1)
session.get_track("Piano").add_clip(clip2)
session.get_track("Piano").add_clip(clip3)
session.get_track("Piano").add_clip(clip4)

# Print the session
print(session)

