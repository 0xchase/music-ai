
class Beat:
    def __init__(self):
        self._notes = []

    def __delitem__(self, key):
        del self._notes[key]

    def __getitem__(self, key):
        return self._notes[key]

    def __setitem__(self, key, value):
        self._notes[key] = value

