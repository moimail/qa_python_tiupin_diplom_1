import allure
from praktikum.ingredient import Ingredient
from data import Data


class TestIngredient:
    @allure.title("Проверка верного присваивания названия ингредиента")
    def test_name_of_ingredient_correct(self):
        ingredient = Ingredient(Data.ingredients[0].get("type"),
                                Data.ingredients[0].get("name"),
                                Data.ingredients[0].get("price"))

        assert ingredient.name == Data.ingredients[0].get("name")

    @allure.title("Проверка верного присваивания типа ингредиента")
    def test_type_of_ingredient_correct(self):
        ingredient = Ingredient(Data.ingredients[1].get("type"),
                                Data.ingredients[1].get("name"),
                                Data.ingredients[1].get("price"))

        assert ingredient.type == Data.ingredients[1].get("type")

    @allure.title("Проверка верного присваивания цены ингредиента")
    def test_price_of_ingredient_correct(self):
        ingredient = Ingredient(Data.ingredients[2].get("type"),
                                Data.ingredients[2].get("name"),
                                Data.ingredients[2].get("price"))

        assert ingredient.price == Data.ingredients[2].get("price")

    @allure.title("Проверка, что метод возвращает верное название ингредиента")
    def test_get_name_return_true_name(self):
        ingredient = Ingredient(Data.ingredients[0].get("type"),
                                Data.ingredients[0].get("name"),
                                Data.ingredients[0].get("price"))
        name = ingredient.get_name()

        assert name == Data.ingredients[0].get("name")

    @allure.title("Проверка, что метод возвращает верную цену ингредиента")
    def test_get_price_return_true_price(self):
        ingredient = Ingredient(Data.ingredients[2].get("type"),
                                Data.ingredients[2].get("name"),
                                Data.ingredients[2].get("price"))
        price = ingredient.get_price()

        assert price == Data.ingredients[2].get("price")

    @allure.title("Проверка, что метод возвращает верный тип ингредиента")
    def test_get_type_return_true_type(self):
        ingredient = Ingredient(Data.ingredients[1].get("type"),
                                Data.ingredients[1].get("name"),
                                Data.ingredients[1].get("price"))
        type_ing = ingredient.get_type()

        assert type_ing == Data.ingredients[1].get("type")
