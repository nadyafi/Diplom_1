class TestIngredient:

    def test_get_price_success(self, ingredient):
        assert ingredient.get_price() == 200.0

    def test_get_name_success(self, ingredient):
        assert ingredient.get_name() == 'hot sauce'

    def test_get_type_success(self, ingredient):
        assert ingredient.get_type() == 'FILLING' or 'SAUCE'
