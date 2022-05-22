class CafeApp:

    def __init__(self, cafe, display):
        self._cafe = cafe
        self._display = display

    def buy(self, drink: str, money: float):
        drink, change = self._cafe.buy(drink, money)
        self._display(f"You bought {drink}. The change is {change:.1f} Baht. Thank you.")
