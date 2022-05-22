from logic import DrinkNotInMenu


class CafeApp:

    def __init__(self, cafe, display):
        self._cafe = cafe
        self._display = display

    def buy(self, drink: str, money: float):
        try:
            drink, change = self._cafe.buy(drink, money)
        except DrinkNotInMenu:
            self._display_drink_not_in_menu(drink)
        else:
            self._display_buy_success(change, drink)

    def _display_buy_success(self, change, drink):
        self._display(f"You bought {drink}. The change is {change:.1f} Baht. Thank you.")

    def _display_drink_not_in_menu(self, drink):
        self._display(f"Sorry. We don't have {drink}.")
