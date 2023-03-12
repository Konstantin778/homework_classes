from _0audioequipment import AudioEquipment


class Speakers(AudioEquipment):

    material = "пластик"
    decoration = "прозрачный пластик"

    def __init__(self, loudness: int, **kwargs):
        self._loudness = loudness
        super().__init__(**kwargs)

    def get_extra(self):
        self.material = "дерево"
        self.decoration = "медь"

    @property
    def loudness(self):
        return self._loudness

    @loudness.setter
    def loudness(self, value):
        self._loudness = value