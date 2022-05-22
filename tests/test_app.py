from app import CafeApp


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


class DisplayMock:
    def __init__(self):
        self.displayed_text = ""

    def __call__(self, text):
        self.displayed_text = text


class CafeMock:
    def __init__(self, return_value=None):
        self._return_value = return_value or ("", 0.0)
        self.buy_is_called_with_parameters = ("", 0.0)

    def buy(self, drink: str, money: float) -> (str, float):
        self.buy_is_called_with_parameters = drink, money
        return self._return_value
