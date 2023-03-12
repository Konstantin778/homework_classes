from _1_1headphones import Headphones


class Wire(Headphones):
    def __init__(self, wire_len: int, **kwargs):
        self._wire_len = wire_len
        super().__init__(**kwargs)

    def unravel_wire(self):
        time = self._wire_len * 0.1
        return f"Провод распутан за {time} секунд"

    @property
    def wire_len(self):
        return f"{self._wire_len} милиметров"

    @wire_len.setter
    def wire_len(self, value):
        self._wire_len = value


class MiniSpeaker:
    radius: int = 10


class Wireless(Headphones):
    mini_speaker = MiniSpeaker

    def __init__(self, battery_time: int, **kwargs):
        self._battery_time = battery_time
        super().__init__(**kwargs)

    def _use_wireless(self):
        return f"Работа в течение {self._battery_time} минут"

    def get_mini_speaker(self):
        return self.mini_speaker.radius





