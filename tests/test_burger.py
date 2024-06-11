from praktikum.burger import Burger
from praktikum.ingredient_types import *
from unittest.mock import Mock


def mock_sauce():
    m_sauce = Mock()
    m_sauce.get_price.return_value = 50.0
    m_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    m_sauce.get_name.return_value = 'Ketchup'
    return m_sauce


def mock_filling():
    m_filling = Mock()
    m_filling.get_price.return_value = 1000.0
    m_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    m_filling.get_name.return_value = 'Beef'
    return m_filling


def mock_bun():
    m_bun = Mock()
    m_bun.get_price.return_value = 100.0
    m_bun.get_name.return_value = 'Bun'
    return m_bun


class TestBurger:

    def test_set_buns_success(self):
        burger = Burger()
        bun = mock_bun()
        burger.set_buns(bun)
        assert bun == burger.bun

    def test_add_ingredient_success(self):
        burger = Burger()
        burger.set_buns(mock_bun())
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        assert burger.ingredients == [sauce]

    def test_remove_ingredient_success(self):
        burger = Burger()
        burger.set_buns(mock_bun())
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        filling = mock_filling()
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [filling]

    def test_move_ingredient_success(self):
        burger = Burger()
        burger.set_buns(mock_bun())
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        filling = mock_filling()
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [filling, sauce]

    def test_get_price_success(self):
        burger = Burger()
        bun = mock_bun()
        filling = mock_filling()
        bun.get_price.return_value = 100.0
        filling.get_price.return_value = 200.0
        burger.set_buns(bun)
        burger.add_ingredient(filling)
        assert burger.get_price() == 100.0 * 2 + 200.0

    def test_get_receipt_success(self):
        burger = Burger()
        bun = mock_bun()
        burger.set_buns(bun)
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        filling = mock_filling()
        burger.add_ingredient(filling)
        receipt = (
            '(==== Bun ====)\n'
            '= sauce Ketchup =\n'
            '= filling Beef =\n'
            '(==== Bun ====)\n\n'
            'Price: 1250.0'
        )
        assert burger.get_receipt() == receipt
