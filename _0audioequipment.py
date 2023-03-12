class AudioEquipment:
    def __init__(self, producer: str, **kwargs):
        self._producer = producer

    def play_music(self):
        return "Воспроизведение музыки"


    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, value):
        self._producer = value
