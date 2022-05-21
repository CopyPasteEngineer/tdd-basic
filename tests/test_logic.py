from logic import Cafe


def test_should_return_tea_and_the_change_of_30_baht_when_buying_tea_with_50_baht():
    cafe = Cafe()
    drink, change = cafe.buy("tea", 50.0)
    assert (drink, change) == ("tea", 30.0)
