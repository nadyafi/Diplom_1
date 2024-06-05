from bun import Bun


class TestBun:

    def test_get_name_success(self, bun):
        assert bun.get_name() == 'black bun'

    def test_get_price_success(self, bun):
        assert bun.get_price() == 100.0

    def test_get_name_new_name_success(self):
        self.new_bun = Bun('red bun', 2000.0)
        assert self.new_bun.get_name() == 'red bun'

    def test_get_price_new_price_success(self):
        self.new_bun = Bun('red bun', 2000.0)
        assert self.new_bun.get_price() == 2000.0
