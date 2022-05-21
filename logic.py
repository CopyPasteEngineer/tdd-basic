class Cafe:
    PRICE = {
        "tea": 20.0,
        "coffee": 30.0,
    }

    def buy(self, drink: str, money: float) -> (str, float):
        self._validate_drink(drink)
        change = self._bill(drink, money)
        return drink, change

    def _bill(self, drink, money):
        change = money - self.PRICE[drink]
        if change < 0:
            raise MoneyNotEnough()
        return change

    def _validate_drink(self, drink):
        if drink not in self.PRICE:
            raise DrinkNotInMenu()


class DrinkNotInMenu(Exception):
    pass


class MoneyNotEnough(Exception):
    pass
