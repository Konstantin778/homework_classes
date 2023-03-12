from _1_2hphone_types import Wireless


class TWS(Wireless):
    def __init__(self, box_material: str, pair_weight: int, **kwargs):
        self._box_material = box_material
        self.pair_weight = pair_weight
        super().__init__(**kwargs)

    def get_single_weight(self):
        return f"Вес одного наушника {self.pair_weight / 2} грамм"


class Hoop(Wireless):
    comfortable = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_advice(self):
        if not self.comfortable:
            return "Лучше поискать что-то другое"
        return "Хороший выбор"

