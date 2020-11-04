#!/usr/bin/python3

from song.session import *

session = Session("Test Session")
session.add_track(Track("Piano"))
session.add_track(Track("Guitar"))
session.add_track(Track("Drums"))
session.add_track(Track("FX"))

session.get_track("Guitar").add_clip(Clip(16))

print(session)
