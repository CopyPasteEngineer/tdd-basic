from pytest import raises

from logic import Cafe, DrinkNotInMenu, MoneyNotEnough


def test_should_return_tea_and_the_change_of_30_baht_when_buying_tea_with_50_baht():
    cafe = Cafe(randomly_select=RandomlySelectMock())
    drink, change = cafe.buy("tea", 50.0)
    assert (drink, change) == ("tea", 30.0)


def test_should_return_coffee_and_the_change_of_70_baht_when_buying_coffee_with_100_baht():
    cafe = Cafe(randomly_select=RandomlySelectMock())
    drink, change = cafe.buy("coffee", 100.0)
    assert (drink, change) == ("coffee", 70.0)


def test_should_raise_DrinkNotInMenu_when_buying_cocoa():
    cafe = Cafe(randomly_select=RandomlySelectMock())
    with raises(DrinkNotInMenu):
        cafe.buy("cocoa", 50.0)


def test_should_raise_MoneyNotEnough_when_buying_coffee_with_1_baht():
    cafe = Cafe(randomly_select=RandomlySelectMock())
    with raises(MoneyNotEnough):
        cafe.buy("coffee", 1.0)


def test_should_randomly_select_a_drink_between_tea_and_coffee_when_buying_surprise():
    random_mock = RandomlySelectMock()
    cafe = Cafe(randomly_select=random_mock)
    cafe.buy("surprise", 100.0)
    assert random_mock.is_called_with_choices == ["tea", "coffee"]


class RandomlySelectMock:
    def __call__(self, choices):
        self.is_called_with_choices = choices
