#!/usr/bin/python3

import music21
from song.session import *
from clip.generators.random import RandomClipGenerator

session = Session("Test Session")
session.add_track(Track("Piano"))
session.add_track(Track("Guitar"))
session.add_track(Track("Drums"))
session.add_track(Track("FX"))

session.get_track("Guitar").add_clip(Clip(4))

print(session)

random = RandomClipGenerator()

clip = random.generate()

