class CafeApp:

    def __init__(self, cafe):
        self._cafe = cafe

    def buy(self, drink: str, money: float):
        self._cafe.buy(drink, money)
