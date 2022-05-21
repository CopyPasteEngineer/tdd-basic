class Cafe:
    def buy(self, drink: str, money: float) -> (str, float):
        return drink, money-20.0
