from praktikum.ingredient import Ingredient
from data import BurgerData
from praktikum.ingredient_types import *


class TestIngredient:

    def test_get_price_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.ingredient_type_sauce,
                                BurgerData.ingredient_price_sauce)
        assert ingredient.get_price() == 200.0

    def test_get_name_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.ingredient_type_sauce,
                                BurgerData.ingredient_price_sauce)
        assert ingredient.get_name() == 'hot sauce'

    def test_get_type_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.ingredient_type_sauce,
                                BurgerData.ingredient_price_sauce)
        assert ingredient.get_type() == 'SAUCE'
