from _2_1speakers import Speakers

class Outdoors(Speakers):
    _water_resist = True

    def __init__(self, price: int, **kwargs):
        self.price = price
        super().__init__(**kwargs)

    def get_discount_price(self, discount = 10):
        final_sum = self.price - (self.price/100*discount)
        return final_sum


class Indoors(Speakers):
    water_resist = False
    additional_bonus = "подписка на музыкальный сервис на 3 месяца"

    def __init__(self, year: int, **kwargs):
        self.year = year
        super().__init__(**kwargs)

    def get_super_bonus(self):
        if self.year > 2020:
            return "Дополнительные предложения отсутствуют"
        return "Скидка 50%"