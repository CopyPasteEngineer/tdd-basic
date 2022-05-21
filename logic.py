class Cafe:
    PRICE = {
        "tea": 20.0,
        "coffee": 30.0,
    }

    def buy(self, drink: str, money: float) -> (str, float):
        change = money - self.PRICE[drink]
        return drink, change
