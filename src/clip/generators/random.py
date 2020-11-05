from clip.abstract.generator import ClipGenerator
from song.clip import Clip


class RandomClipGenerator(ClipGenerator):
    def __init__(self):
        print("Created random clip generator")

    def generate(self, length: int):
        clip = Clip(4)
        for _ in length/4:
            clip.append(Measure())



        return s


    def info(self):
        return "Generates a clip using random note values"

