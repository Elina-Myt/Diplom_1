from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


# Тесты на проверку получения данных
class TestIngredients:

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус Spicy-X',
                                90)
        assert ingredient.get_name() == 'Соус Spicy-X'

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус Spicy-X',
                                90)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                'Соус Spicy-X',
                                90)
        assert ingredient.get_price() == 90
