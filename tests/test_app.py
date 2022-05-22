from app import CafeApp


def test_should_call_cafe_buy():
    cafe = CafeMock()
    app = CafeApp(cafe=cafe)
    app.buy("tea", 30.0)
    assert cafe.buy_is_called_with_parameters == ("tea", 30.0)


class CafeMock:
    def __init__(self):
        self.buy_is_called_with_parameters = ("", 0.0)

    def buy(self, drink: str, money: float) -> (str, float):
        self.buy_is_called_with_parameters = drink, money
