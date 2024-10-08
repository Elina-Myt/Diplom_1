from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


# Тесты на проверку получения данных из базы данных
class TestDataBase:

    def test_available_buns(self):
        data = Database()
        available_buns = data.available_buns()

        assert available_buns[0].get_name() == "black bun"
        assert available_buns[0].get_price() == 100

    def test_ingredient_from_database_get_name(self):
        data = Database()
        available_ingredients = data.available_ingredients()

        assert available_ingredients[1].get_name() == 'sour cream'
        assert available_ingredients[4].get_price() == 200
        assert available_ingredients[5].get_type() == 'FILLING'