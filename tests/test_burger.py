class TestBurger:

    def test_set_buns_success(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert mock_bun == burger.bun

    def test_add_ingredient_success(self, burger, mock_bun, sauce, filling):
        burger.set_buns(mock_bun())
        burger.add_ingredient(sauce)
        assert burger.ingredients == [sauce]

    def test_remove_ingredient_success(self, burger, sauce, filling, mock_bun):
        burger.set_buns(mock_bun())
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [filling]

    def test_move_ingredient_success(self, burger, sauce, filling, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [filling, sauce]

    def test_get_price_success(self, burger, mock_bun, filling):
        mock_bun.get_price.return_value = 100.0
        filling.get_price.return_value = 200.0
        burger.set_buns(mock_bun)
        burger.add_ingredient(filling)
        assert burger.get_price() == 100.0 * 2 + 200.0

    def test_get_receipt_success(self, burger, mock_bun, sauce, filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        receipt = (
            '(==== Bun ====)\n'
            '= sauce Ketchup =\n'
            '= filling Beef =\n'
            '(==== Bun ====)\n\n'
            'Price: 1250.0'
        )
        assert burger.get_receipt() == receipt
