from praktikum.bun import Bun
from data import BurgerData


class TestBun:

    def test_get_name_success(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price)
        assert bun.get_name() == 'black bun'

    def test_get_price_success(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price)
        assert bun.get_price() == 100.0
