import pytest
import ingredient_types as it


class TestDatabase:

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300)
    ])
    def test_available_buns(self, database, name, price, bun):
        buns = database.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        bun_prices = [bun.get_price() for bun in buns]
        assert name in bun_names
        assert price in bun_prices

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (it.INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (it.INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (it.INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
        (it.INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (it.INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
        (it.INGREDIENT_TYPE_FILLING, 'sausage', 300)
    ])
    def test_available_ingredients(self, database, ingredient_type, name, price, ingredient):
        ingredients = database.available_ingredients()
        ingredient_types = [ingredient.get_type() for ingredient in ingredients]
        ingredient_names = [ingredient.get_name() for ingredient in ingredients]
        ingredient_prices = [ingredient.get_price() for ingredient in ingredients]
        assert ingredient_type in ingredient_types
        assert name in ingredient_names
        assert price in ingredient_prices
