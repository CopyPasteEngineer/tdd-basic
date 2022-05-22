from app import CafeApp
from logic import DrinkNotInMenu, MoneyNotEnough


def test_should_call_cafe_buy():
    cafe = CafeMock()
    app = CafeApp(cafe=cafe, display=DisplayMock())
    app.buy("tea", 30.0)
    assert cafe.buy_is_called_with_parameters == ("tea", 30.0)


def test_should_display_drink_and_change_when_succeeded():
    display = DisplayMock()
    app = CafeApp(cafe=CafeMock(return_value=("tea", 10.0)), display=display)
    app.buy("tea", 30.0)
    assert display.displayed_text == "You bought tea. The change is 10.0 Baht. Thank you."


def test_should_display_message_when_DrinkNotInMenu_is_raised():
    display = DisplayMock()
    app = CafeApp(cafe=CafeMock(error=DrinkNotInMenu()), display=display)
    app.buy("cocoa", 100.0)
    assert display.displayed_text == "Sorry. We don't have cocoa."


def test_should_display_message_when_MoneyNotEnough_is_raised():
    display = DisplayMock()
    app = CafeApp(cafe=CafeMock(error=MoneyNotEnough()), display=display)
    app.buy("coffee", 5.0)
    assert display.displayed_text == "Sorry. 5.0 Baht is not enough for coffee."


class DisplayMock:
    def __init__(self):
        self.displayed_text = ""

    def __call__(self, text):
        self.displayed_text = text


class CafeMock:
    def __init__(self, return_value=None, error=None):
        self._return_value = return_value or ("", 0.0)
        self._error = error
        self.buy_is_called_with_parameters = ("", 0.0)

    def buy(self, drink: str, money: float) -> (str, float):
        self.buy_is_called_with_parameters = drink, money
        if self._error:
            raise self._error
        return self._return_value
