from _0audioequipment import AudioEquipment


class Headphones(AudioEquipment):

    def __init__(self, colour: str, **kwargs):
        self._colour = colour
        super().__init__(**kwargs)

    def play_low(self):
        return "Воспроизведение напрямую в уши"

