import allure

from data import Data
from praktikum.bun import Bun


class TestBun:
    @allure.title("Проверка, что метод возвращает верное название булки")
    def test_get_name_return_true_name(self):
        bun = Bun(Data.buns[2].get("name"), Data.buns[2].get("price"))
        name = bun.get_name()

        assert name == Data.buns[2].get("name")

    @allure.title("Проверка, что метод возвращает верную цену булки")
    def test_get_price_return_true_price(self):
        bun = Bun(Data.buns[2].get("name"), Data.buns[2].get("price"))
        price = bun.get_price()

        assert price == Data.buns[2].get("price")
