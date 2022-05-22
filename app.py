from logic import DrinkNotInMenu, MoneyNotEnough


class CafeApp:

    def __init__(self, cafe, display):
        self._cafe = cafe
        self._display = display

    def buy(self, drink: str, money: float):
        try:
            drink, change = self._cafe.buy(drink, money)
        except DrinkNotInMenu:
            self._display_drink_not_in_menu(drink)
        except MoneyNotEnough:
            self._display_money_not_enough(drink, money)
        else:
            self._display_buy_success(change, drink)

    def _display_money_not_enough(self, drink, money):
        self._display(f"Sorry. {money:.1f} Baht is not enough for {drink}.")

    def _display_buy_success(self, change, drink):
        self._display(f"You bought {drink}. The change is {change:.1f} Baht. Thank you.")

    def _display_drink_not_in_menu(self, drink):
        self._display(f"Sorry. We don't have {drink}.")
