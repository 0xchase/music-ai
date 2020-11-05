from .beat import Beat

class Measure:
    def __init__(self):
        length = 4
        self.beats = []

        for beat in range(0, length):
            self.beats.append(Beat())

    def __str__(self):
        return "[///]"

