import allure
import pytest
from praktikum.burger import Burger
from unittest.mock import Mock, patch


class TestBurger:
    @allure.title("Проверка верного значения аттрибута 'bun'")
    def test_create_burger_consist_bun_is_none(self):
        burger = Burger()

        assert burger.bun is None

    @allure.title("Проверка верного значения аттрибута 'ingredients'")
    def test_create_burger_consist_ingredients_is_empty_list(self):
        burger = Burger()

        assert burger.ingredients == []

    @allure.title("Проверка, что в атрибут 'bun' устанавливается объект класса 'Bun'")
    @patch("praktikum.bun.Bun")
    def test_set_buns_sets_valid_attribute(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @allure.title("Проверка, что в список ингридиентов добавляется объект класса 'Ingredient'")
    @patch("praktikum.ingredient.Ingredient")
    def test_add_ingredient_sets_valid_attribute(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    @allure.title("Проверка, что цена бургера рассчитывается верно")
    @pytest.mark.parametrize(
        'price_buns, price_ingr1, price_ingr2',
        [
            pytest.param(100.0, 20.0, 30.0, id="bun: 100.0, ingr1: 20.0, ingr2: 30.0, price = 250.0"),
            pytest.param(200.0, 50.0, 50.0, id="bun: 200.0, ingr1: 50.0, ingr2: 50.0, price = 500.0"),
            pytest.param(10.0, 5.5, 5.1, id="bun: 10.0, ingr1: 5.5, ingr2: 5.1, price = 30.6")
        ])
    def test_get_price_return_correct_result(self, price_buns, price_ingr1, price_ingr2):
        mock_bun = Mock()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_bun.get_price.return_value = price_buns
        mock_ingredient1.get_price.return_value = price_ingr1
        mock_ingredient2.get_price.return_value = price_ingr2

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        price_return = burger.get_price()

        assert price_return == price_buns * 2 + price_ingr1 + price_ingr2, "Цена рассчитана неверно."

    @allure.title("Проверка, что ингредиент удаляется верно")
    def test_remove_ingredient_correct_delete_ingredient(self):
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.remove_ingredient(0)

        assert burger.ingredients == [mock_ing2]

    @allure.title("Проверка, что ингредиент верно перемещается вверх и вниз")
    @pytest.mark.parametrize(
        'index, index_new',
        [
            (0, 1),
            (1, 1),
            (2, 0)
        ])
    def test_move_ingredient_correct_replace_ingredient(self, index, index_new):
        mock_1 = Mock()
        mock_2 = Mock()
        mock_3 = Mock()
        exp_res = [[mock_2, mock_1, mock_3], [mock_1, mock_2, mock_3], [mock_3, mock_1, mock_2]]
        burger = Burger()
        burger.ingredients = [mock_1, mock_2, mock_3]
        burger.move_ingredient(index, index_new)

        assert burger.ingredients == exp_res[index]

    @allure.title("Проверка, что рецепт верно печатается")
    def test_get_receipt_return_correct_value(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_name.return_value = "Булочка"
        mock_bun.get_price.return_value = 100.0
        mock_ingredient.get_name.return_value = "Острый"
        mock_ingredient.get_type.return_value = "соус"
        mock_ingredient.get_price.return_value = 100.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        return_receipt = burger.get_receipt()

        assert return_receipt == "(==== Булочка ====)\n= соус Острый =\n(==== Булочка ====)\n\nPrice: 300.0"
